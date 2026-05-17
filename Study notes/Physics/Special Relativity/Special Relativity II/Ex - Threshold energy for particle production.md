---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Problem Statement

Two particles, each of rest mass $m$, collide and produce — in addition to the original two — a new particle of rest mass $M$:
$$m + m \;\longrightarrow\; m + m + M.$$

**(a)** Working in the **centre-of-momentum frame**, where the two incoming particles have equal and opposite momenta, find the minimum (threshold) speed $v$ of each incoming particle for the reaction to be possible. Express the answer through the Lorentz factor $\gamma_v$.

**(b)** Now suppose the experiment is done in the **lab frame**, where one of the incoming particles is at rest and the other moves with speed $u$. Find the threshold value of $\gamma_u$, and hence the minimum kinetic energy of the moving particle.

**(c)** Compare the two thresholds in the regime $M\gg m$. Why do particle accelerators collide two beams rather than fire one beam at a fixed target?

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - Four-Momentum and Rest Mass#The Mass-Shell Relation]]

The total four-momentum of a system, squared, is a Lorentz invariant: $(\sum P)\cdot(\sum P)$ is the same in every frame and equals $M_{\text{sys}}^2c^2$, the invariant mass squared of the system. For two future-pointing timelike four-momenta, $P_1\cdot P_2 \ge m_1m_2c^2$.

---

# Convergent Strategy

**Problem class.** This is a *threshold* problem: find the minimum energy for a reaction. The topic strategy is fixed — evaluate the invariant $(\sum P)^2$ in two frames and use that at threshold the products are all at rest in the centre-of-momentum frame.

**Assumption pattern.** "Threshold" is the operative word: it means there is *just enough* energy, so the products carry no spare kinetic energy. In the centre-of-momentum frame, where the total spatial momentum is zero, "no spare kinetic energy" means **all products are at rest**.

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] gives $P_1 + P_2 = P_3 + P_4 + P_5$. Square both sides: the invariant $(P_1+P_2)^2$ is the same in every frame, so compute it in the lab frame (where the kinematics are given) and set it equal to $(P_3+P_4+P_5)^2$ computed in the centre-of-momentum frame (where, at threshold, the products are at rest, making the square trivially $(2m+M)^2c^2$).

**Key decision point.** Two insights. First, *threshold ⟺ products at rest in the centre-of-momentum frame* — this is what pins down "minimum". Second, the invariant $(\sum P)^2$ is the bridge between frames: evaluate it where each side is easy and equate. The lab-frame answer's *quadratic* dependence on $M$ is the punchline.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — conservation of four-momentum, $P_1 + P_2 = \sum P_{\text{out}}$.
2. **Square a four-momentum to extract an invariant mass** — squaring $\sum P$ turns it into the invariant mass squared of the system.
3. **Go to the centre-of-momentum frame** — where, at threshold, the products are at rest and $(\sum P_{\text{out}})^2 = (2m+M)^2c^2$.
4. **Go to the rest frame of a chosen particle** — the lab frame, where one incoming particle is at rest.
5. **Use a Lorentz invariant to switch frames** — $(\sum P)^2$ is the same in both frames.

---

# Hints

> [!note]- Hint 1
> "Threshold" means the minimum energy. Where does all the energy go at the minimum? There is nothing to spare for kinetic energy of the products. In which frame does "no kinetic energy" mean "all products at rest"? (Not the lab frame — momentum must be conserved there.)

> [!note]- Hint 2
> At threshold, in the centre-of-momentum frame, the three product particles are all at rest. Their total four-momentum is then $(\,(2m+M)c,\ \mathbf{0})$, and its square is $(2m+M)^2c^2$.

> [!note]- Hint 3
> The quantity $(P_1 + P_2)\cdot(P_1 + P_2)$ is a Lorentz invariant — the same number in every frame. Compute it in the centre-of-momentum frame and in the lab frame, and set the two equal.

> [!note]- Hint 4
> In the lab frame, $P_1 = (m\gamma_u c, m\gamma_u\mathbf{u})$ and $P_2 = (mc,\mathbf{0})$. Then $(P_1+P_2)^2 = P_1^2 + P_2^2 + 2P_1\cdot P_2 = m^2c^2 + m^2c^2 + 2m^2\gamma_u c^2$. Set equal to $(2m+M)^2c^2$ and solve for $\gamma_u$.

---

# Solution

The strategy is to evaluate the invariant $(\sum P)^2$ in two frames. In the centre-of-momentum frame, at threshold, the products are at rest, so $(\sum P)^2 = (2m+M)^2c^2$ trivially. In the lab frame the same invariant is a known function of the beam energy. Equating the two delivers both thresholds; the lab-frame one turns out to scale as $M^2$, which is why accelerators collide beams.

**Step 1: Threshold in the centre-of-momentum frame (part a).**

At threshold the three products are at rest in the centre-of-momentum frame. Conservation of energy then gives $2m\gamma_v c^2 = (2m + M)c^2$, so $\gamma_v = 1 + M/2m$.

