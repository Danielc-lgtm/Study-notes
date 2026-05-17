---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Problem Statement

A particle of rest mass $M$, **at rest** in some inertial frame, decays into two particles of rest masses $m_2$ and $m_3$:
$$M \;\longrightarrow\; m_2 + m_3.$$

**(a)** Show the decay is possible only if $M \ge m_2 + m_3$.

**(b)** Working in the rest frame of the parent, find the energies $E_2$ and $E_3$ of the two decay products entirely in terms of the three masses. Show in particular that
$$E_2 = \frac{(M^2 + m_2^2 - m_3^2)c^2}{2M}.$$

**(c)** Find the Lorentz factors $\gamma_2,\gamma_3$ and the common magnitude $|\mathbf{p}|$ of the two products' three-momenta, and verify that for the symmetric case $m_2 = m_3 = m$ the products fly apart back-to-back with equal speeds and $\gamma = M/2m$.

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - Four-Momentum and Rest Mass#The Mass-Shell Relation]]

A particle of rest mass $m$ has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E/c,\mathbf{p})$ with $P\cdot P = m^2c^2$, i.e. $E^2 = \mathbf{p}^2c^2 + m^2c^4$. A particle at rest has $P^\mu = (mc,\mathbf{0})$.

---

# Convergent Strategy

**Problem class.** This is a *decay-kinematics* problem: conservation of four-momentum determines the products' energies and momenta from the masses alone.

**Assumption pattern.** The parent is at rest, so its four-momentum is the simple $(Mc,\mathbf{0})$. There are two products; the conservation law is four scalar equations, and the masses are the only data — the answer must be a formula in $M,m_2,m_3$.

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] gives $P_1 = P_2 + P_3$. To get $E_2$, isolate the *other* product: $P_3 = P_1 - P_2$, then square — $P_3\cdot P_3 = m_3^2c^2$ on the left, and the right contains the known $P_1\cdot P_1 = M^2c^2$, $P_2\cdot P_2 = m_2^2c^2$, and $P_1\cdot P_2$, which in the parent rest frame is simply $M E_2$.

**Key decision point.** The move is, as ever, *isolate the four-momentum you do not want ($P_3$) and square*. Squaring eliminates $P_3$'s direction and speed, leaving a linear equation for $E_2$. The parent's rest frame makes $P_1\cdot P_2 = ME_2$ trivially, which is what lets the energy be solved for directly.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — $P_1 = P_2 + P_3$.
2. **Go to the rest frame of a chosen particle** — the parent's rest frame, $P_1 = (Mc,\mathbf{0})$.
3. **Square a four-momentum to extract an invariant mass** — squaring the isolated $P_3$ gives $m_3^2c^2$.
4. **Use the mass-shell relation** — $P_i\cdot P_i = m_i^2c^2$ for each particle.

---

# Hints

> [!note]- Hint 1
> Work in the rest frame of the parent. Its four-momentum is $P_1 = (Mc,\mathbf{0})$ — the simplest possible. Conservation of four-momentum gives $P_1 = P_2 + P_3$, so the products have equal and opposite three-momenta.

> [!note]- Hint 2
> For part (a): the time component of $P_1 = P_2 + P_3$ is $Mc^2 = E_2 + E_3$. Each $E_i = \sqrt{\mathbf{p}_i^2c^2 + m_i^2c^4} \ge m_ic^2$. Add the inequalities.

> [!note]- Hint 3
> For $E_2$: isolate the *other* product, $P_3 = P_1 - P_2$, and square. Then $P_3\cdot P_3 = m_3^2c^2$ on the left; expand $(P_1-P_2)^2$ on the right.

> [!note]- Hint 4
> In the parent's rest frame $P_1 = (Mc,\mathbf{0})$, so $P_1\cdot P_2 = Mc\cdot(E_2/c) - \mathbf{0}\cdot\mathbf{p}_2 = ME_2$. The squared equation becomes linear in $E_2$ — solve it.

---

# Solution

The parent at rest gives the cleanest possible starting four-momentum, $(Mc,\mathbf{0})$. Isolating one product and squaring eliminates it, and because $P_1\cdot P_2 = ME_2$ in the rest frame, the squared equation is *linear* in the energy — so $E_2$ drops out at once.

**Step 1: The decay is possible only if $M\ge m_2+m_3$ (part a).**

