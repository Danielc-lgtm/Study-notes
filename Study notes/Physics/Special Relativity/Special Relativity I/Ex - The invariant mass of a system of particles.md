---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Four-Vector"
  - "Thm - Invariance of the Spacetime Interval"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$. In relativistic kinematics a particle of rest mass $m$ moving with velocity $\mathbf{v}$ carries a [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = (E, \mathbf{p})$, a future-pointing [[Def - Four-Vector|four-vector]] with energy $E = \gamma m$, momentum $\mathbf{p} = \gamma m\mathbf{v}$, and invariant norm $P\cdot P = E^2 - |\mathbf{p}|^2 = m^2$.

A system consists of several particles with four-momenta $P_1, P_2, \dots, P_n$. Its **total four-momentum** is $P = \sum_i P_i$, and its **invariant mass** $M$ is defined by $M^2 = P\cdot P$.

1. Show that $M$ is the same in every inertial frame — it is a genuine invariant.
2. Show that $M$ equals the total energy of the system measured *in the frame where the total momentum vanishes* (the centre-of-momentum frame).
3. Prove that $M \ge \sum_i m_i$, with equality if and only if all the particles are mutually at rest. Interpret the excess.
4. **Application: pair production.** Two photons, each of energy $E$, collide head-on. Find the invariant mass of the two-photon system, and the threshold $E$ at which the collision can create an electron–positron pair (each of rest mass $m_e$).

**Recall:**

The exercise rests on four-momenta being four-vectors and on the invariance of their inner products.

![[Def - Four-Vector#The Definition]]

A four-momentum is a four-vector, so $P\cdot P$ and $P_i\cdot P_j$ are [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]]. A massive particle's four-momentum is future-pointing [[Def - Classification of Four-Vectors|timelike]] ($P\cdot P = m^2 > 0$); a photon's is future-pointing null ($P\cdot P = 0$).

---

# Convergent Strategy

**Problem class.** An *establish-an-invariant* problem. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] says: recognise the quantity as a four-vector inner product, then evaluate it in the most convenient frame.

**Assumption pattern.** Several four-momenta are given; a frame-independent quantity (the invariant mass) is sought. The signpost: "invariant mass" *names* itself as an invariant — it must be a four-vector norm.

**Theorem routing.** Part 1: $P = \sum P_i$ is a sum of four-vectors, hence a four-vector, so $P\cdot P$ is invariant by [[Thm - Invariance of the Spacetime Interval|the invariance theorem]]. Part 2: evaluate $P\cdot P$ in the centre-of-momentum frame, where $\mathbf{P} = 0$ and $P\cdot P = E_{\text{cm}}^2$. Part 3: apply the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] to the future-pointing timelike $P_i$. Part 4: compute $P\cdot P$ for two photons and set $M \ge 2m_e$.

**Key decision point.** The crux is part 2's frame choice: although $P\cdot P$ can be computed in any frame, choosing the centre-of-momentum frame collapses $\mathbf{P}$ to zero, leaving $P\cdot P = E_{\text{cm}}^2$ — so the invariant mass is literally the rest energy of the whole system. The whole technique is "evaluate the invariant where it is easiest".

---

# Legal Operations Used

1. **Compute an invariant in the most convenient frame** — the centre-of-momentum frame, where the total momentum vanishes.

2. **Recognise a quantity as a four-vector inner product** — $M^2 = P\cdot P$ with $P$ a sum of four-vectors.

3. **Classify a four-vector** — each $P_i$ is future-pointing timelike (massive) or null (photon).

4. **Apply the reversed triangle inequality** to bound $M$ below by $\sum m_i$.

---

# Hints

> [!note]- Hint 1
> Each $P_i$ is a four-vector, so the sum $P = \sum_i P_i$ is a four-vector (four-vectors form a vector space). The inner product $P\cdot P$ of a four-vector with itself is Lorentz invariant. Done.

> [!note]- Hint 2
> The centre-of-momentum (CM) frame is the frame where the total spatial momentum $\mathbf{P} = \sum_i\mathbf{p}_i$ vanishes. In that frame $P = (E_{\text{cm}}, \mathbf{0})$, so $P\cdot P = E_{\text{cm}}^2$. Since $P\cdot P = M^2$ and is invariant, $M = E_{\text{cm}}$: the invariant mass is the total energy in the CM frame.

> [!note]- Hint 3
> The four-momenta $P_i$ of massive particles are future-pointing timelike, with $\|P_i\| = \sqrt{P_i\cdot P_i} = m_i$. The reversed triangle inequality gives $\|\sum P_i\| \ge \sum\|P_i\|$, i.e. $M \ge \sum m_i$. Equality requires all $P_i$ parallel — all particles with the same four-velocity, i.e. mutually at rest.

