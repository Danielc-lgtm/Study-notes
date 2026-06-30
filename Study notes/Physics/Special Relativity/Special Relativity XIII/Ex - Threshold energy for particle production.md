---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Inelastic Collisions and Particle Production"
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

1. Derive the general fixed-target threshold: for $\mathcal{P}_1 + \mathcal{P}_2 \to (\text{products of total mass } m_{\text{thres}})$ with $\mathcal{P}_2$ at rest, show the projectile energy must satisfy $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/(2m_2)$.
2. **Antiproton production.** Antiprotons are made by $p + p \to p + p + p + \bar{p}$. With all protons of mass $m_p$, find the threshold energy of the incident proton on a stationary proton target. (The antiproton has the same mass as the proton.)
3. **Pair production on a nucleus.** For $\gamma + \mathcal{N} \to \mathcal{N} + e^+ + e^-$ with a heavy stationary nucleus of mass $M_\mathcal{N} \gg m_e$, find the threshold photon energy and show it is approximately $2m_e c^2$.
4. Show that in a **collider** (centre-of-momentum frame), the threshold for $p + p \to p + p + p + \bar{p}$ requires each beam to have energy only $2m_p$, vastly less than the fixed-target requirement.

Work with $c = 1$ in the derivation; restore $c$ in numerical answers.

**Recall:**

![[Thm - Inelastic Collisions and Particle Production#Statement]]

Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) gives $\sum P_{\text{in}} = \sum P_{\text{out}}$. The invariant mass of the system is $\sqrt{s} = \sqrt{(\sum P_{\text{in}})^2}$, equal to the total energy in the centre-of-momentum frame; at threshold all products are at rest there, so $\sqrt{s} = m_{\text{thres}} = \sum_a m_a'$.

---

# Convergent Strategy

**Problem class.** The flagship *threshold* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|two-frame-invariant]] type: evaluate the invariant $s$ in the centre-of-momentum frame (at threshold, products at rest, $s = m_{\text{thres}}^2$) and in the lab (where the data live), and equate.

**Assumption pattern.** A reaction producing new particles, with a fixed target or a collider. The signpost is "minimum energy" or "threshold" — at threshold all products are at rest in the centre-of-momentum frame, which fixes $s = m_{\text{thres}}^2$.

**Theorem routing.** All parts use the threshold criterion $\sqrt{s} \ge m_{\text{thres}}$ from [[Thm - Inelastic Collisions and Particle Production]], with $s$ evaluated in the lab frame (parts 1–3) via $s = m_1^2 + m_2^2 + 2m_2 E_1$ or in the collider frame (part 4) via $s = (2E)^2$.

**Key decision point.** The crux is the two-frame evaluation of the *same* invariant $s$: at threshold, in the centre-of-momentum frame, $s = m_{\text{thres}}^2$ (products at rest); in the lab, $s = m_1^2 + m_2^2 + 2m_2 E_1$. Equating gives the threshold energy. The non-obvious content is the quadratic ($m_{\text{thres}}^2$) growth in fixed-target versus linear in collider.

---

# Legal Operations Used

1. **Go to the centre-of-momentum frame** (operation 3 from the topic page). At threshold, all products are at rest there, so the total four-momentum is $(m_{\text{thres}}, \mathbf{0})$ and $s = m_{\text{thres}}^2$.

2. **Use a Lorentz invariant to switch frames** (operation 6). The invariant $s$ is evaluated in the centre-of-momentum frame (where it is $m_{\text{thres}}^2$ at threshold) and the lab (where it is $m_1^2 + m_2^2 + 2m_2 E_1$), then equated.

3. **Square a four-momentum to extract an invariant mass** (operation 2). The invariant $s = (\sum P_{\text{in}})^2$ is the squared total four-momentum.

---

# Hints

> [!note]- Hint 1
> The available energy is the invariant $\sqrt{s} = \sqrt{(P_1+P_2)^2}$. At threshold all products are at rest in the centre-of-momentum frame, so $\sqrt{s} = m_{\text{thres}} = \sum m_a'$. Evaluate $s$ in the lab: $s = m_1^2 + m_2^2 + 2m_2 E_1$. Set $s = m_{\text{thres}}^2$ and solve for $E_1$.

> [!note]- Hint 2
> For $p + p \to p + p + p + \bar{p}$, the products are four protons (the antiproton has mass $m_p$), so $m_{\text{thres}} = 4m_p$. With $m_1 = m_2 = m_p$: $E_1 \ge ((4m_p)^2 - m_p^2 - m_p^2)/(2m_p) = (16m_p^2 - 2m_p^2)/(2m_p) = 7m_p$.

> [!note]- Hint 3
> For $\gamma + \mathcal{N}\to\mathcal{N} + e^+ + e^-$, $m_1 = 0$ (photon), $m_2 = M_\mathcal{N}$, $m_{\text{thres}} = M_\mathcal{N} + 2m_e$. Then $E_1 \ge ((M_\mathcal{N}+2m_e)^2 - M_\mathcal{N}^2)/(2M_\mathcal{N}) = (4M_\mathcal{N}m_e + 4m_e^2)/(2M_\mathcal{N}) = 2m_e(1 + m_e/M_\mathcal{N}) \approx 2m_e$.

