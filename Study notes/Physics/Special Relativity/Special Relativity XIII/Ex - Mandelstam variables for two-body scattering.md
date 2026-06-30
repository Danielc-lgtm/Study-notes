---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Inelastic Collisions and Particle Production"
tags: [physics, special-relativity]
---

# Problem Statement

For a two-body process $\mathcal{P}_1 + \mathcal{P}_2 \to \mathcal{P}_3 + \mathcal{P}_4$ with [[Def - Four-Momentum and Rest Mass|four-momenta]] $P_1, P_2, P_3, P_4$ and masses $m_1, m_2, m_3, m_4$, define the **Mandelstam variables**
$$s = (P_1 + P_2)^2, \qquad t = (P_1 - P_3)^2, \qquad u = (P_1 - P_4)^2.$$

1. Show $s, t, u$ are Lorentz invariants, and that $s = (P_3+P_4)^2$ (and analogously for $t, u$) using conservation of four-momentum.
2. Prove the sum rule $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.
3. Show that $s$ is the square of the centre-of-mass energy, $s = E_{\text{cm}}^2$, and that $\sqrt{s}$ is the invariant mass of the system.
4. Compute $\sqrt{s}$ for (a) a **collider** of two equal-mass particles $m$ each with energy $E$ (head-on), and (b) a **fixed target** of a projectile of energy $E_1$ on a stationary target $m_2$. Compare the energy needed to reach a given $\sqrt{s}$.

Work with $c = 1$.

**Recall:**

Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) gives $P_1 + P_2 = P_3 + P_4$. The mass-shell is $P_a\cdot P_a = m_a^2$. The invariant mass of a system is $\sqrt{(\sum P)^2}$, equal to the total energy in the centre-of-momentum frame ([[Thm - Inelastic Collisions and Particle Production]]). The Minkowski inner product $A\cdot B = A^0 B^0 - \mathbf{A}\cdot\mathbf{B}$ is a Lorentz scalar.

---

# Convergent Strategy

**Problem class.** A *structural-invariants* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|establish-an-invariant]] type: the Mandelstam variables are squares of four-momentum combinations, hence Lorentz scalars, and the sum rule and centre-of-mass identity follow from expanding squares and using conservation and the mass-shell.

**Assumption pattern.** A $2\to2$ process with four external four-momenta. The signpost is "scattering kinematics in terms of invariants" — the right variables are the Minkowski squares $s, t, u$, not the frame-dependent energies and angles. Conservation $P_1 + P_2 = P_3 + P_4$ relates the in and out forms.

**Theorem routing.** Part 1 uses frame-invariance of squares and conservation ([[Thm - Conservation of Four-Momentum]]). Part 2 expands $s + t + u$ and uses the mass-shell plus conservation to kill the cross terms. Part 3 evaluates $s$ in the centre-of-momentum frame ([[Thm - Inelastic Collisions and Particle Production]]). Part 4 evaluates $s$ in the collider and fixed-target geometries.

**Key decision point.** The crux of part 2 is recognising that the cross terms in $s + t + u$ assemble into $-2P_1\cdot(P_1 + P_2 - P_3 - P_4) = 0$ by conservation, leaving only the mass-shell terms. The crux of part 4 is that $\sqrt{s}$ grows *linearly* with beam energy in a collider but only as the *square root* of beam energy in a fixed target — the kinematic case for colliders.

---

# Legal Operations Used

1. **Use a Lorentz invariant to switch frames** (operation 6 from the topic page). The Mandelstam variables are Lorentz scalars, evaluated in whichever frame is convenient (centre-of-momentum for $s$).

2. **Square a four-momentum to extract an invariant mass** (operation 2). Each Mandelstam variable is a Minkowski square; $s$ is the invariant mass squared of the system.

3. **Go to the centre-of-momentum frame** (operation 3). Part 3 evaluates $s$ in the frame where the total momentum vanishes, giving $s = E_{\text{cm}}^2$.

---

# Hints

> [!note]- Hint 1
> Each Mandelstam variable is the Minkowski square of a four-vector (a sum or difference of four-momenta), hence a Lorentz scalar. For $s = (P_1+P_2)^2$, conservation $P_1+P_2 = P_3+P_4$ gives $s = (P_3+P_4)^2$ immediately.

> [!note]- Hint 2
> Expand $s + t + u = (P_1+P_2)^2 + (P_1-P_3)^2 + (P_1-P_4)^2$. Collect the $P_1\cdot P_1 = m_1^2$ terms (there are three), the other mass-shell terms, and the cross terms; the cross terms involving $P_1$ assemble into $2P_1\cdot(P_2 - P_3 - P_4) = -2P_1\cdot(P_1 - \text{(conserved)})\cdots$ — use conservation to make them cancel.

> [!note]- Hint 3
> In the centre-of-momentum frame $P_1 + P_2 = (E_{\text{cm}}, \mathbf{0})$ (zero total momentum), so $s = (P_1+P_2)^2 = E_{\text{cm}}^2$. Hence $\sqrt{s} = E_{\text{cm}}$ is the total energy there, i.e. the invariant mass of the system.

