---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Problem Statement

A system consists of particles with [[Def - Four-Momentum and Rest Mass|four-momenta]] $P_1, \ldots, P_N$. Define its **invariant mass** $M$ by $M^2 = P\cdot P$ where $P = \sum_a P_a$ is the total four-momentum.

1. Show that $M$ is a Lorentz invariant, and that in the **centre-of-momentum frame** (where $\sum_a \mathbf{p}_a = 0$) it equals the total energy: $M = E_{\text{cm}}$.
2. Show that $M \ge \sum_a m_a$, with equality if and only if all the particles are at rest relative to one another.
3. Compute the invariant mass of a system of **two photons** of energies $E_1, E_2$ whose directions make an angle $\theta$. When is it zero?
4. Compute the invariant mass of **two massive particles** of mass $m$ each, moving with the same speed in opposite directions (Lorentz factor $\Gamma$ each), and compare with $2m$.

Work with $c = 1$.

**Recall:**

The four-momentum of a particle satisfies the mass-shell relation:

![[Def - Four-Momentum and Rest Mass#The Definition]]

The total four-momentum of a system is the sum $P = \sum_a P_a$, conserved for an isolated system ([[Thm - Conservation of Four-Momentum]]). A [[Def - The Four-Momentum of a Photon|photon]] has a null four-momentum, $P_\gamma\cdot P_\gamma = 0$, and relative to an observer $P_\gamma = E(U_0 + \mathbf{n})$ with $\mathbf{n}$ its unit direction. The Minkowski inner product is $A\cdot B = A^0 B^0 - \mathbf{A}\cdot\mathbf{B}$, a Lorentz scalar.

---

# Convergent Strategy

**Problem class.** A *find-an-invariant* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|central type]]: the quantity asked for (the system mass) is the Minkowski length of a four-vector (the total four-momentum), so it is computed by squaring and is the same in every frame. Once recognised as an invariant, evaluate it in the most convenient frame.

**Assumption pattern.** The system is a collection of four-momenta; the invariant mass is built from their sum. The signpost is "mass of a *system*" — this is *not* the sum of the parts' masses but the length of the total four-momentum, and the cross terms $2P_a\cdot P_b$ carry all the interesting physics (relative motion, the photon-system mass).

**Theorem routing.** Part 1 uses that $P\cdot P$ is a Lorentz scalar ([[Def - Four-Momentum and Rest Mass]]) and that in the centre-of-momentum frame $P = (E_{\text{cm}}, \mathbf{0})$. Part 2 uses the reversed Cauchy–Schwarz inequality for future-timelike four-vectors via [[Thm - Mass-Energy Equivalence]]. Parts 3–4 are direct expansions of $(\sum P_a)^2$ using $P_a\cdot P_a = m_a^2$ (or $0$ for photons) and the inner-product formula.

**Key decision point.** The crux is *not* to compute in the lab frame and chase $\gamma$ factors, but to recognise the system mass as an invariant and evaluate it where it is simplest — the centre-of-momentum frame for parts 1–2, and directly via the inner-product formula for the explicit cases 3–4. The non-obvious content is that two massless particles can form a *massive* system.

---

# Legal Operations Used

1. **Square a four-momentum to extract an invariant mass** (operation 2 from the topic page). The system mass is $\sqrt{(\sum P_a)^2}$; squaring the total four-momentum is the entire method.

2. **Go to the centre-of-momentum frame** (operation 3). In this frame the total spatial momentum vanishes, so $P = (E_{\text{cm}}, \mathbf{0})$ and the invariant is just $E_{\text{cm}}^2$, giving part 1.

3. **Use a Lorentz invariant to switch frames** (operation 6). The invariance of $P\cdot P$ is what lets the value computed in the centre-of-momentum frame be transported to any other.

---

# Hints

> [!note]- Hint 1
> The invariant mass is $M^2 = P\cdot P$ with $P = \sum_a P_a$. The inner product of four-vectors is the same in every frame, so $M$ is an invariant. To find its value, evaluate $P\cdot P$ in the frame where $\sum_a\mathbf{p}_a = 0$.

> [!note]- Hint 2
> Expand $M^2 = (\sum_a P_a)\cdot(\sum_a P_a) = \sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b$. For two future-timelike four-momenta, $P_a\cdot P_b \ge m_a m_b$ (the reversed Cauchy–Schwarz inequality), with equality iff $P_a \parallel P_b$ (parallel four-velocities, i.e. relative rest).

> [!note]- Hint 3
> For two photons, $P_1\cdot P_1 = P_2\cdot P_2 = 0$, so $M^2 = 2P_1\cdot P_2$. Use $P_1\cdot P_2 = E_1 E_2(1-\cos\theta)$ (from the photon directions making angle $\theta$). It vanishes only when $\theta = 0$ — collinear photons.

> [!note]- Hint 4
> For two massive particles, $M^2 = 2m^2 + 2P_1\cdot P_2$. With equal speeds in opposite directions, each has $P = (\Gamma m, \pm\Gamma m v\,\hat{\mathbf{x}})$, so $P_1\cdot P_2 = \Gamma^2 m^2(1 + v^2)$... or work in the centre-of-momentum frame, which is the lab here, where $M = E_{\text{cm}} = 2\Gamma m$.

