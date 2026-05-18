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

Consider a two-body scattering process $1 + 2 \to 3 + 4$, in which two incoming particles with [[Def - Four-Momentum and Rest Mass|four-momenta]] $P_1, P_2$ and rest masses $m_1, m_2$ collide and produce two outgoing particles with four-momenta $P_3, P_4$ and rest masses $m_3, m_4$. Define the three **Mandelstam variables**
$$s = (P_1 + P_2)^2, \qquad t = (P_1 - P_3)^2, \qquad u = (P_1 - P_4)^2,$$
where $X^2 \equiv X\cdot X$ denotes the Minkowski square.

**(a)** Show that each of $s$, $t$, $u$ is a Lorentz invariant, and prove the **sum rule**
$$s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2.$$

**(b)** Show that $s$ is the square of the invariant mass of the system, and that in the centre-of-momentum frame $\sqrt{s}$ equals the total energy — the **centre-of-mass energy** $E_{\text{cm}}$. Deduce the threshold condition $\sqrt{s} \ge m_3 + m_4$ for the reaction to be kinematically possible.

**(c)** Compute $s$ explicitly for two experimental arrangements, taking for simplicity $m_1 = m_2 = m$:
  (i) a **collider**, in which the two beams have equal and opposite three-momenta, each particle having energy $E$;
  (ii) a **fixed-target** experiment, in which particle $2$ is at rest and particle $1$ has lab energy $E_{\text{lab}}$.
Compare the centre-of-mass energy $\sqrt{s}$ reachable by each at large beam energy.

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - Four-Momentum and Rest Mass#The Mass-Shell Relation]]

The Minkowski inner product of two four-vectors $A^\mu = (A^0,\mathbf{A})$ and $B^\mu = (B^0,\mathbf{B})$ is $A\cdot B = A^0 B^0 - \mathbf{A}\cdot\mathbf{B}$, and it is the same number in every inertial frame — that is the defining property of a Lorentz invariant. In particular the Minkowski square of any sum or difference of four-momenta is a Lorentz scalar. The square of a *single* particle's four-momentum is its rest mass squared: $P_i\cdot P_i = m_i^2$ (the mass-shell relation, $c = 1$).

---

# Convergent Strategy

**Problem class.** This is a *structural* kinematics problem: rather than solving a specific collision, it sets up the invariant language in which every two-body collision is described. The target is not a number but three identities — invariance, the sum rule, and the interpretation of $\sqrt{s}$.

**Assumption pattern.** Two ingredients drive every step. The first is that each external particle is *on its mass shell*, $P_i\cdot P_i = m_i^2$ — squaring any single four-momentum yields a known mass. The second is [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], $P_1 + P_2 = P_3 + P_4$, which is the *only* dynamical input and is what makes the three Mandelstam variables dependent rather than independent.

**Theorem routing.** Invariance of $s,t,u$ is immediate: each is a Minkowski square of a four-vector, hence a contraction with one index up and one down, hence a scalar. The sum rule routes through *both* assumptions — expand the three squares (mass shells supply the diagonal terms), then collapse the cross terms using conservation of four-momentum. Part (b) routes through the centre-of-momentum frame, where the total four-momentum is purely temporal so its square is the total energy squared. Part (c) is direct component arithmetic.

**Key decision point.** The one non-obvious move is in the sum rule: after expanding, the cross terms are $2P_1\cdot(P_2 - P_3 - P_4)$, and the trick is to recognise — using conservation — that the bracket is exactly $-P_1$, turning a sum of three awkward inner products into the single mass-shell value $-2m_1^2$. Spotting that conservation lets you *eliminate* $P_2,P_3,P_4$ in favour of $P_1$ is what makes the cross terms cancel.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Square a four-momentum to extract an invariant mass** — every $P_i\cdot P_i$ is replaced by $m_i^2$ when the three Mandelstam squares are expanded.
2. **Write down the total four-momentum and set it equal before and after** — conservation $P_1 + P_2 = P_3 + P_4$ collapses the cross terms in the sum rule.
3. **Raise and lower indices with the metric, and keep contractions paired** — each Mandelstam variable is a properly paired Minkowski contraction, which is what makes it a Lorentz scalar.
4. **Go to the centre-of-momentum frame** — where the total four-momentum is purely temporal and $s = E_{\text{cm}}^2$.
5. **Use a Lorentz invariant to switch frames** — $s$ is computed in the lab and reinterpreted in the centre-of-momentum frame because it is the same number in both.