> [!note]- Hint 4
> Collider: each beam has $P = (E, \pm\mathbf{p})$ with $|\mathbf{p}| = \sqrt{E^2-m^2}$, total momentum zero, so $s = (2E)^2 = 4E^2$, $\sqrt{s} = 2E$. Fixed target: $P_2 = (m_2, \mathbf{0})$, so $s = m_1^2 + m_2^2 + 2m_2 E_1 \approx 2m_2 E_1$ for $E_1 \gg m_2$, giving $\sqrt{s} \approx \sqrt{2m_2 E_1}$.

---

# Solution

The Mandelstam variables $s, t, u$ are Lorentz-invariant squares of four-momentum combinations that fully capture two-body kinematics. Part 1 establishes invariance and the in/out equality; Part 2 proves the sum rule via conservation; Part 3 identifies $s$ as the centre-of-mass energy squared; Part 4 contrasts collider and fixed-target geometries. The headline is that $\sqrt{s}$ grows linearly with collider beam energy but only as the square root of fixed-target beam energy.

**Step 1: Invariance and the in/out equality.**

> [!note]- Derivation
> Each Mandelstam variable is the Minkowski square of a four-vector: $s = (P_1+P_2)\cdot(P_1+P_2)$, $t = (P_1-P_3)\cdot(P_1-P_3)$, $u = (P_1-P_4)\cdot(P_1-P_4)$. A Minkowski square is a Lorentz scalar, so $s, t, u$ are Lorentz invariants — the same number in every frame.
>
> By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], $P_1 + P_2 = P_3 + P_4$, so
> $$s = (P_1+P_2)^2 = (P_3+P_4)^2,$$
> and similarly $P_1 - P_3 = P_4 - P_2$ gives $t = (P_1-P_3)^2 = (P_4-P_2)^2 = (P_2-P_4)^2$, and $P_1 - P_4 = P_3 - P_2$ gives $u = (P_1-P_4)^2 = (P_2-P_3)^2$. Each variable has an "incoming" and an "outgoing" form, equal by conservation.

**Step 2: The sum rule.**

> [!note]- Derivation
> Expand each variable using $P_a\cdot P_a = m_a^2$:
> $$s = (P_1+P_2)^2 = m_1^2 + m_2^2 + 2P_1\cdot P_2,$$
> $$t = (P_1-P_3)^2 = m_1^2 + m_3^2 - 2P_1\cdot P_3,$$
> $$u = (P_1-P_4)^2 = m_1^2 + m_4^2 - 2P_1\cdot P_4.$$
> Add them:
> $$s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2P_1\cdot(P_2 - P_3 - P_4).$$
> Now use conservation $P_1 + P_2 = P_3 + P_4$, i.e. $P_2 - P_3 - P_4 = -P_1$. Substituting:
> $$s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2P_1\cdot(-P_1) = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 - 2m_1^2,$$
> using $P_1\cdot P_1 = m_1^2$. The $m_1^2$ terms collapse: $3m_1^2 - 2m_1^2 = m_1^2$, giving
> $$\boxed{\ s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2\ }.$$
> So the three Mandelstam variables are not independent: their sum is fixed by the masses, and two of them determine the kinematics completely.

**Step 3: $s$ is the centre-of-mass energy squared.**

> [!note]- Derivation
> Evaluate $s = (P_1 + P_2)^2$ in the **centre-of-momentum frame**, where the total spatial momentum vanishes, $\mathbf{p}_1 + \mathbf{p}_2 = \mathbf{0}$. There $P_1 + P_2 = (E_{\text{cm}}, \mathbf{0})$ with $E_{\text{cm}} = E_1^* + E_2^*$ the total energy, so
> $$s = (P_1+P_2)^2 = E_{\text{cm}}^2 - |\mathbf{0}|^2 = E_{\text{cm}}^2.$$
> Hence $\sqrt{s} = E_{\text{cm}}$ is the total energy in the centre-of-momentum frame, which is exactly the **invariant mass** of the colliding system, $\sqrt{s} = M = \sqrt{(P_1+P_2)^2}$. This is the single most important number characterising a collision: it is the energy *available* for the reaction, and the maximum mass of particles that can be produced. The "$\sqrt{s} = 13$ TeV" of the LHC is this quantity.

**Step 4: Collider versus fixed target.**