> [!note]- Derivation
> In the parent's rest frame, [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] $P_1 = P_2 + P_3$ has time component (conservation of energy)
> $$Mc^2 = E_2 + E_3.$$
> Each product satisfies the [[Def - Four-Momentum and Rest Mass|energy–momentum relation]] $E_i = \sqrt{\mathbf{p}_i^2c^2 + m_i^2c^4}$, so
> $$E_i \ge \sqrt{m_i^2c^4} = m_ic^2,$$
> with equality only if $\mathbf{p}_i = 0$. Adding the two inequalities,
> $$Mc^2 = E_2 + E_3 \ge m_2c^2 + m_3c^2 \;\Longrightarrow\; M \ge m_2 + m_3.$$
> A particle can decay only into products whose rest masses sum to no more than its own. If $M = m_2+m_3$ exactly, the products are born at rest (the threshold case); if $M > m_2+m_3$, the surplus $(M - m_2 - m_3)c^2$ — the **$Q$-value** of the decay — appears as kinetic energy of the products. If $M < m_2+m_3$ the decay is kinematically forbidden, no matter what.

**Step 2: The energy of product 2 (part b).**

Isolating $P_3$ and squaring gives $E_2 = \dfrac{(M^2 + m_2^2 - m_3^2)c^2}{2M}$.

> [!note]- Derivation
> From $P_1 = P_2 + P_3$, isolate the product whose energy we are *not* solving for:
> $$P_3 = P_1 - P_2.$$
> Square both sides (Minkowski inner product with itself):
> $$P_3\cdot P_3 = (P_1 - P_2)\cdot(P_1-P_2) = P_1\cdot P_1 - 2P_1\cdot P_2 + P_2\cdot P_2.$$
> Now invoke the [[Def - Four-Momentum and Rest Mass|mass shells]]: $P_3\cdot P_3 = m_3^2c^2$, $P_1\cdot P_1 = M^2c^2$, $P_2\cdot P_2 = m_2^2c^2$. So
> $$m_3^2c^2 = M^2c^2 + m_2^2c^2 - 2P_1\cdot P_2.$$
> The cross term $P_1\cdot P_2$ is evaluated in the **parent's rest frame**, where $P_1 = (Mc,\mathbf{0})$ and $P_2 = (E_2/c,\mathbf{p}_2)$:
> $$P_1\cdot P_2 = (Mc)\Big(\frac{E_2}{c}\Big) - \mathbf{0}\cdot\mathbf{p}_2 = M E_2.$$
> The squared equation is therefore *linear* in $E_2$:
> $$m_3^2c^2 = M^2c^2 + m_2^2c^2 - 2ME_2 \;\Longrightarrow\; 2ME_2 = (M^2 + m_2^2 - m_3^2)c^2,$$
> $$\boxed{\;E_2 = \frac{(M^2 + m_2^2 - m_3^2)c^2}{2M}\;}$$
> By the symmetry $2\leftrightarrow 3$ (isolate $P_2$ instead and square),
> $$E_3 = \frac{(M^2 + m_3^2 - m_2^2)c^2}{2M}.$$
> Check: $E_2 + E_3 = \dfrac{(M^2+m_2^2-m_3^2) + (M^2+m_3^2-m_2^2)}{2M}c^2 = \dfrac{2M^2}{2M}c^2 = Mc^2$ — conservation of energy, as it must. The energies are fixed *entirely* by the three rest masses; a two-body decay is **monoenergetic**, with no spread.

**Step 3: Lorentz factors and momenta (part c).**

> [!note]- Derivation
> The Lorentz factor of product 2 follows from $E_2 = \gamma_2 m_2c^2$:
> $$\gamma_2 = \frac{E_2}{m_2c^2} = \frac{M^2 + m_2^2 - m_3^2}{2Mm_2}, \qquad \gamma_3 = \frac{M^2 + m_3^2 - m_2^2}{2Mm_3}.$$
> The common magnitude of the three-momenta — equal because $P_1 = P_2+P_3$ with $\mathbf{p}_1 = 0$ forces $\mathbf{p}_2 = -\mathbf{p}_3$ — comes from the energy–momentum relation for product 2:
> $$|\mathbf{p}|^2c^2 = E_2^2 - m_2^2c^4 = \Big(\frac{(M^2+m_2^2-m_3^2)c^2}{2M}\Big)^2 - m_2^2c^4.$$
> Putting over a common denominator $4M^2$ and recognising the difference of squares,
> $$|\mathbf{p}|^2c^2 = \frac{(M^2+m_2^2-m_3^2)^2 - 4M^2m_2^2}{4M^2}c^4 = \frac{\big[(M^2+m_2^2-m_3^2) - 2Mm_2\big]\big[(M^2+m_2^2-m_3^2)+2Mm_2\big]}{4M^2}c^4.$$
> The two brackets are $\big[(M-m_2)^2 - m_3^2\big]$ and $\big[(M+m_2)^2 - m_3^2\big]$, each again a difference of squares:
> $$|\mathbf{p}|c = \frac{c^2}{2M}\sqrt{(M-m_2-m_3)(M-m_2+m_3)(M+m_2-m_3)(M+m_2+m_3)}.$$
> This compact result — sometimes called the **Källén function** or triangle function — is real precisely when $M \ge m_2 + m_3$ (the first factor non-negative), reconfirming part (a): the products' momentum is real exactly when the decay is allowed.
>
> **Symmetric case $m_2 = m_3 = m$.** Then $E_2 = E_3 = \dfrac{(M^2 + m^2 - m^2)c^2}{2M} = \dfrac{Mc^2}{2}$ — the two products share the parent's energy equally. The Lorentz factor is
> $$\gamma_2 = \gamma_3 = \frac{E}{mc^2} = \frac{M}{2m},$$
> and since $\mathbf{p}_2 = -\mathbf{p}_3$ with equal magnitudes and equal masses, the two products fly apart **back-to-back at equal speeds**. The condition $M\ge 2m$ is exactly the requirement $\gamma = M/2m \ge 1$. (This matches the Oxford-notes result for $A\to B+B$, and as $m\to 0$ it becomes the symmetric decay into two photons, each of energy $Mc^2/2$.)