> [!note]- Hint 4
> Two photons of energy $E$ colliding head-on: photon 1 has $P_1 = (E, E, 0, 0)$, photon 2 has $P_2 = (E, -E, 0, 0)$ (opposite momenta). Compute $P\cdot P$ for $P = P_1 + P_2$. For pair production the invariant mass must reach $2m_e$ (the minimum invariant mass of an electron–positron pair, which occurs when they are at relative rest).

---

# Solution

The invariant mass of a system is the Minkowski norm of its total four-momentum — and like every four-vector norm, it is the same in all frames, equals the rest energy in the centre-of-momentum frame, and (by the reversed triangle inequality) exceeds the sum of the parts' rest masses.

**Step 1: $M$ is a Lorentz invariant.**

> [!note]- Derivation
> Each particle's four-momentum $P_i$ is a [[Def - Four-Vector|four-vector]] — it transforms between frames by $P_i^\mu = \Lambda^\mu{}_\nu P_i'^\nu$. Four-vectors form a vector space, closed under addition, so the **total four-momentum**
> $$P = \sum_{i=1}^n P_i$$
> is itself a four-vector. By [[Thm - Invariance of the Spacetime Interval|the invariance theorem]] (in its four-vector form), the inner product of any four-vector with itself is Lorentz invariant. Hence
> $$M^2 = P\cdot P = \eta_{\mu\nu}P^\mu P^\nu$$
> takes the same value in every inertial frame. **The invariant mass $M$ is a genuine invariant** — every observer, whatever their motion, computes the same $M$ for the system, even though they disagree on each particle's energy and momentum. (Total four-momentum is also *conserved* in interactions — a separate fact, from **Special Relativity II** — so $M$ is both frame-independent and, for an isolated system, time-independent.)

**Step 2: $M$ is the total energy in the centre-of-momentum frame.**

> [!note]- Derivation
> Write $P = (E_{\text{tot}}, \mathbf{P})$ where $E_{\text{tot}} = \sum_i E_i$ and $\mathbf{P} = \sum_i\mathbf{p}_i$. In a general frame,
> $$M^2 = P\cdot P = E_{\text{tot}}^2 - |\mathbf{P}|^2.$$
> Because $P$ is future-pointing timelike (a sum of future-pointing timelike/null vectors — see Step 3), there is a frame in which its spatial part vanishes: the **centre-of-momentum frame**, defined by $\mathbf{P} = \sum_i\mathbf{p}_i = \mathbf{0}$. In that frame $P = (E_{\text{cm}}, \mathbf{0})$ and
> $$M^2 = E_{\text{cm}}^2 - 0 = E_{\text{cm}}^2 \;\Longrightarrow\; M = E_{\text{cm}}.$$
> **The invariant mass equals the total energy of the system in its centre-of-momentum frame** — its "rest energy". This is the system-level analogue of $E = m$ for a single particle at rest. The technique is the universal one: $P\cdot P$ may be computed in *any* frame, so compute it where it is easiest — the CM frame, where the messy momentum term drops out.

**Step 3: $M \ge \sum_i m_i$.**

> [!note]- Derivation
> Each massive particle's four-momentum $P_i$ is **future-pointing timelike**: $P_i\cdot P_i = m_i^2 > 0$ and $E_i = \gamma_i m_i > 0$. Its Minkowski norm is $\|P_i\| = \sqrt{P_i\cdot P_i} = m_i$.
>
> The [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] for future-pointing timelike four-vectors gives, applied repeatedly to the sum,
> $$M = \|P\| = \Big\|\sum_i P_i\Big\| \ \ge\ \sum_i \|P_i\| = \sum_i m_i.$$
> So **the invariant mass of a system is at least the sum of the rest masses of its constituents.** By the equality clause of the reversed triangle inequality, equality holds iff all the $P_i$ are parallel — iff every particle has the same four-velocity, i.e. all particles are **mutually at rest**.
>
> *Interpretation.* The excess $M - \sum_i m_i \ge 0$ is the kinetic energy of relative motion, locked into the system. A box of hot gas weighs more than the same box cold, because the invariant mass includes the kinetic energy of the molecules' relative motion. Mass, in relativity, is *not additive*: a system is heavier than the sum of its parts by exactly the internal kinetic (and binding) energy. The invariant mass is the total rest energy, and rest energy counts everything that cannot be transformed away by a single boost.

**Step 4: Two-photon collision and the pair-production threshold.**