> [!note]- Derivation
> In the centre-of-momentum frame the two incoming particles have equal and opposite three-momenta, each moving at speed $v$, so their four-momenta are $P_1 = (m\gamma_v c, +m\gamma_v\mathbf{v})$ and $P_2 = (m\gamma_v c, -m\gamma_v\mathbf{v})$. The total incoming four-momentum is
> $$P_1 + P_2 = (2m\gamma_v c,\ \mathbf{0}).$$
> By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], the total outgoing four-momentum equals this, so the products also have zero total three-momentum — consistent with being in the centre-of-momentum frame.
>
> Now "threshold" — the minimum incoming energy. The total energy is fixed by the incoming particles; whatever is not spent on the rest energies $2mc^2 + Mc^2$ of the products goes into their kinetic energy. The minimum incoming energy is the case with *no* kinetic energy left over, i.e. **all three products at rest** in this frame. (They can all be simultaneously at rest precisely because the total three-momentum is zero here — this is why the centre-of-momentum frame is the right place to impose the threshold condition.) Then the outgoing four-momentum is $((2m+M)c,\mathbf{0})$, and conservation of the time component gives
> $$2m\gamma_v c^2 = (2m + M)c^2 \;\Longrightarrow\; \boxed{\;\gamma_v = 1 + \frac{M}{2m}\;}$$
> The threshold kinetic energy per incoming particle is $T_v = (\gamma_v - 1)mc^2 = \tfrac12 Mc^2$: the two particles each contribute half the new particle's rest energy, and the new particle is born at rest.

**Step 2: The invariant $(P_1+P_2)^2$.**

The quantity $(P_1+P_2)\cdot(P_1+P_2)$ is the same in every frame. At threshold it equals $(2m+M)^2c^2$.

> [!note]- Derivation
> The Minkowski square of the total four-momentum is a Lorentz scalar, so it has the same value in the centre-of-momentum frame and in the lab frame. Compute it in the centre-of-momentum frame at threshold, where the *outgoing* four-momentum is $((2m+M)c,\mathbf{0})$:
> $$(P_1 + P_2)^2 = (P_3+P_4+P_5)^2 = \big((2m+M)c\big)^2 - \mathbf{0}^2 = (2m+M)^2c^2.$$
> This is the invariant mass squared of the whole system at threshold, and by invariance it is the value of $(P_1+P_2)^2$ in *any* frame, including the lab.

**Step 3: Threshold in the lab frame (part b).**

Equating the invariant to its lab-frame expression gives $\gamma_u = 1 + \dfrac{2M}{m} + \dfrac{M^2}{2m^2}$.

> [!note]- Derivation
> In the lab frame, one incoming particle is at rest and the other moves at speed $u$:
> $$P_1 = (m\gamma_u c,\ m\gamma_u\mathbf{u}), \qquad P_2 = (mc,\ \mathbf{0}).$$
> Compute the invariant $(P_1+P_2)^2$ directly:
> $$(P_1+P_2)^2 = P_1\cdot P_1 + P_2\cdot P_2 + 2P_1\cdot P_2.$$
> Each particle is on its mass shell: $P_1\cdot P_1 = P_2\cdot P_2 = m^2c^2$ (the [[Def - Four-Momentum and Rest Mass|mass-shell relation]]). The cross term is
> $$P_1\cdot P_2 = (m\gamma_u c)(mc) - (m\gamma_u\mathbf{u})\cdot\mathbf{0} = m^2\gamma_u c^2.$$
> Hence
> $$(P_1+P_2)^2 = m^2c^2 + m^2c^2 + 2m^2\gamma_u c^2 = 2m^2c^2(1 + \gamma_u).$$
> Setting this equal to the threshold invariant $(2m+M)^2c^2$ from Step 2:
> $$2m^2(1+\gamma_u) = (2m+M)^2 = 4m^2 + 4mM + M^2.$$
> Solving for $\gamma_u$:
> $$1 + \gamma_u = \frac{4m^2 + 4mM + M^2}{2m^2} \;\Longrightarrow\; \boxed{\;\gamma_u = 1 + \frac{2M}{m} + \frac{M^2}{2m^2}\;}$$
> The minimum kinetic energy of the beam particle is
> $$T_u = (\gamma_u - 1)mc^2 = \Big(\frac{2M}{m} + \frac{M^2}{2m^2}\Big)mc^2 = 2Mc^2 + \frac{M^2c^2}{2m}.$$

**Step 4: Comparison and the case $M\gg m$ (part c).**