> [!note]- Complete formal solution
> Work in the parent's rest frame, $P_1 = (Mc,\mathbf{0})$. Conservation of four-momentum: $P_1 = P_2 + P_3$.
>
> **(a)** Time component: $Mc^2 = E_2 + E_3$. Since $E_i = \sqrt{\mathbf{p}_i^2c^2+m_i^2c^4}\ge m_ic^2$, adding gives $M\ge m_2+m_3$.
>
> **(b)** Isolate $P_3 = P_1 - P_2$ and square: $m_3^2c^2 = M^2c^2 + m_2^2c^2 - 2P_1\cdot P_2$. In the rest frame $P_1\cdot P_2 = ME_2$, so
> $$E_2 = \frac{(M^2+m_2^2-m_3^2)c^2}{2M}, \qquad E_3 = \frac{(M^2+m_3^2-m_2^2)c^2}{2M},$$
> and $E_2+E_3 = Mc^2$ as required.
>
> **(c)** $\gamma_i = E_i/m_ic^2$; the common momentum magnitude is
> $$|\mathbf{p}|c = \frac{c^2}{2M}\sqrt{(M{-}m_2{-}m_3)(M{-}m_2{+}m_3)(M{+}m_2{-}m_3)(M{+}m_2{+}m_3)},$$
> real iff $M\ge m_2+m_3$. For $m_2=m_3=m$: $E_2=E_3=Mc^2/2$, $\gamma=M/2m$, products back-to-back at equal speed. $\blacksquare$

---

# Key Takeaways

**A two-body decay is completely determined by the three rest masses — it is monoenergetic.** The striking feature of this problem is that the answer contains *no* free parameters: given $M$, $m_2$, $m_3$, the energies $E_2$, $E_3$, the speeds, and the momentum magnitude are all fixed numbers. Conservation of four-momentum is four equations, the two product four-momenta carry $2\times 3 = 6$ unknowns minus the overall direction freedom, and the count works out so that the *energies* are pinned down exactly. This is why a two-body decay produces decay products of sharp, definite energy — a spectral line — whereas a three-body decay (such as beta decay, $n\to p + e^- + \bar\nu$) produces a *continuous* spectrum, because the extra particle leaves a free parameter. Historically the continuous beta spectrum was the clue that a third, unseen particle — the neutrino — had to be present. The lesson: count the kinematic degrees of freedom against the conservation equations to predict whether decay products are monoenergetic.

**Isolate the product you are not solving for, then square.** To find $E_2$ we isolated $P_3$ — the *other* particle — and squared it away. This seems backwards at first: why eliminate $P_3$ when we want $E_2$? Because squaring $P_3$ turns it into the known $m_3^2c^2$ and removes its three unknown components, while the cross term $P_1\cdot P_2$, in the rest frame, is just $ME_2$ — linear in exactly the quantity we want. The general principle: to solve for one particle's energy, eliminate the *other* particle by isolate-and-square; the conservation equation then becomes linear in the target energy. This is the same elimination technique as in [[Ex - Compton scattering|Compton scattering]] and [[Ex - Threshold energy for particle production|threshold]] problems, and recognising which four-momentum to isolate — the one *not* in the answer — is the whole skill.

**The triangle (Källén) function packages the kinematic boundary.** The momentum magnitude came out as a square root of a product of four factors, $(M\mp m_2\mp m_3)(\cdots)$, the Källén function $\lambda(M^2,m_2^2,m_3^2)$. Its structure is informative: it is real exactly when $M\ge m_2+m_3$, so the *same* algebra that computes the momentum also re-derives the decay-possibility condition of part (a) — the momentum is real precisely when the decay is allowed, and it vanishes at threshold $M = m_2+m_3$ where the products are born at rest. This function recurs throughout relativistic kinematics: it governs phase space in decay rates, the boundary of the Dalitz plot in three-body decays, and threshold behaviour in scattering. Whenever a two-body relativistic kinematics problem produces a momentum magnitude, expect the Källén function, and read off the kinematic boundary from where it changes sign.
