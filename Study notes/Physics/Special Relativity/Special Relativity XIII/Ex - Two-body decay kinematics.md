---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Problem Statement

A particle of rest mass $m_1$, at rest, decays into two particles of rest masses $m_2$ and $m_3$: $\mathcal{P}_1 \to \mathcal{P}_2 + \mathcal{P}_3$.

1. Show the decay is possible only if $m_1 \ge m_2 + m_3$.
2. Find the energies $E_2, E_3$ and Lorentz factors $\gamma_2, \gamma_3$ of the products in the rest frame of $\mathcal{P}_1$, in terms of the three masses; show $\gamma_2 = (m_1^2 + m_2^2 - m_3^2)/(2m_1 m_2)$.
3. **Higgs decay.** The Higgs boson ($m_h c^2 \approx 125$ GeV) decays to two photons, $h\to\gamma\gamma$. Find the photon energies in the Higgs rest frame, and explain why they are emitted back-to-back.
4. If the Higgs is moving with energy $E_h$ and one photon is observed at energy $E_\gamma$, find the angle $\theta$ this photon makes with the Higgs's direction.

Work with $c = 1$ in the derivation.

**Recall:**

![[Def - Four-Momentum and Rest Mass#The Definition]]

Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) gives $P_1 = P_2 + P_3$. A [[Def - The Four-Momentum of a Photon|photon]] has $P_\gamma\cdot P_\gamma = 0$. The energy–momentum relation is $E^2 = \mathbf{p}^2 + m^2$.

---

# Convergent Strategy

**Problem class.** A *decay kinematics* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|conservation-plus-eliminate]] type: conservation of four-momentum in the parent rest frame fixes the product energies entirely from the masses, and one product is eliminated by isolating and squaring.