> [!note]- Derivation
> Compare the threshold kinetic energies:
> $$T_v^{\text{(CM, per particle)}} = \tfrac12 Mc^2, \qquad T_v^{\text{(CM, total)}} = Mc^2, \qquad T_u^{\text{(lab)}} = 2Mc^2 + \frac{M^2c^2}{2m}.$$
> In the centre-of-momentum frame the total kinetic energy needed is just $Mc^2$ — exactly the rest energy of the new particle, with nothing wasted. In the lab frame the cost is far higher, and for a *heavy* new particle, $M\gg m$, the dominant term is
> $$T_u^{\text{(lab)}} \approx \frac{M^2c^2}{2m},$$
> which scales **quadratically** with $M$, against the **linear** scaling $Mc^2$ in the centre-of-momentum frame.
>
> The reason is conservation of three-momentum. In the lab frame the incoming beam carries a large momentum, and that momentum must be carried away by the products — so the products *cannot* be at rest after the collision; they must keep moving, and the kinetic energy tied up in that forced motion is wasted, unavailable for making rest mass. In the centre-of-momentum frame the total momentum is zero, the products can be born at rest, and *every* bit of input kinetic energy converts to rest mass.
>
> This is precisely why modern particle accelerators — the LHC above all — **collide two beams head-on** (realising the centre-of-momentum frame) rather than firing one beam at a stationary target. To reach a given $M$, a fixed-target machine needs energy growing as $M^2$, a collider only as $M$. For the heavy particles of interest (the $W$, $Z$, the Higgs, hypothetical new states) the quadratic penalty is the difference between feasible and impossible.

> [!note]- Complete formal solution
> Conservation of four-momentum reads $P_1 + P_2 = P_3 + P_4 + P_5$. The invariant $(P_1+P_2)^2$ may be evaluated in any frame.
>
> *Centre-of-momentum frame, threshold:* the products are at rest, so the outgoing four-momentum is $((2m+M)c,\mathbf{0})$ and $(P_1+P_2)^2 = (2m+M)^2c^2$. Equivalently, conservation of energy with both incoming particles at speed $v$ gives $2m\gamma_v c^2 = (2m+M)c^2$, so $\gamma_v = 1 + M/2m$.
>
> *Lab frame:* with $P_1 = (m\gamma_u c, m\gamma_u\mathbf{u})$, $P_2 = (mc,\mathbf{0})$,
> $$(P_1+P_2)^2 = 2m^2c^2 + 2m^2\gamma_u c^2 = 2m^2c^2(1+\gamma_u).$$
> Equating to $(2m+M)^2c^2$: $\;\gamma_u = 1 + 2M/m + M^2/2m^2$, so the threshold beam kinetic energy is $T_u = 2Mc^2 + M^2c^2/2m$.
>
> For $M\gg m$, $T_u\approx M^2c^2/2m$ (quadratic in $M$) versus total $T = Mc^2$ (linear) in the centre-of-momentum frame. Conservation of momentum forces the lab-frame products to keep moving, wasting kinetic energy; colliding beams realise the centre-of-momentum frame and avoid the quadratic penalty. $\blacksquare$

---

# Key Takeaways

**At threshold, the products are at rest in the centre-of-momentum frame — this is the entire content of "minimum energy".** Every threshold problem hinges on translating the word "minimum" into a kinematic statement, and the translation is always the same: with the least possible input energy, there is nothing left over for the products' kinetic energy, so in the frame where their total momentum vanishes — the centre-of-momentum frame — they are all simultaneously at rest. This makes the outgoing side trivial: $\sum P_{\text{out}} = (\sum m_{\text{out}}\cdot c,\,\mathbf{0})$, whose square is $(\sum m_{\text{out}})^2c^2$. The reason it must be the centre-of-momentum frame and not the lab is that conservation of momentum forbids the products from being at rest in any frame where the total momentum is nonzero. Whenever you see "threshold", "minimum energy", or "least energetic", immediately write down the products at rest in the centre-of-momentum frame.

**The invariant $(\sum P)^2$ is the universal bridge between frames — evaluate it where each side is easiest.** The square of the total four-momentum is a Lorentz scalar, so it is one number computable in any frame, and the art is to compute the *incoming* side in the frame where the beam kinematics are given (the lab) and the *outgoing* side in the frame where the threshold condition is simple (the centre-of-momentum frame), then equate. This sidesteps ever transforming a four-vector explicitly: the invariance does the frame-changing for free. The same move — "compute the invariant mass of the system in two frames and equate" — solves essentially every collision problem in the topic, and it generalises: in a decay, the invariant mass of the products equals the parent's mass; in scattering, $(\sum P)^2$ before equals $(\sum P)^2$ after. Squaring a four-momentum equation is never a loss; it converts a vector statement into a scalar one about quantities every observer agrees on.

**Conservation of momentum makes fixed-target collisions quadratically wasteful.** The headline result — lab-frame threshold energy scales as $M^2/m$, centre-of-momentum threshold as $M$ — is not an algebraic accident; it is conservation of three-momentum exacting a tax. In the lab the incoming beam carries momentum, the products must carry it away, so the products cannot stop, and the kinetic energy locked into that compulsory motion is energy that *cannot* be spent making rest mass. The centre-of-momentum frame has zero total momentum, the products may be born at rest, and the conversion of kinetic energy into mass is perfectly efficient. This is a completely general lesson about relativistic reactions: useful energy is the energy available *in the centre-of-momentum frame*, the invariant $\sqrt{(\sum P)^2}\,c$, and any frame with net momentum wastes the rest. It is why the LHC collides counter-rotating beams, and why the relevant figure of merit for a collider is the centre-of-mass energy, not the beam energy.