---

# Hints

> [!note]- Hint 1
> A Minkowski square $X\cdot X = \eta_{\mu\nu}X^\mu X^\nu$ has one index up and one down — it is a fully contracted scalar. What does that tell you about how it transforms under a Lorentz boost? Apply this to $X = P_1 + P_2$, $X = P_1 - P_3$, $X = P_1 - P_4$.

> [!note]- Hint 2
> For the sum rule, expand each square with the Minkowski binomial formula $(A\pm B)^2 = A^2 \pm 2A\cdot B + B^2$. Every "diagonal" term $P_i\cdot P_i$ is a known mass squared. Collect the surviving cross terms — they all contain $P_1$.

> [!note]- Hint 3
> The cross terms sum to $2P_1\cdot P_2 - 2P_1\cdot P_3 - 2P_1\cdot P_4 = 2P_1\cdot(P_2 - P_3 - P_4)$. Now use [[Thm - Conservation of Four-Momentum|conservation of four-momentum]]: $P_1 + P_2 = P_3 + P_4$ rearranges to $P_2 - P_3 - P_4 = -P_1$.

> [!note]- Hint 4
> For (b), in the centre-of-momentum frame the total three-momentum vanishes, so $P_1 + P_2 = (E_{\text{cm}}, \mathbf{0})$ and $s = (P_1+P_2)^2 = E_{\text{cm}}^2$. For (c), write the four-momenta in components: collider has $P_1 = (E,\mathbf{p})$, $P_2 = (E,-\mathbf{p})$; fixed target has $P_1 = (E_{\text{lab}}, \mathbf{p}_{\text{lab}})$, $P_2 = (m,\mathbf{0})$.

---

# Solution

The whole exercise is the unpacking of one fact: $s$, $t$, $u$ are Minkowski squares of four-vectors, hence Lorentz scalars, and conservation of four-momentum ties them together. Invariance is one line; the sum rule is the expand-and-collapse computation; the meaning of $\sqrt{s}$ is read off in the centre-of-momentum frame.

**Step 1: Each Mandelstam variable is a Lorentz invariant (part a).**

Each of $s,t,u$ is the Minkowski square of a four-vector, and a Minkowski square is a fully contracted scalar — the same number in every inertial frame.

> [!note]- Derivation
> The sum $P_1 + P_2$ and the differences $P_1 - P_3$, $P_1 - P_4$ are each a linear combination of [[Def - Four-Momentum and Rest Mass|four-momenta]], hence each is itself a four-vector: under a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ it transforms as $X^\mu \to \Lambda^\mu{}_\nu X^\nu$. The Minkowski square of any four-vector,
> $$X^2 = \eta_{\mu\nu}X^\mu X^\nu = X_\mu X^\mu,$$
> is a contraction of an upper index with a lower one. Under $\Lambda$, $X^\mu X_\mu \to (\Lambda^\mu{}_\alpha X^\alpha)(\Lambda_\mu{}^\beta X_\beta) = (\Lambda^\mu{}_\alpha\Lambda_\mu{}^\beta) X^\alpha X_\beta = \delta_\alpha^\beta X^\alpha X_\beta = X^\beta X_\beta$, using the defining property $\Lambda^T\eta\Lambda = \eta$ of a Lorentz transformation. So the value is unchanged: $s$, $t$, $u$ are Lorentz scalars, computable in whichever frame is convenient and equal in all.

**Step 2: The sum rule $s + t + u = \sum_i m_i^2$ (part a).**

Expanding the three squares, every diagonal term is a mass squared and the cross terms collapse — via conservation of four-momentum — to $-2m_1^2$, leaving $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.

