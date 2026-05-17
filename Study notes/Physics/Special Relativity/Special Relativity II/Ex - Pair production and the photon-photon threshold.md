---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

**(a)** Show that a single photon travelling through empty space **cannot** decay into an electron–positron pair, $\gamma \not\to e^+ + e^-$, no matter how energetic it is.

**(b)** Two photons *can* collide to produce an electron–positron pair, $\gamma + \gamma \to e^+ + e^-$. Suppose the two photons have energies $E_1$ and $E_2$ and their directions of travel make an angle $\theta$ with each other. Find the **threshold** condition relating $E_1$, $E_2$, $\theta$, and the electron mass $m_e$ for the process to be possible.

**(c)** As a special case, two photons of equal energy $E$ collide head-on ($\theta = \pi$). Find the minimum $E$ for pair production. This is the process by which a high-energy gamma ray is absorbed by the cosmic background of soft photons.

**Recall:**

![[Def - The Four-Momentum of a Photon#The Definition]]

![[Thm - Conservation of Four-Momentum#Statement]]

A photon has a **null** four-momentum, $P_\gamma\cdot P_\gamma = 0$. An electron or positron has rest mass $m_e$ and four-momentum with $P\cdot P = m_e^2c^2$. The invariant mass squared of a system is $(\sum P)\cdot(\sum P)$, the same in every frame.

---

# Convergent Strategy

**Problem class.** Part (a) is an *impossibility* argument; parts (b) and (c) are *threshold* problems. Both are governed by the invariant mass of the system.

**Assumption pattern.** The decisive quantity is the invariant mass squared $(\sum P)^2$ of the photon system, set against the invariant mass of the would-be products. A single photon has $(\sum P)^2 = 0$; an $e^+e^-$ pair has $(\sum P)^2 \ge (2m_e)^2c^2 > 0$. The mismatch is the whole of part (a).

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] equates the total four-momentum before and after; therefore the invariant mass squared $(\sum P)^2$ is conserved. For (a), compute $(\sum P)^2$ for one photon (zero) and for a pair (positive) — they cannot match. For (b), compute $(P_1+P_2)^2$ for the two photons and require it to reach the minimum invariant mass $(2m_e)^2c^2$ of the pair (products at rest in the centre-of-momentum frame).

**Key decision point.** The unifying insight is that **the invariant mass of a system is conserved and is the gatekeeper**: a single photon has invariant mass zero, a massive pair has invariant mass at least $2m_e$, and no process can change a conserved quantity from zero to nonzero. For (b), the photons' nullity makes $(P_1+P_2)^2 = 2P_1\cdot P_2$, a single clean inner product.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — conservation of four-momentum.
2. **Square a four-momentum to extract an invariant mass** — $(\sum P)^2$ is the invariant mass squared.
3. **Use the photon's null four-momentum** — $P_\gamma\cdot P_\gamma = 0$ for each photon.
4. **Go to the centre-of-momentum frame** — where, at threshold, the pair is at rest.

---

# Hints

> [!note]- Hint 1
> The invariant mass squared of a system, $(\sum P)\cdot(\sum P)$, is conserved (it is the square of the conserved total four-momentum) and is the *same in every frame*. Compute it for a single photon. Compute it for an electron–positron pair. Can they be equal?

> [!note]- Hint 2
> A single photon has $(\sum P)^2 = P_\gamma\cdot P_\gamma = 0$. An $e^+e^-$ pair has $(\sum P)^2 = (P_+ + P_-)^2 \ge (2m_ec)^2 > 0$ — strictly positive, because the pair has positive invariant mass. A conserved quantity cannot go from $0$ to positive.

> [!note]- Hint 3
> For two photons, $(P_1+P_2)^2 = P_1^2 + P_2^2 + 2P_1\cdot P_2 = 0 + 0 + 2P_1\cdot P_2$ — the nullity deletes the self-terms. Compute $P_1\cdot P_2$ in the lab frame from $P_i = (E_i/c)(1,\mathbf{e}_i)$ with $\mathbf{e}_1\cdot\mathbf{e}_2 = \cos\theta$.

> [!note]- Hint 4
> Threshold: the invariant mass squared of the photon system must reach the *minimum* invariant mass squared of the pair, which is $(2m_ec)^2$ (the pair at rest in the centre-of-momentum frame). Set $2P_1\cdot P_2 = (2m_ec)^2$.

---

# Solution

The governing quantity throughout is the invariant mass squared $(\sum P)^2$ of the photon system. A single photon has invariant mass zero; a massive pair has invariant mass at least $2m_e$; since the invariant mass is conserved, one photon cannot become a pair. Two photons *can* carry nonzero invariant mass, and the threshold is where it reaches $2m_e$.

**Step 1: A single photon cannot pair-produce (part a).**

The invariant mass squared of a single photon is $0$; that of an $e^+e^-$ pair is at least $(2m_ec)^2 > 0$. A conserved quantity cannot change from zero to positive, so $\gamma\not\to e^+e^-$.

> [!note]- Derivation
> Suppose, for contradiction, that a single photon of four-momentum $P_\gamma$ decayed into an electron and a positron with four-momenta $P_+$ and $P_-$. [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] would require
> $$P_\gamma = P_+ + P_-.$$
> Take the Minkowski square of both sides. The squared quantity is the invariant mass squared of the system, the *same in every frame*. On the left,
> $$P_\gamma\cdot P_\gamma = 0,$$
> because a photon has a [[Def - The Four-Momentum of a Photon|null four-momentum]]. On the right,
> $$(P_+ + P_-)^2 = P_+\cdot P_+ + P_-\cdot P_- + 2P_+\cdot P_- = m_e^2c^2 + m_e^2c^2 + 2P_+\cdot P_-.$$
> Now, for any two future-pointing timelike four-momenta of massive particles, $P_+\cdot P_- \ge m_e\cdot m_e\,c^2 = m_e^2c^2$, with equality only if the two particles have the same four-velocity (are mutually at rest). [To see this: evaluate $P_+\cdot P_-$ in the rest frame of the positron, where $P_+ = (m_ec,\mathbf{0})$ and $P_- = (E_-/c,\mathbf{p}_-)$, giving $P_+\cdot P_- = m_eE_- \ge m_e\cdot m_ec^2$ since $E_-\ge m_ec^2$.] Hence
> $$(P_+ + P_-)^2 = 2m_e^2c^2 + 2P_+\cdot P_- \ge 2m_e^2c^2 + 2m_e^2c^2 = (2m_ec)^2 > 0.$$
> So conservation of four-momentum would demand $0 = (P_+ + P_-)^2 \ge (2m_ec)^2 > 0$, a contradiction. **A single photon in vacuum cannot produce an $e^+e^-$ pair**, however energetic it is.
>
> The physical content: the invariant mass of the system is conserved, a single photon has invariant mass zero (it is massless), an $e^+e^-$ pair has invariant mass at least $2m_e$, and a conserved quantity cannot jump from zero to positive. Equivalently — a photon has no rest frame, but an $e^+e^-$ pair always has a centre-of-momentum frame in which it is at rest, and no boost turns a frame-less object into one with a rest frame. (Pair production *does* occur near an atomic nucleus: the nucleus absorbs the excess momentum, so the relevant system is photon-plus-nucleus, whose invariant mass is not zero.)

**Step 2: Two photons — the invariant mass of the pair (part b).**

For two photons, $(P_1+P_2)^2 = 2P_1\cdot P_2 = \dfrac{2E_1E_2}{c^2}(1-\cos\theta)$.

> [!note]- Derivation
> Two photons can carry nonzero invariant mass. Their four-momenta are
> $$P_1 = \frac{E_1}{c}(1,\mathbf{e}_1), \qquad P_2 = \frac{E_2}{c}(1,\mathbf{e}_2), \qquad \mathbf{e}_1\cdot\mathbf{e}_2 = \cos\theta.$$
> The invariant mass squared of the two-photon system is
> $$(P_1 + P_2)^2 = \underbrace{P_1\cdot P_1}_{0} + \underbrace{P_2\cdot P_2}_{0} + 2P_1\cdot P_2 = 2P_1\cdot P_2,$$
> the photon self-terms vanishing by nullity. The cross term is
> $$P_1\cdot P_2 = \frac{E_1}{c}\cdot\frac{E_2}{c}\big(1\cdot 1 - \mathbf{e}_1\cdot\mathbf{e}_2\big) = \frac{E_1E_2}{c^2}(1-\cos\theta).$$
> Hence the two-photon system has invariant mass squared
> $$(P_1+P_2)^2 = \frac{2E_1E_2}{c^2}(1-\cos\theta).$$
> This is positive whenever the photons are not collinear ($\theta\neq 0$): two non-parallel photons together constitute a system with nonzero invariant mass, even though each photon is massless. (Two *parallel* photons, $\theta = 0$, have $(P_1+P_2)^2 = 0$ — collectively still massless — which is why they, like a single photon, cannot pair-produce.)

**Step 3: The threshold condition (part b, continued).**

The process is possible iff $E_1E_2(1-\cos\theta) \ge 2m_e^2c^4$.

> [!note]- Derivation
> By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], the invariant mass squared of the photon system equals that of the produced pair:
> $$(P_1+P_2)^2 = (P_+ + P_-)^2.$$
> From Step 1, the pair's invariant mass squared satisfies $(P_+ + P_-)^2 \ge (2m_ec)^2$, with equality at **threshold**, when the electron and positron are at rest in the centre-of-momentum frame. So the process can occur if and only if the photon system carries *at least* this much invariant mass:
> $$(P_1+P_2)^2 \ge (2m_ec)^2.$$
> Using the result of Step 2:
> $$\frac{2E_1E_2}{c^2}(1-\cos\theta) \ge 4m_e^2c^2 \;\Longrightarrow\; \boxed{\;E_1 E_2\,(1-\cos\theta) \ge 2\,m_e^2c^4\;}$$
> This is the threshold condition. Note it depends on the *product* of the photon energies and on the collision angle, but not on the individual energies separately — a low-energy photon can pair-produce off a high-energy one, provided the product is large enough.

**Step 4: Head-on equal-energy collision (part c).**

For $\theta = \pi$, $E_1 = E_2 = E$: the threshold is $E \ge m_ec^2$.

> [!note]- Derivation
> Head-on, $\theta = \pi$, so $1-\cos\theta = 2$; equal energies, $E_1 = E_2 = E$. The threshold condition $E_1E_2(1-\cos\theta)\ge 2m_e^2c^4$ becomes
> $$E\cdot E\cdot 2 \ge 2m_e^2c^4 \;\Longrightarrow\; E^2 \ge m_e^2c^4 \;\Longrightarrow\; E \ge m_ec^2.$$
> Each photon must carry at least the rest energy of one electron, $m_ec^2 \approx 0.511$ MeV. This makes sense: head-on, in the centre-of-momentum frame (which is the lab frame here, by symmetry), the two photons share their energy equally with the pair, and at threshold each photon's energy becomes exactly one particle's rest energy.
>
> This is the mechanism of **gamma-ray absorption by background light**. A very high-energy gamma ray ($E_1$ large) travelling through space collides with a low-energy background photon ($E_2$ small — a photon of the cosmic microwave background, or of starlight). The threshold $E_1E_2(1-\cos\theta)\ge 2m_e^2c^4$ shows that even a tiny $E_2$ suffices if $E_1$ is large enough: the universe is opaque to sufficiently energetic gamma rays, because they pair-produce off the ambient photon bath. This sets an effective horizon for gamma-ray astronomy.

> [!note]- Complete formal solution
> **(a)** If $\gamma\to e^+e^-$ were possible, conservation of four-momentum gives $P_\gamma = P_+ + P_-$. Squaring: $0 = P_\gamma^2 = (P_++P_-)^2 = 2m_e^2c^2 + 2P_+\cdot P_-$. But $P_+\cdot P_-\ge m_e^2c^2$ for two massive particles, so $(P_++P_-)^2\ge(2m_ec)^2>0$, contradicting $P_\gamma^2 = 0$. A single photon cannot pair-produce.
>
> **(b)** For two photons, $P_i = (E_i/c)(1,\mathbf{e}_i)$, $\mathbf{e}_1\cdot\mathbf{e}_2=\cos\theta$:
> $$(P_1+P_2)^2 = 2P_1\cdot P_2 = \frac{2E_1E_2}{c^2}(1-\cos\theta).$$
> Conservation of four-momentum equates this to the pair's invariant mass squared, which is at least $(2m_ec)^2$. Threshold:
> $$\frac{2E_1E_2}{c^2}(1-\cos\theta)\ge 4m_e^2c^2 \;\Longrightarrow\; E_1E_2(1-\cos\theta)\ge 2m_e^2c^4.$$
>
> **(c)** $\theta=\pi$, $E_1=E_2=E$: $\;2E^2\ge 2m_e^2c^4\Rightarrow E\ge m_ec^2\approx 0.511$ MeV. $\blacksquare$

---

# Key Takeaways

**The invariant mass of a system is conserved, and it is the gatekeeper of every reaction.** Part (a) is settled in three lines because the invariant mass squared $(\sum P)^2$ is a conserved quantity — it is the square of the conserved total four-momentum — and it is a Lorentz scalar, the same in every frame. A single photon has invariant mass zero; an electron–positron pair has invariant mass at least $2m_e$; nothing can change a conserved quantity from zero to positive. This is the cleanest possible impossibility argument, and it generalises: to decide whether a process $A\to B + C + \cdots$ is *kinematically* allowed, compute the invariant mass of the initial state and of the final state, and check that the initial invariant mass is at least the sum of the final rest masses. The invariant mass is to relativistic reactions what the determinant is to linear maps — a single number that decides feasibility.

**A photon's nullity collapses the algebra; a system of photons can still be massive.** When the two-photon invariant mass $(P_1+P_2)^2$ is expanded, the self-terms $P_1^2$ and $P_2^2$ vanish because each photon is null, leaving the single clean cross term $2P_1\cdot P_2$. Yet — and this is the subtle point — that cross term is *positive* for non-parallel photons, so two massless photons together form a system with nonzero invariant mass. Mass is the Minkowski length of the *total* four-momentum, and the sum of two null vectors pointing in different directions is timelike. This is the sharpest illustration of the non-additivity of mass: $0 + 0 \neq 0$ for invariant masses when the constituents move. The trigger lesson: never sum rest masses; always sum four-momenta and take the length of the sum.

**Threshold means the products at rest in the centre-of-momentum frame, and the invariant mass is computed wherever it is easiest.** The threshold condition $E_1E_2(1-\cos\theta)\ge 2m_e^2c^4$ comes from setting the photon system's invariant mass equal to the *minimum* invariant mass of the pair, $(2m_e c)^2$, which is realised when the electron and positron are at rest in their centre-of-momentum frame. The computation evaluates one invariant — $(\sum P)^2$ — in the frame where the photon kinematics are given, and equates it to the same invariant in the frame where the threshold condition is simple. This is identical in spirit to [[Ex - Threshold energy for particle production|the particle-production threshold]]: the recurring method for every threshold problem is *invariant mass of the initial state, evaluated in the convenient frame, set equal to the total rest mass of the products*. The physical pay-off here — that energetic gamma rays are absorbed by the ambient photon bath, making the universe opaque to them — is a direct astrophysical consequence of one squared four-vector equation.