> [!note]- Hint 4
> In a collider the lab is the centre-of-momentum frame, so $\sqrt{s} = E_1 + E_2 = 2E$ for equal beams. Threshold $\sqrt{s} = 4m_p$ needs $2E = 4m_p$, i.e. $E = 2m_p$ per beam. Compare with the $7m_p$ kinetic energy needed for a fixed target.

---

# Solution

A reaction's threshold is found by evaluating the invariant $s$ in two frames: at threshold, in the centre-of-momentum frame, the products are at rest so $s = m_{\text{thres}}^2$; in the lab, $s = m_1^2 + m_2^2 + 2m_2 E_1$. Part 1 derives the general formula; Part 2 gives the famous antiproton threshold $7m_p$; Part 3 the pair-production threshold $\approx 2m_e$; Part 4 the dramatically lower collider threshold.

**Step 1: The general fixed-target threshold.**

> [!note]- Derivation
> The available energy for the reaction is the invariant mass of the incoming system, $\sqrt{s} = \sqrt{(P_1 + P_2)^2}$, which is conserved (so the same before and after). At **threshold** all products are at rest in the centre-of-momentum frame; there the total four-momentum is $(\sum_a m_a', \mathbf{0}) = (m_{\text{thres}}, \mathbf{0})$, so
> $$s = m_{\text{thres}}^2.$$
> Now evaluate the *same* invariant in the lab, with $\mathcal{P}_2$ at rest ($P_2 = (m_2, \mathbf{0})$) and $\mathcal{P}_1$ of energy $E_1$:
> $$s = (P_1 + P_2)^2 = m_1^2 + m_2^2 + 2P_1\cdot P_2 = m_1^2 + m_2^2 + 2m_2 E_1.$$
> Setting the two equal, $m_1^2 + m_2^2 + 2m_2 E_1 = m_{\text{thres}}^2$, and solving for $E_1$:
> $$\boxed{\ E_1 \ge \frac{m_{\text{thres}}^2 - m_1^2 - m_2^2}{2m_2}\ }.$$
> Note the *quadratic* dependence on $m_{\text{thres}}$: to make heavier products, the required beam energy grows as the square of their total mass.

**Step 2: Antiproton production.**

> [!note]- Derivation
> The reaction $p + p \to p + p + p + \bar{p}$ produces four particles, each of mass $m_p$ (the antiproton $\bar p$ has the same mass as the proton). So $m_{\text{thres}} = 4m_p$. With $m_1 = m_2 = m_p$:
> $$E_1 \ge \frac{(4m_p)^2 - m_p^2 - m_p^2}{2m_p} = \frac{16m_p^2 - 2m_p^2}{2m_p} = \frac{14m_p^2}{2m_p} = 7m_p.$$
> So the incident proton needs total energy $E_1 \ge 7m_p$, i.e. kinetic energy $E_1 - m_p = 6m_p$. Numerically, with $m_p c^2 = 0.938$ GeV:
> $$E_1 \ge 7\times 0.938\ \text{GeV} = 6.57\ \text{GeV}.$$
> This is the threshold the Bevatron at Berkeley was built to exceed (it accelerated protons to $6.2$ GeV kinetic energy, total energy $\approx 7.1$ GeV); the antiproton was discovered there in 1955. Three *new* particles' worth of mass (one $\bar p$ plus the extra $p$ needed for baryon-number conservation, beyond the two incoming) must be supplied, which is why so much energy is needed.

**Step 3: Pair production on a nucleus.**

> [!note]- Derivation
> The reaction $\gamma + \mathcal{N} \to \mathcal{N} + e^+ + e^-$ has projectile a photon ($m_1 = 0$), target a heavy nucleus ($m_2 = M_\mathcal{N}$), and products the nucleus plus a pair, so $m_{\text{thres}} = M_\mathcal{N} + 2m_e$. Then
> $$E_1 \ge \frac{(M_\mathcal{N} + 2m_e)^2 - 0 - M_\mathcal{N}^2}{2M_\mathcal{N}} = \frac{M_\mathcal{N}^2 + 4M_\mathcal{N}m_e + 4m_e^2 - M_\mathcal{N}^2}{2M_\mathcal{N}} = \frac{4M_\mathcal{N}m_e + 4m_e^2}{2M_\mathcal{N}}.$$
> $$E_1 \ge 2m_e\Big(1 + \frac{m_e}{M_\mathcal{N}}\Big) \approx 2m_e c^2 = 1.02\ \text{MeV},$$
> for $M_\mathcal{N}\gg m_e$. So a photon of energy just above $2m_e c^2 = 1.02$ MeV can pair-produce in the field of a nucleus. The nucleus's role is essential: it absorbs the recoil momentum, which is why a single photon in *vacuum* cannot pair-produce (see [[Ex - Whether a particle reaction is kinematically allowed]]) — the heavy nucleus barely moves (its recoil energy $\sim m_e^2/M_\mathcal{N}$ is negligible), so almost all the photon energy goes into the pair.

**Step 4: The collider threshold.**

> [!note]- Derivation
> In a **collider**, two proton beams collide head-on, each of energy $E$, so the lab *is* the centre-of-momentum frame. The available energy is $\sqrt{s} = E_1 + E_2 = 2E$ (the beam energies add directly). Threshold $\sqrt{s} = m_{\text{thres}} = 4m_p$ requires
> $$2E = 4m_p \;\Longrightarrow\; E = 2m_p.$$
> Each beam needs total energy $2m_p$, i.e. kinetic energy $m_p$. Compare:
> - **Fixed target:** $E_1 = 7m_p$ (kinetic energy $6m_p$).
> - **Collider:** $E = 2m_p$ per beam (kinetic energy $m_p$ per beam, $2m_p$ total).
>
> The collider needs roughly a third of the total kinetic energy, and the advantage grows for heavier products: the fixed-target threshold scales as $m_{\text{thres}}^2$, the collider as $m_{\text{thres}}$. This is why antiproton-collider experiments (and all modern high-energy machines) use colliding beams.

> [!note]- Complete formal solution
> The available energy is $\sqrt{s} = \sqrt{(P_1+P_2)^2}$, conserved. At threshold, products at rest in the centre-of-momentum frame, $s = m_{\text{thres}}^2$. Evaluated in the lab with $\mathcal{P}_2$ at rest, $s = m_1^2 + m_2^2 + 2m_2 E_1$, so $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/2m_2$. **(2)** For $p+p\to p+p+p+\bar p$, $m_{\text{thres}} = 4m_p$, $m_1 = m_2 = m_p$: $E_1 \ge (16-2)m_p^2/2m_p = 7m_p \approx 6.57$ GeV. **(3)** For $\gamma+\mathcal{N}\to\mathcal{N}+e^+e^-$, $m_1 = 0$, $m_2 = M_\mathcal{N}$, $m_{\text{thres}} = M_\mathcal{N}+2m_e$: $E_1 \ge 2m_e(1+m_e/M_\mathcal{N}) \approx 2m_e = 1.02$ MeV. **(4)** Collider: $\sqrt{s} = 2E$, threshold $E = 2m_p$ per beam — far less than the $7m_p$ fixed-target requirement, because the fixed-target threshold grows as $m_{\text{thres}}^2$ and the collider as $m_{\text{thres}}$. $\blacksquare$

---

# Key Takeaways

**At threshold the products are at rest in the centre-of-momentum frame — this fixes $s = m_{\text{thres}}^2$.** The single idea that solves every threshold problem is that the minimum-energy configuration has all products at rest in the centre-of-momentum frame, because any relative motion would require energy beyond the rest masses. There the total four-momentum is $(m_{\text{thres}}, \mathbf{0})$, so the invariant $s = m_{\text{thres}}^2$. Evaluating the *same* invariant in the lab (where the data are given) and equating delivers the threshold in one step. The reusable technique is the two-frame move: compute the conserved invariant $s$ in the frame where it is simple (centre-of-momentum at threshold) and in the frame where the kinematics are specified (lab), then set them equal. This is the same machinery as the [[Ex - Mandelstam variables for two-body scattering|Mandelstam]] identity $s = E_{\text{cm}}^2$ and the [[Ex - The invariant mass of a system of particles|invariant mass]] of a system — all are "$s$ is the available energy".

**The fixed-target threshold grows as the square of the product mass — colliders grow only linearly.** The formula $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/2m_2$ has the product mass appearing *squared*, so creating heavier particles requires quadratically more fixed-target beam energy. The reason is that conservation of momentum forbids the products from being at rest in the lab — they must carry the incoming momentum, and that kinetic energy is unavailable for making mass. In a collider, where the lab is the centre-of-momentum frame, no energy is wasted on net motion and the threshold grows only linearly. The reusable diagnostic: the available energy is $\sqrt{s} \approx \sqrt{2m_2 E_1}$ for a fixed target (square root of beam energy) but $\sqrt{s} = 2E$ for a collider (linear) — a gap of order $\sqrt{s}/2m_2$, enormous for heavy products. This is the kinematic reason every modern high-energy machine collides beams.

**A heavy spectator absorbs recoil at almost no energy cost — why pair production needs a nucleus.** Part 3 shows the threshold for photon pair production on a nucleus is just $2m_e c^2 = 1.02$ MeV, barely above the pair rest energy, because the heavy nucleus ($M_\mathcal{N}\gg m_e$) absorbs the recoil momentum while taking up negligible energy (its recoil energy $\sim m_e^2/M_\mathcal{N}$ vanishes as $M_\mathcal{N}\to\infty$). This is the resolution of why a single photon cannot pair-produce in *vacuum* (forbidden, [[Ex - Whether a particle reaction is kinematically allowed]]) but *can* in matter: the nucleus is the third body that makes the books balance, at almost no energy penalty. The reusable trigger: when a reaction is forbidden by momentum conservation, a heavy spectator can rescue it — it carries away the momentum cheaply. This is also why electrons in materials, neutrons in nuclei, and lattice phonons in solids act as momentum reservoirs that enable otherwise-forbidden processes.