> [!note]- Derivation
> Expand each Mandelstam variable with $(A \pm B)^2 = A^2 \pm 2A\cdot B + B^2$ and use the mass-shell relation $P_i\cdot P_i = m_i^2$:
> $$s = (P_1 + P_2)^2 = P_1^2 + P_2^2 + 2P_1\cdot P_2 = m_1^2 + m_2^2 + 2P_1\cdot P_2,$$
> $$t = (P_1 - P_3)^2 = P_1^2 + P_3^2 - 2P_1\cdot P_3 = m_1^2 + m_3^2 - 2P_1\cdot P_3,$$
> $$u = (P_1 - P_4)^2 = P_1^2 + P_4^2 - 2P_1\cdot P_4 = m_1^2 + m_4^2 - 2P_1\cdot P_4.$$
> Add the three. The diagonal terms give $3m_1^2 + m_2^2 + m_3^2 + m_4^2$. The cross terms give
> $$2P_1\cdot P_2 - 2P_1\cdot P_3 - 2P_1\cdot P_4 = 2P_1\cdot(P_2 - P_3 - P_4).$$
> Now invoke [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], $P_1 + P_2 = P_3 + P_4$. Rearranged, this reads $P_2 - P_3 - P_4 = -P_1$. Substituting,
> $$2P_1\cdot(P_2 - P_3 - P_4) = 2P_1\cdot(-P_1) = -2P_1\cdot P_1 = -2m_1^2.$$
> The cross terms therefore contribute $-2m_1^2$, and
> $$s + t + u = \big(3m_1^2 + m_2^2 + m_3^2 + m_4^2\big) - 2m_1^2 = m_1^2 + m_2^2 + m_3^2 + m_4^2.$$
> The sum of the three invariants is fixed entirely by the external masses; it carries no information about the dynamics or the scattering angle. Consequently a two-body process has only *two* independent kinematic invariants, and a scattering amplitude is genuinely a function $\mathcal{M}(s,t)$ — the third variable $u$ is determined.

**Step 3: $s$ is the invariant mass squared, and $\sqrt{s} = E_{\text{cm}}$ (part b).**

In the centre-of-momentum frame the total four-momentum is purely temporal, so $s = E_{\text{cm}}^2$; the threshold for the reaction is $\sqrt{s} \ge m_3 + m_4$.

> [!note]- Derivation
> By conservation of four-momentum, $P_1 + P_2 = P_3 + P_4 \equiv P_{\text{tot}}$, so $s = (P_1+P_2)^2 = P_{\text{tot}}^2$ — the Minkowski square of the *total* four-momentum, which is by definition the **invariant mass squared** $M_{\text{sys}}^2$ of the whole system.
>
> The **centre-of-momentum frame** is the inertial frame in which the total three-momentum vanishes, $\sum\mathbf{p} = \mathbf{0}$. In that frame $P_{\text{tot}}^\mu = (E_{\text{cm}}, \mathbf{0})$, where $E_{\text{cm}}$ is the total energy, and therefore
> $$s = P_{\text{tot}}^2 = E_{\text{cm}}^2 - \mathbf{0}^2 = E_{\text{cm}}^2 \;\Longrightarrow\; \sqrt{s} = E_{\text{cm}}.$$
> Because $s$ is a Lorentz invariant (Step 1), this identifies $\sqrt{s}$ in *every* frame as the centre-of-mass energy — it is the headline number characterising the collision.
>
> For the reaction to be kinematically possible, the outgoing particles $3$ and $4$ must at least be created. Evaluate $s$ from the outgoing side in the centre-of-momentum frame: $s = (P_3 + P_4)^2 = (E_3 + E_4)^2 - (\mathbf{p}_3 + \mathbf{p}_4)^2$. Since the total outgoing three-momentum also vanishes in this frame, $s = (E_3 + E_4)^2$, with $E_3 \ge m_3$ and $E_4 \ge m_4$ because each energy is at least the rest energy. Hence
> $$\sqrt{s} = E_3 + E_4 \ge m_3 + m_4.$$
> The reaction can proceed only if the centre-of-mass energy is at least the sum of the product rest masses; equality is the threshold, where the products are created at rest in the centre-of-momentum frame.

**Step 4: $s$ for a collider versus a fixed target (part c).**

A collider gives $s = 4E^2$; a fixed target gives $s = 2m^2 + 2mE_{\text{lab}}$. At large energy the collider reaches $\sqrt{s} \sim 2E$ but the fixed target only $\sqrt{s} \sim \sqrt{2mE_{\text{lab}}}$.