> [!note]- Derivation
> Two photons of energy $E$ collide head-on. A photon's four-momentum is null with energy equal to the magnitude of its momentum; taking them along the $x$-axis with opposite momenta,
> $$P_1 = (E, E, 0, 0), \qquad P_2 = (E, -E, 0, 0).$$
> (Check: $P_i\cdot P_i = E^2 - E^2 = 0$ — null, as a photon must be.) The total four-momentum is
> $$P = P_1 + P_2 = (2E, 0, 0, 0).$$
> The total momentum already vanishes — this *is* the centre-of-momentum frame. The invariant mass:
> $$M^2 = P\cdot P = (2E)^2 - 0 = 4E^2 \;\Longrightarrow\; M = 2E.$$
> So two head-on photons of energy $E$ form a system of invariant mass $2E$ — even though each photon individually has zero mass. Two massless objects make a massive system: the mass is the energy of their relative motion, which here is all there is.
>
> *Pair-production threshold.* The collision can create an electron–positron pair only if the available invariant mass $M$ is at least the minimum invariant mass of such a pair. By Step 3, an electron–positron system has invariant mass $\ge m_e + m_e = 2m_e$, the minimum attained when the pair is created mutually at rest. Conservation of four-momentum forces the produced pair to have the *same* total four-momentum, hence the same invariant mass $M = 2E$, as the photons. The reaction $\gamma\gamma \to e^+e^-$ is therefore possible only if
> $$M = 2E \ \ge\ 2m_e \;\Longrightarrow\; E \ \ge\ m_e.$$
> Each photon must carry at least the electron rest energy $m_e$ (with $c$: $m_ec^2 \approx 0.511\,\mathrm{MeV}$). Below threshold there is simply not enough invariant mass to make the pair, no matter how the photons are aimed; at threshold the pair is produced at rest in the CM frame. This is the kinematic basis of pair production, and the invariant-mass calculation is the whole of it.

> [!note]- Complete formal solution
> The total four-momentum $P = \sum_i P_i$ is a four-vector (sum of four-vectors), so $M^2 = P\cdot P$ is Lorentz invariant. Writing $P = (E_{\text{tot}},\mathbf{P})$, in the centre-of-momentum frame $\mathbf{P} = 0$, so $M^2 = E_{\text{cm}}^2$ and $M = E_{\text{cm}}$. Each massive $P_i$ is future-pointing timelike with $\|P_i\| = m_i$; the reversed triangle inequality gives $M = \|\sum P_i\| \ge \sum\|P_i\| = \sum m_i$, with equality iff all particles are mutually at rest, the excess being internal kinetic energy. For two head-on photons of energy $E$, $P_1 = (E,E,0,0)$, $P_2 = (E,-E,0,0)$, $P = (2E,0,0,0)$, so $M = 2E$; pair production $\gamma\gamma \to e^+e^-$ requires $M \ge 2m_e$, hence $E \ge m_e$. $\blacksquare$

---

# Key Takeaways

**To compute an invariant, recognise it as a four-vector inner product and evaluate it in the easiest frame.** The invariant mass looked like it might require tracking every particle's energy and momentum through every frame. It does not. The moment one recognises $M^2 = P\cdot P$ as the Minkowski norm of a four-vector, [[Thm - Invariance of the Spacetime Interval|invariance]] guarantees the answer is frame-independent, so it may be computed wherever the arithmetic is simplest — and the centre-of-momentum frame, where $\mathbf{P} = 0$, is almost always that frame. This is the single most powerful labour-saving move in relativistic kinematics, and it generalises far beyond mass: any quantity that *should* be observer-independent is a contraction of four-vectors, hence an invariant, hence computable in a convenient frame. The trigger is the word "invariant" (or "rest", or "centre-of-momentum") in the problem — it is announcing that a four-vector norm is waiting to be evaluated.

**Mass is not additive: a system weighs more than its parts by the internal kinetic and binding energy.** The reversed triangle inequality, $M \ge \sum m_i$, says the invariant mass of a composite strictly exceeds the sum of constituent rest masses whenever the parts are in relative motion. A hot gas weighs more than a cold one; a stretched spring weighs more than a relaxed one; a bound nucleus weighs *less* than its free constituents (negative binding energy) — every form of internal energy contributes to the invariant mass. The deepest instance is Step 4: two massless photons combine into a system of nonzero mass $2E$. Mass, properly understood, is just the rest energy — the total energy in the centre-of-momentum frame — and rest energy counts everything that cannot be boosted away. The reusable insight: never assume mass adds; compute $\|\sum P_i\|$, and the difference from $\sum m_i$ is precisely the energy of relative motion stored in the system.

**Thresholds for particle reactions are invariant-mass inequalities.** Whether a collision can produce a given set of particles is decided by one comparison: the invariant mass of the incoming system must be at least the minimum invariant mass of the outgoing particles, which is the sum of their rest masses (attained when the products are mutually at rest). Conservation of four-momentum forces the in and out states to share the same invariant mass, so the threshold is $M_{\text{in}} \ge \sum_{\text{out}} m_j$. The two-photon calculation, $2E \ge 2m_e$, is the prototype: a clean, frame-independent inequality, derived entirely from "compute the invariant mass and apply the reversed triangle inequality". The same logic fixes the threshold of every reaction in particle physics — proton–antiproton production, the discovery energies of new particles, the design energy of a collider. The general pattern: a reaction is kinematically allowed exactly when the initial invariant mass clears the sum of the final rest masses, and that is one four-vector-norm computation.