**Assumption pattern.** A single parent at rest decaying into two products. The signpost is "a particle at rest decays" — work in its rest frame, where $P_1 = (m_1, \mathbf{0})$ and the products go back-to-back with equal and opposite momenta. The unwanted product (when solving for the other's energy) is isolated and squared.

**Theorem routing.** Part 1 uses the energy form of conservation, $m_1 = E_2 + E_3 \ge m_2 + m_3$. Part 2 isolates $P_3 = P_1 - P_2$, squares to $m_3^2$, and solves for $E_2$ ([[Thm - Conservation of Four-Momentum]] + mass-shell). Part 3 specialises to two photons. Part 4 uses the boosted-frame rearrange-and-square move for the photon angle.

**Key decision point.** In part 2 the crux is isolating the *unwanted* product ($P_3$) and squaring to $m_3^2$, leaving a linear equation for $E_2$. In part 4 the crux is that you know nothing about the *second* photon, so isolate *its* four-momentum, $P_\gamma' = P_h - P_\gamma$, and square to $0$ (null) to get the angle of the observed photon.

---

# Legal Operations Used

1. **Write down the total four-momentum and set it equal before and after** (operation 1 from the topic page). Conservation reads $P_1 = P_2 + P_3$ in the parent rest frame.

2. **Go to the rest frame of a chosen massive particle** (operation 4). Working in the parent's rest frame, $P_1 = (m_1, \mathbf{0})$, so $m_1 = E_2 + E_3$ and $\mathbf{p}_2 = -\mathbf{p}_3$.

3. **Square a four-momentum to extract an invariant mass** (operation 2). Isolating one product and squaring to its mass-shell gives the other's energy; in part 4, isolating the unobserved photon and squaring to $0$ gives the angle.

---

# Hints

> [!note]- Hint 1
> In the parent rest frame, conservation gives $m_1 = E_2 + E_3$. Each $E_a \ge m_a$ (energy at least rest energy), so $m_1 = E_2 + E_3 \ge m_2 + m_3$.

> [!note]- Hint 2
> To find $E_2$, isolate the unwanted product: $P_3 = P_1 - P_2$. Square: $m_3^2 = m_1^2 + m_2^2 - 2P_1\cdot P_2$. With $P_1 = (m_1, \mathbf{0})$, $P_1\cdot P_2 = m_1 E_2$. Solve for $E_2$.

> [!note]- Hint 3
> For $h\to\gamma\gamma$, in the Higgs rest frame $m_h = E_\gamma + E_\gamma'$ and $\mathbf{p}_\gamma + \mathbf{p}_\gamma' = 0$. By symmetry (or set $m_2 = m_3 = 0$ in part 2), each photon has energy $E_\gamma = m_h/2$; they go back-to-back because their momenta must cancel.

> [!note]- Hint 4
> If the Higgs moves and one photon is observed, you know nothing about the *second* photon — isolate it: $P_\gamma' = P_h - P_\gamma$, square to $0$ (null). With $P_h\cdot P_\gamma = E_h E_\gamma - |\mathbf{p}_h|E_\gamma\cos\theta$, solve for $\cos\theta$.

---

# Solution

A particle at rest decays into two products whose energies are fixed entirely by the three masses, by conservation of four-momentum in the rest frame. Part 1 reads the threshold off the energy sum; Part 2 isolates and squares one product to get the other's energy; Part 3 specialises to back-to-back photons; Part 4 finds the photon angle in a boosted frame by squaring the unobserved photon.

**Step 1: The decay requires $m_1 \ge m_2 + m_3$.**

> [!note]- Derivation
> Work in the rest frame of $\mathcal{P}_1$, where $P_1 = (m_1, \mathbf{0})$. Conservation of four-momentum $P_1 = P_2 + P_3$ has time component
> $$m_1 = E_2 + E_3.$$
> Each product's energy is at least its rest energy, $E_2 \ge m_2$ and $E_3 \ge m_3$ (since $E = \sqrt{m^2 + \mathbf{p}^2} \ge m$). Hence
> $$m_1 = E_2 + E_3 \ge m_2 + m_3.$$
> A particle can decay only into products whose total rest mass it can supply. Equality $m_1 = m_2 + m_3$ holds only at the boundary, where the products are produced at rest (no kinetic energy) — but then they have zero momentum and cannot separate, so strict inequality is needed for an actual decay.

**Step 2: Product energies and Lorentz factors.**

> [!note]- Derivation
> To find $E_2$, isolate the unwanted product $\mathcal{P}_3$: $P_3 = P_1 - P_2$. Square (Minkowski):
> $$m_3^2 = P_3\cdot P_3 = (P_1 - P_2)\cdot(P_1 - P_2) = m_1^2 - 2P_1\cdot P_2 + m_2^2.$$
> In the parent rest frame $P_1 = (m_1, \mathbf{0})$, so $P_1\cdot P_2 = m_1 E_2$. Substituting:
> $$m_3^2 = m_1^2 + m_2^2 - 2m_1 E_2 \;\Longrightarrow\; \boxed{\ E_2 = \frac{m_1^2 + m_2^2 - m_3^2}{2m_1}\ }.$$
> By symmetry ($2\leftrightarrow 3$), $E_3 = (m_1^2 + m_3^2 - m_2^2)/(2m_1)$, and indeed $E_2 + E_3 = m_1$. The Lorentz factors are $\gamma_a = E_a/m_a$:
> $$\gamma_2 = \frac{E_2}{m_2} = \frac{m_1^2 + m_2^2 - m_3^2}{2m_1 m_2}, \qquad \gamma_3 = \frac{m_1^2 + m_3^2 - m_2^2}{2m_1 m_3}.$$
> The product energies and speeds are *completely determined* by the three masses — a two-body decay from rest is monoenergetic. The common momentum magnitude is $|\mathbf{p}_2| = |\mathbf{p}_3| = \sqrt{E_2^2 - m_2^2}$.

**Step 3: Higgs to two photons.**

> [!note]- Derivation
> For $h\to\gamma\gamma$, set $m_2 = m_3 = 0$ (photons). From part 2, $E_\gamma = (m_h^2 + 0 - 0)/(2m_h) = m_h/2$. So each photon carries **half the Higgs rest energy**,
> $$E_\gamma = E_\gamma' = \frac{m_h}{2} \approx \frac{125\ \text{GeV}}{2} = 62.5\ \text{GeV}.$$
> In the Higgs rest frame the total momentum is zero, $\mathbf{p}_\gamma + \mathbf{p}_\gamma' = \mathbf{0}$, so $\mathbf{p}_\gamma = -\mathbf{p}_\gamma'$: the photons are emitted **back-to-back** (opposite directions). Because $|\mathbf{p}_\gamma| = E_\gamma = m_h/2$ for both, their momenta are equal in magnitude and opposite in direction. The problem is rotationally symmetric (the Higgs has no preferred axis), so the back-to-back pair can point in any direction.

**Step 4: Photon angle from a moving Higgs.**

> [!note]- Derivation
> Now the Higgs moves with energy $E_h$ and momentum $|\mathbf{p}_h| = \sqrt{E_h^2 - m_h^2}$, and one photon is observed with energy $E_\gamma$ at angle $\theta$ to the Higgs's direction. We know nothing about the *second* photon, so isolate it: $P_\gamma' = P_h - P_\gamma$. Square (it is null):
> $$0 = P_\gamma'\cdot P_\gamma' = (P_h - P_\gamma)\cdot(P_h - P_\gamma) = m_h^2 + 0 - 2P_h\cdot P_\gamma.$$
> So $P_h\cdot P_\gamma = m_h^2/2$. Compute the contraction in the lab frame: $P_h = (E_h, \mathbf{p}_h)$, $P_\gamma = (E_\gamma, E_\gamma\mathbf{n})$ with $\mathbf{p}_h\cdot\mathbf{n} = |\mathbf{p}_h|\cos\theta$, so
> $$P_h\cdot P_\gamma = E_h E_\gamma - \mathbf{p}_h\cdot\mathbf{p}_\gamma = E_h E_\gamma - |\mathbf{p}_h|E_\gamma\cos\theta.$$
> Setting this equal to $m_h^2/2$ and solving:
> $$\cos\theta = \frac{E_h E_\gamma - m_h^2/2}{|\mathbf{p}_h|E_\gamma} = \frac{2E_h E_\gamma - m_h^2}{2E_\gamma\sqrt{E_h^2 - m_h^2}}.$$
> This gives the angle of the observed photon directly from the Higgs and photon energies, without any reference to the unobserved photon — the rearrange-and-square move eliminating it.

> [!note]- Complete formal solution
> In the parent rest frame $P_1 = (m_1, \mathbf{0})$, conservation $P_1 = P_2 + P_3$ gives $m_1 = E_2 + E_3 \ge m_2 + m_3$ (each $E_a \ge m_a$), so the decay needs $m_1 \ge m_2 + m_3$. Isolating $P_3 = P_1 - P_2$ and squaring to $m_3^2$ gives $E_2 = (m_1^2+m_2^2-m_3^2)/2m_1$ and $\gamma_2 = E_2/m_2 = (m_1^2+m_2^2-m_3^2)/2m_1 m_2$ (similarly for $3$). For $h\to\gamma\gamma$ ($m_2=m_3=0$), $E_\gamma = m_h/2$, back-to-back since $\mathbf{p}_\gamma + \mathbf{p}_\gamma' = 0$. For a moving Higgs, isolating the unobserved photon $P_\gamma' = P_h - P_\gamma$ and squaring to $0$ gives $P_h\cdot P_\gamma = m_h^2/2$, hence $\cos\theta = (2E_h E_\gamma - m_h^2)/(2E_\gamma\sqrt{E_h^2-m_h^2})$. $\blacksquare$

---

# Key Takeaways

**A two-body decay from rest is monoenergetic — the product energies are fixed by the masses alone.** The striking result of part 2 is that the product energies $E_2 = (m_1^2+m_2^2-m_3^2)/2m_1$ depend *only* on the three rest masses, not on any other parameter. A particle at rest decaying into two has no freedom: the energies, speeds, and momentum magnitudes are completely determined, and the only thing that varies (by rotational symmetry) is the direction of the back-to-back axis. This is the basis of particle identification: a monoenergetic decay product is the signature of a two-body decay from a parent at rest, and measuring the product energy gives the parent mass. The reusable technique is the isolate-and-square move — to find one product's energy, isolate the *other* product, square to its mass-shell, and solve the resulting linear equation. The same move handles any two-body decay and is the decay analogue of the [[Ex - Compton scattering|Compton]] elimination.

**"Particle at rest decays" means work in its rest frame, where the products go back-to-back.** The single most useful recognition for decay problems is to work in the parent's rest frame, where $P_1 = (m_1, \mathbf{0})$, conservation gives $m_1 = \sum E_a$ for the energies and $\sum\mathbf{p}_a = 0$ for the momenta, and a two-body decay is forced back-to-back (equal and opposite momenta). The threshold $m_1 \ge m_2 + m_3$ then reads off immediately from the energy sum. This frame is where decay kinematics is simplest, and transforming to the lab (part 4) is a separate, later step. The trigger: any decay of a particle described as "at rest" or "in its rest frame" — start there, get the product energies from the masses, then boost if needed.

**When you know nothing about a particle, isolate it and square — even in a boosted frame.** Part 4 reuses the chapter's master reflex in a new guise: the second photon from a moving Higgs is completely unknown, so isolate *it* ($P_\gamma' = P_h - P_\gamma$) and square to its mass-shell ($0$, null), eliminating it and leaving an equation for the *observed* photon's angle. This is exactly the [[Ex - Compton scattering|Compton]] technique applied to a decay in a boosted frame. The trigger is "one product is observed, the other is not": isolate the unobserved one, square it away, and read off the observed one's kinematics. The method is frame-independent — it works in the rest frame (parts 1–3) and the lab frame (part 4) alike — because squaring a four-vector is a Lorentz invariant. This is how, at the LHC, the Higgs mass is reconstructed from the invariant mass of observed photon pairs, the di-photon peak at $125$ GeV.