---

# Solution

The invariant mass of a system is the Minkowski length of its total four-momentum, $M = \sqrt{(\sum P_a)^2}$ — an invariant equal to the total energy in the centre-of-momentum frame. The proof breaks into four parts: Part 1 uses frame-invariance of $P\cdot P$ and the centre-of-momentum frame; Part 2 uses the reversed Cauchy–Schwarz inequality; Parts 3–4 expand the square explicitly. The non-obvious result is that two photons form a massive system, because the mass is the length of the *sum* of two null vectors.

**Step 1: $M$ is invariant and equals $E_{\text{cm}}$.**

> [!note]- Derivation
> The total four-momentum $P = \sum_a P_a$ is a four-vector (a sum of four-vectors), so its Minkowski square $P\cdot P$ is a Lorentz scalar — the same number in every inertial frame. Hence $M = \sqrt{P\cdot P}$ is a Lorentz invariant.
>
> To evaluate it, go to the **centre-of-momentum frame**, defined by $\sum_a\mathbf{p}_a = \mathbf{0}$. There the total four-momentum has no spatial part: $P = (E_{\text{cm}}, \mathbf{0})$ with $E_{\text{cm}} = \sum_a E_a^*$ the total energy in that frame. Then
> $$M^2 = P\cdot P = E_{\text{cm}}^2 - |\mathbf{0}|^2 = E_{\text{cm}}^2,$$
> so $M = E_{\text{cm}}$. The invariant mass is the total energy *in the frame where the system is at rest as a whole*. (Such a frame exists whenever $P$ is timelike, i.e. $M > 0$; it fails only for a system of collinear massless particles, where $P$ is null and $M = 0$.)

**Step 2: $M \ge \sum_a m_a$, equality iff mutual rest.**

> [!note]- Derivation
> Expand the square of the total four-momentum:
> $$M^2 = \Big(\sum_a P_a\Big)\cdot\Big(\sum_b P_b\Big) = \sum_a P_a\cdot P_a + 2\sum_{a<b}P_a\cdot P_b = \sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b.$$
> For two future-directed timelike four-momenta $P_a = m_a U_a$, $P_b = m_b U_b$, the **reversed Cauchy–Schwarz inequality** for future-timelike vectors gives $U_a\cdot U_b \ge 1$, hence $P_a\cdot P_b = m_a m_b\,(U_a\cdot U_b) \ge m_a m_b$, with equality iff $U_a = U_b$ (the particles share a four-velocity, i.e. are at relative rest). (The reversed inequality holds because $U_a\cdot U_b = \Gamma_{\text{rel}}$ is the relative Lorentz factor, always $\ge 1$.) Therefore
> $$M^2 \ge \sum_a m_a^2 + 2\sum_{a<b}m_a m_b = \Big(\sum_a m_a\Big)^2,$$
> so $M \ge \sum_a m_a$, with equality iff every pair is at relative rest. Physically: a system in internal motion weighs more than the sum of its parts, by the internal kinetic energy; only a system with no internal motion has $M = \sum m_a$. (Binding — negative interaction energy — can lower $M$ below $\sum m_a$, but that requires interaction energy not captured by free four-momenta.)

**Step 3: Two-photon invariant mass.**

> [!note]- Derivation
> For two photons, $P_1\cdot P_1 = P_2\cdot P_2 = 0$ (null), so
> $$M^2 = (P_1 + P_2)^2 = 0 + 0 + 2P_1\cdot P_2 = 2P_1\cdot P_2.$$
> Relative to an observer, $P_1 = E_1(U_0 + \mathbf{n}_1)$, $P_2 = E_2(U_0 + \mathbf{n}_2)$ with $\mathbf{n}_1\cdot\mathbf{n}_2 = -\cos\theta$ (Minkowski; the spatial directions make angle $\theta$). Then
> $$P_1\cdot P_2 = E_1 E_2(U_0 + \mathbf{n}_1)\cdot(U_0 + \mathbf{n}_2) = E_1 E_2(1 + \mathbf{n}_1\cdot\mathbf{n}_2) = E_1 E_2(1 - \cos\theta),$$
> so
> $$\boxed{\ M^2 = 2E_1 E_2(1 - \cos\theta)\ }.$$
> This is **nonzero** for any $\theta \ne 0$, even though both photons are massless: two photons in different directions form a *massive* system. It vanishes only when $\theta = 0$ (collinear photons moving the same way), where the total four-momentum is null. For $\theta = \pi$ (head-on), $M^2 = 4E_1 E_2$, $M = 2\sqrt{E_1 E_2}$ — the invariant mass of, for instance, two photons that could pair-produce.

**Step 4: Two massive particles, opposite directions.**