> [!note]- Derivation
> Take $m_1 = m_2 = m$ and use that $s = (P_1 + P_2)^2 = P_1^2 + P_2^2 + 2P_1\cdot P_2 = 2m^2 + 2P_1\cdot P_2$ from Step 2; the whole computation reduces to evaluating the single inner product $P_1\cdot P_2$.
>
> *(i) Collider.* The two beams have equal and opposite three-momenta, each particle of energy $E$ and momentum magnitude $|\mathbf{p}|$:
> $$P_1 = (E, \mathbf{p}), \qquad P_2 = (E, -\mathbf{p}).$$
> Then $P_1\cdot P_2 = E\cdot E - \mathbf{p}\cdot(-\mathbf{p}) = E^2 + |\mathbf{p}|^2$. Using the mass shell $E^2 = |\mathbf{p}|^2 + m^2$, so $|\mathbf{p}|^2 = E^2 - m^2$,
> $$P_1\cdot P_2 = E^2 + (E^2 - m^2) = 2E^2 - m^2.$$
> Hence
> $$s = 2m^2 + 2(2E^2 - m^2) = 4E^2 \;\Longrightarrow\; \sqrt{s} = 2E.$$
> Every bit of the two beam energies appears in the centre-of-mass energy — the collider *is* the centre-of-momentum frame.
>
> *(ii) Fixed target.* Particle $2$ is at rest, particle $1$ has lab energy $E_{\text{lab}}$ and momentum $\mathbf{p}_{\text{lab}}$:
> $$P_1 = (E_{\text{lab}}, \mathbf{p}_{\text{lab}}), \qquad P_2 = (m, \mathbf{0}).$$
> Then $P_1\cdot P_2 = E_{\text{lab}}\cdot m - \mathbf{p}_{\text{lab}}\cdot\mathbf{0} = m E_{\text{lab}}$, and
> $$s = 2m^2 + 2m E_{\text{lab}} \;\Longrightarrow\; \sqrt{s} = \sqrt{2m^2 + 2m E_{\text{lab}}}.$$
>
> *Comparison at large energy.* For the collider $\sqrt{s} = 2E$ grows *linearly* with the beam energy. For the fixed target, at $E_{\text{lab}} \gg m$ the dominant term is $s \approx 2m E_{\text{lab}}$, so
> $$\sqrt{s} \approx \sqrt{2m E_{\text{lab}}},$$
> which grows only as the *square root* of the beam energy. To reach a given centre-of-mass energy $\sqrt{s}$, a collider needs beam energy $E \sim \sqrt{s}/2$, while a fixed-target machine needs $E_{\text{lab}} \sim s/2m$ — quadratically more. This is the same quadratic penalty seen in [[Ex - Threshold energy for particle production|the threshold problem]], stated now in the invariant language of $s$: the useful energy of a collision is $\sqrt{s}$, and fixed-target geometry squanders most of the beam energy on the unavoidable forward motion of the products.

> [!note]- Complete formal solution
> **(a)** Each of $P_1+P_2$, $P_1-P_3$, $P_1-P_4$ is a four-vector. Its Minkowski square $X_\mu X^\mu$ is a contraction of an upper with a lower index; under $\Lambda$, $X_\mu X^\mu \to \Lambda^\mu{}_\alpha\Lambda_\mu{}^\beta X^\alpha X_\beta = \delta^\beta_\alpha X^\alpha X_\beta = X^\beta X_\beta$, so $s,t,u$ are Lorentz invariants.
> Expanding with the mass shells $P_i^2 = m_i^2$:
> $$s = m_1^2 + m_2^2 + 2P_1\cdot P_2, \quad t = m_1^2 + m_3^2 - 2P_1\cdot P_3, \quad u = m_1^2 + m_4^2 - 2P_1\cdot P_4.$$
> Summing, the cross terms are $2P_1\cdot(P_2 - P_3 - P_4)$; conservation of four-momentum $P_1 + P_2 = P_3 + P_4$ gives $P_2 - P_3 - P_4 = -P_1$, so the cross terms equal $-2P_1^2 = -2m_1^2$, and
> $$s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 - 2m_1^2 = m_1^2 + m_2^2 + m_3^2 + m_4^2.$$
> **(b)** By conservation, $s = (P_1+P_2)^2 = P_{\text{tot}}^2 = M_{\text{sys}}^2$. In the centre-of-momentum frame $P_{\text{tot}} = (E_{\text{cm}},\mathbf{0})$, so $s = E_{\text{cm}}^2$ and $\sqrt s = E_{\text{cm}}$. Evaluating $s$ from the outgoing side in that frame, $\sqrt s = E_3 + E_4 \ge m_3 + m_4$, the threshold condition.
> **(c)** With $m_1=m_2=m$, $s = 2m^2 + 2P_1\cdot P_2$. Collider: $P_1=(E,\mathbf{p})$, $P_2=(E,-\mathbf{p})$, $P_1\cdot P_2 = E^2 + |\mathbf{p}|^2 = 2E^2 - m^2$, so $s = 4E^2$, $\sqrt s = 2E$. Fixed target: $P_1 = (E_{\text{lab}},\mathbf{p}_{\text{lab}})$, $P_2 = (m,\mathbf{0})$, $P_1\cdot P_2 = mE_{\text{lab}}$, so $s = 2m^2 + 2mE_{\text{lab}}$, $\sqrt s = \sqrt{2m^2 + 2mE_{\text{lab}}}$. At large energy $\sqrt s \to 2E$ (collider, linear) versus $\sqrt s \to \sqrt{2mE_{\text{lab}}}$ (fixed target, square-root): the collider converts beam energy into centre-of-mass energy with no loss, the fixed target quadratically worse. $\blacksquare$