> [!note]- Derivation
> **(a) Collider.** Two equal-mass particles, each of energy $E$ and momentum magnitude $|\mathbf{p}| = \sqrt{E^2-m^2}$, collide head-on: $P_1 = (E, \mathbf{p})$, $P_2 = (E, -\mathbf{p})$. The total momentum is zero (this *is* the centre-of-momentum frame), so
> $$s = (P_1+P_2)^2 = (2E)^2 - \mathbf{0} = 4E^2 \;\Longrightarrow\; \sqrt{s} = 2E.$$
> The available energy grows **linearly** with the beam energy.
>
> **(b) Fixed target.** Projectile $P_1 = (E_1, \mathbf{p}_1)$ on a stationary target $P_2 = (m_2, \mathbf{0})$:
> $$s = (P_1 + P_2)^2 = m_1^2 + m_2^2 + 2P_1\cdot P_2 = m_1^2 + m_2^2 + 2m_2 E_1.$$
> For $E_1 \gg m_1, m_2$ (ultra-relativistic projectile), $s \approx 2m_2 E_1$, so
> $$\sqrt{s} \approx \sqrt{2m_2 E_1}.$$
> The available energy grows only as the **square root** of the beam energy.
>
> **Comparison.** To reach a given $\sqrt{s}$, the collider needs $E = \sqrt{s}/2$ (linear), but the fixed target needs $E_1 \approx s/(2m_2) = (\sqrt{s})^2/(2m_2)$ (quadratic). For $\sqrt{s} = 14$ TeV with proton beams ($m_2 \approx 0.94$ GeV): the collider needs $E = 7$ TeV per beam; the fixed target would need $E_1 \approx (14\ \text{TeV})^2/(2\times 0.94\ \text{GeV}) \approx 10^5$ TeV. The collider is more efficient by a factor $\sim\sqrt{s}/2m_2 \sim 7000$ — which is why no fixed-target experiment can reach LHC energies.

> [!note]- Complete formal solution
> Each Mandelstam variable is a Minkowski square, hence Lorentz invariant; conservation $P_1+P_2 = P_3+P_4$ gives $s = (P_3+P_4)^2$ etc. Expanding $s+t+u$ with $P_a\cdot P_a = m_a^2$ and using $P_2-P_3-P_4 = -P_1$ collapses the cross terms, giving $s+t+u = m_1^2+m_2^2+m_3^2+m_4^2$. In the centre-of-momentum frame $P_1+P_2 = (E_{\text{cm}},\mathbf{0})$, so $s = E_{\text{cm}}^2$ and $\sqrt{s}$ is the invariant mass. For a collider $s = 4E^2$, $\sqrt{s} = 2E$ (linear); for a fixed target $s = m_1^2+m_2^2+2m_2 E_1 \approx 2m_2 E_1$, $\sqrt{s} \approx \sqrt{2m_2 E_1}$ (square root). To reach $\sqrt{s}$, the collider needs $E = \sqrt{s}/2$ but the fixed target needs $E_1 \approx s/2m_2$, quadratically more. $\blacksquare$

---

# Key Takeaways

**The Mandelstam variables are the natural language of scattering because they are invariant.** Two-body kinematics involves many frame-dependent quantities — energies, angles, momenta — but the physics is captured by just three Lorentz scalars $s, t, u$, the Minkowski squares of four-momentum combinations. Because they are invariant, they are the same to every observer, so a scattering amplitude can be written as a function $\mathcal{M}(s,t,u)$ that is manifestly frame-independent. The sum rule $s+t+u = \sum m_i^2$ means only two are independent, and the deep payoff is **crossing symmetry**: the same analytic function $\mathcal{M}(s,t,u)$, continued into different regions of the $(s,t,u)$ plane, describes several physical processes (an incoming particle crossed to an outgoing antiparticle), so computing one channel gives the others for free. The reusable lesson: when scattering kinematics gets tangled in frame-dependent variables, switch to $s, t, u$ — the invariant squares — and the structure simplifies. This is the entry point to all of scattering theory.

**$\sqrt{s}$ is the energy available for the reaction, and it equals the lab energy only when momenta cancel.** The variable $s = (P_1+P_2)^2 = E_{\text{cm}}^2$ is the single most important number in a collision: the invariant mass of the system, the total energy in the centre-of-momentum frame, and the maximum mass of particles that can be produced. In a collider, where the beams meet head-on so the lab *is* the centre-of-momentum frame, $\sqrt{s}$ is just the sum of beam energies — no energy is wasted on net motion. In a fixed-target experiment, the un-cancelled momentum carries away energy that cannot be used, so $\sqrt{s} \approx \sqrt{2m_2 E_1}$ is far smaller than the beam energy. The reusable diagnostic: to find the available energy of any collision, compute $\sqrt{s} = \sqrt{(\sum P_{\text{in}})^2}$ — the invariant mass of the incoming system — and compare it to the threshold $\sum m_{\text{products}}$ for whatever you want to make.

**Colliders beat fixed targets by a square root — the kinematic basis of accelerator design.** The contrast in part 4 is the reason every high-energy machine is a collider. The available energy $\sqrt{s}$ grows *linearly* with beam energy in a collider ($\sqrt{s} = 2E$) but only as the *square root* of beam energy in a fixed target ($\sqrt{s} \approx \sqrt{2m_2 E_1}$). To reach a given $\sqrt{s}$, the fixed target needs *quadratically* more beam energy — to match the LHC's $14$ TeV would require a single proton at $\sim 10^5$ TeV, physically impossible. This one-line kinematic comparison, derived purely from $s = (P_1+P_2)^2$ evaluated in two geometries, justified the multi-billion-dollar decision to build counter-rotating colliding beams. The trigger: any "how much beam energy to produce particle X?" question — compute $\sqrt{s}$ in both geometries and the collider's advantage (a factor $\sim\sqrt{s}/2m_2$) is immediate. The same machinery sets the [[Ex - Threshold energy for particle production|production threshold]].