> [!note]- Derivation
> Two particles of mass $m$ move with speed $v$ (Lorentz factor $\Gamma$) in opposite directions along $\hat{\mathbf{x}}$: $P_1 = (\Gamma m, \Gamma m v\,\hat{\mathbf{x}})$, $P_2 = (\Gamma m, -\Gamma m v\,\hat{\mathbf{x}})$. The total spatial momentum is $\Gamma m v - \Gamma m v = 0$, so this frame *is* the centre-of-momentum frame, and by Step 1, $M = E_{\text{cm}} = E_1 + E_2 = 2\Gamma m$.
>
> Check by direct expansion: $P_1\cdot P_2 = (\Gamma m)^2 - (\Gamma m v)(-\Gamma m v) = \Gamma^2 m^2(1 + v^2)$, so
> $$M^2 = 2m^2 + 2\Gamma^2 m^2(1+v^2) = 2m^2[1 + \Gamma^2(1+v^2)] = 2m^2\cdot 2\Gamma^2 = 4\Gamma^2 m^2,$$
> using $1 + \Gamma^2(1+v^2) = 1 + \Gamma^2 + \Gamma^2 v^2 = \Gamma^2 + \Gamma^2 = 2\Gamma^2$ (since $1 + \Gamma^2 v^2 = \Gamma^2$). Hence $M = 2\Gamma m > 2m$: the system weighs *more* than the sum of the parts' masses, by exactly the total energy $2\Gamma m$ over the rest masses $2m$, i.e. the kinetic energy. As $v\to 0$, $\Gamma\to 1$ and $M\to 2m$, recovering additivity at relative rest.

> [!note]- Complete formal solution
> The invariant mass is $M = \sqrt{P\cdot P}$, $P = \sum_a P_a$. **(1)** $P$ is a four-vector, so $P\cdot P$ is a Lorentz scalar and $M$ is invariant; in the centre-of-momentum frame $P = (E_{\text{cm}}, \mathbf{0})$, giving $M = E_{\text{cm}}$. **(2)** $M^2 = \sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b$, and $P_a\cdot P_b = m_a m_b(U_a\cdot U_b) \ge m_a m_b$ (reversed Cauchy–Schwarz, equality iff $U_a = U_b$), so $M^2 \ge (\sum_a m_a)^2$, i.e. $M \ge \sum_a m_a$ with equality iff all parts are at relative rest. **(3)** For two photons $M^2 = 2P_1\cdot P_2 = 2E_1 E_2(1-\cos\theta)$, nonzero unless $\theta = 0$. **(4)** Two mass-$m$ particles at speed $v$ in opposite directions are in their own centre-of-momentum frame, so $M = 2\Gamma m > 2m$, the system mass exceeding the sum of masses by the internal kinetic energy. $\blacksquare$

---

# Key Takeaways

**Mass is the length of the total four-momentum, and length is not additive.** The single most important lesson of this exercise is that the mass of a system is computed by *summing four-momenta and then taking the Minkowski length*, never by summing masses. The reusable trigger is the phrase "mass of a system" or "invariant mass": whenever you see it, reach for $M = \sqrt{(\sum P_a)^2}$, expand the square, and watch the cross terms $2P_a\cdot P_b$ appear — those cross terms are where the relative motion lives, and they are exactly what makes $M \ne \sum m_a$. This pattern recurs throughout particle physics: the invariant mass of a particle's decay products reconstructs the parent's mass (how the Higgs was found, as a bump in the di-photon invariant-mass spectrum at $125$ GeV), and the same calculation in reverse gives reaction thresholds. The diagnostic to carry away: a system in internal motion is heavier than its parts, a bound system is lighter, and only a system at internal rest has additive mass.

**Two massless particles can be massive — the photon-system mass is the cleanest illustration.** It is counterintuitive that two photons, each with $P\cdot P = 0$, form a system with $M^2 = 2E_1 E_2(1-\cos\theta) > 0$. The resolution is that the mass is the length of the *sum* of the four-momenta, and two null vectors pointing in different directions sum to a *timelike* vector — the future light cone is not closed under addition. This is not a curiosity: it is why two photons can pair-produce ($\gamma\gamma\to e^+e^-$) provided their invariant mass reaches $2m_e$, why a box of photons (blackbody radiation) has a rest mass equal to its energy, and why "massless constituents" does not mean "massless system". The trigger is any system containing photons: do not assume it is massless; compute $M^2 = 2\sum_{a<b}P_a\cdot P_b$, which is generically positive. The only way to get $M = 0$ is for *all* the photons to be collinear and co-directed.

**The centre-of-momentum frame turns the invariant mass into a total energy.** The deepest computational lesson is that $M = E_{\text{cm}}$: the invariant mass is just the total energy in the frame where the system is at rest as a whole. This is why the centre-of-momentum frame is "nearly always the smart frame" — it trivialises the spatial part of the total four-momentum, leaving $P = (E_{\text{cm}}, \mathbf{0})$ and $M = E_{\text{cm}}$. The reusable technique is the two-frame move: recognise the system mass as an invariant, evaluate it in the centre-of-momentum frame (where it is a simple energy sum) *or* directly via the inner-product expansion (where the cross terms are explicit), and equate to whatever frame the data are given in. This is the engine of every [[Ex - Threshold energy for particle production|threshold]] calculation, where the available energy is exactly this invariant mass, and it is the single most labour-saving recognition in relativistic kinematics.