---

# Key Takeaways

**A Minkowski square is automatically a Lorentz invariant — this is why $s$, $t$, $u$ are the right variables.** The reason particle physics is written in terms of $s$, $t$, $u$ rather than energies and angles is that energies and angles are frame-dependent, treacherous quantities, while a fully contracted Minkowski square $X_\mu X^\mu$ is the same number for every observer. Whenever you want a *frame-independent* description of a process, the move is to build it out of contracted four-vectors: squares of four-momentum sums and differences, and inner products $P_i\cdot P_j$. This is the same discipline that runs through every collision problem in the topic — solve in the world of invariants, translate to components only at the end — and the Mandelstam variables are simply the canonical complete set of invariants for a two-body process. Recognising that "this quantity is a Minkowski square, hence a scalar" is a one-line proof of invariance that you should reach for automatically.

**The sum rule is conservation of four-momentum in disguise — expand, then eliminate.** The identity $s + t + u = \sum m_i^2$ looks like a coincidence until you see the mechanism: expanding the three squares produces diagonal terms (fixed by the mass shells) and cross terms (all containing $P_1$), and conservation of four-momentum is precisely the statement that lets you replace $P_2 - P_3 - P_4$ by $-P_1$, collapsing the cross terms to a single mass-shell value. The general lesson is a trigger-reaction pattern: *when an expression contains several four-momenta and you have a conservation law, use the law to eliminate all but one of them*. This is the same elimination move that solves [[Ex - Compton scattering|Compton scattering]] and [[Ex - Two-body decay kinematics|two-body decay]] — there one isolates an unwanted four-momentum and squares it; here one substitutes the conservation relation directly. The payoff of the sum rule is structural: a two-body process has only two independent invariants, so a scattering amplitude lives on a two-dimensional region of the $(s,t)$ plane, and crossing symmetry can relate different physical channels by analytic continuation within that region.

**$\sqrt{s}$ is the centre-of-mass energy, and it is the true figure of merit for a collision.** The variable $s$ has a clean physical reading that makes it the most important of the three: it is the square of the total four-momentum, hence the invariant mass squared of the whole system, and evaluated in the centre-of-momentum frame — where the total three-momentum vanishes — it is simply the total energy squared. So $\sqrt{s}$ is the energy available to *do something* — to create new particles, with threshold $\sqrt{s} \ge \sum m_{\text{out}}$. The collider-versus-fixed-target computation makes the practical consequence vivid: a collider has $\sqrt{s} = 2E$, linear in beam energy, because it already sits in the centre-of-momentum frame; a fixed-target machine has $\sqrt{s} \approx \sqrt{2mE_{\text{lab}}}$, only square-root in beam energy, because conservation of momentum forces the products to keep moving and wastes the rest. Whenever you are asked "how much energy is available in this collision", the answer is never the beam energy — it is $\sqrt{s}$, the invariant, and computing it in whichever frame is convenient (then trusting its invariance) is the fastest route to every threshold and every collider-design question.
