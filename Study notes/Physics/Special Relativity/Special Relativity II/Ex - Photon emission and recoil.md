---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

An atom of rest mass $M$, **at rest** in some inertial frame, is in an excited state. It de-excites by emitting a single photon, and in doing so its rest mass drops to $M'$ (the internal energy released is $\Delta E = (M - M')c^2$, the energy gap between the two atomic levels). The atom recoils.

**(a)** Using conservation of four-momentum, find the energy $E_\gamma$ of the emitted photon exactly, in terms of $M$, $M'$, and $c$.

**(b)** Show that the photon energy is slightly *less* than the level gap $\Delta E = (M-M')c^2$, and identify the shortfall as the **recoil kinetic energy** of the atom. Express the fractional shortfall and show it is of order $\Delta E/Mc^2$.

**(c)** Why does this recoil shift matter for the **Mössbauer effect** and for resonant absorption of photons by atoms?

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - The Four-Momentum of a Photon#The Definition]]

A photon has a null four-momentum, $P_\gamma\cdot P_\gamma = 0$, with $E_\gamma = |\mathbf{p}_\gamma|c$. The atom before and after has [[Def - Four-Momentum and Rest Mass|four-momentum]] satisfying $P\cdot P = (\text{rest mass})^2c^2$.

---

# Convergent Strategy

**Problem class.** This is a *two-body decay* into a massive particle and a photon — a decay-kinematics problem, structurally identical to [[Ex - Two-body decay kinematics]] but with one product massless.

**Assumption pattern.** The parent atom is at rest, so its four-momentum is $(Mc,\mathbf{0})$. There are two products — the recoiling atom (rest mass $M'$) and the photon (massless). The recoiling atom's detailed motion is a nuisance; we want only the photon energy.

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]]: $P_{\text{atom}} = P'_{\text{atom}} + P_\gamma$. Isolate the recoiling atom, $P'_{\text{atom}} = P_{\text{atom}} - P_\gamma$, and square; the left becomes the known $M'^2c^2$, the photon's self-term vanishes ($P_\gamma\cdot P_\gamma = 0$), leaving a linear equation for $E_\gamma$.

**Key decision point.** As in two-body decay: isolate the four-momentum you do not want — the recoil atom — and square. The photon's nullity simplifies the algebra. The conceptual punchline is in the *interpretation*: the photon does not carry the full level gap because momentum conservation forces the atom to recoil, and the recoil kinetic energy is subtracted from the photon.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — $P_{\text{atom}} = P'_{\text{atom}} + P_\gamma$.
2. **Go to the rest frame of a chosen particle** — the initial atom's rest frame, $P_{\text{atom}} = (Mc,\mathbf{0})$.
3. **Square a four-momentum to extract an invariant mass** — squaring the isolated recoil atom gives $M'^2c^2$.
4. **Use the photon's null four-momentum** — $P_\gamma\cdot P_\gamma = 0$.

---

# Hints

> [!note]- Hint 1
> You want the photon energy, not the recoil atom's motion. Isolate the recoil atom's four-momentum and square it away — exactly as in two-body decay.

> [!note]- Hint 2
> Conservation of four-momentum in the atom's rest frame: $P_{\text{atom}} = P'_{\text{atom}} + P_\gamma$, with $P_{\text{atom}} = (Mc,\mathbf{0})$. Isolate: $P'_{\text{atom}} = P_{\text{atom}} - P_\gamma$.

> [!note]- Hint 3
> Square: $M'^2c^2 = P'_{\text{atom}}\cdot P'_{\text{atom}} = (P_{\text{atom}} - P_\gamma)^2 = M^2c^2 + 0 - 2P_{\text{atom}}\cdot P_\gamma$. The photon self-term is zero.

> [!note]- Hint 4
> In the atom's rest frame, $P_{\text{atom}}\cdot P_\gamma = Mc\cdot(E_\gamma/c) = ME_\gamma$. Solve $M'^2c^2 = M^2c^2 - 2ME_\gamma$ for $E_\gamma$. Then compare $E_\gamma$ with $(M-M')c^2$.

---

# Solution

This is a two-body decay with one massless product. Isolating the recoil atom and squaring it away gives the photon energy exactly. The result is slightly below the naive level gap, and the difference is precisely the kinetic energy of the recoiling atom.

**Step 1: Conservation of four-momentum and the photon energy (part a).**

Squaring the isolated recoil-atom four-momentum gives $E_\gamma = \dfrac{(M^2 - M'^2)c^2}{2M}$.

> [!note]- Derivation
> In the rest frame of the initial atom, [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] reads
> $$P_{\text{atom}} = P'_{\text{atom}} + P_\gamma,$$
> with $P_{\text{atom}} = (Mc,\mathbf{0})$ the initial atom (at rest, rest mass $M$), $P'_{\text{atom}}$ the recoiling atom (rest mass $M'$), and $P_\gamma$ the photon.
>
> We want $E_\gamma$, not the recoil atom's motion, so isolate the recoil atom:
> $$P'_{\text{atom}} = P_{\text{atom}} - P_\gamma.$$
> Square both sides:
> $$P'_{\text{atom}}\cdot P'_{\text{atom}} = (P_{\text{atom}} - P_\gamma)^2 = P_{\text{atom}}\cdot P_{\text{atom}} - 2P_{\text{atom}}\cdot P_\gamma + P_\gamma\cdot P_\gamma.$$
> Use the mass shells: $P'_{\text{atom}}\cdot P'_{\text{atom}} = M'^2c^2$, $P_{\text{atom}}\cdot P_{\text{atom}} = M^2c^2$, and $P_\gamma\cdot P_\gamma = 0$ (the photon is [[Def - The Four-Momentum of a Photon|null]]). The cross term, in the rest frame where $P_{\text{atom}} = (Mc,\mathbf{0})$ and $P_\gamma = (E_\gamma/c,\mathbf{p}_\gamma)$:
> $$P_{\text{atom}}\cdot P_\gamma = (Mc)\Big(\frac{E_\gamma}{c}\Big) - \mathbf{0}\cdot\mathbf{p}_\gamma = M E_\gamma.$$
> So the squared equation is
> $$M'^2c^2 = M^2c^2 - 2ME_\gamma,$$
> linear in $E_\gamma$. Solving,
> $$\boxed{\;E_\gamma = \frac{(M^2 - M'^2)c^2}{2M}\;}$$
> This is the exact photon energy. (It is the massless-product limit of the [[Ex - Two-body decay kinematics|two-body decay]] formula $E_2 = (M^2+m_2^2-m_3^2)c^2/2M$ with $m_2 = 0$, $m_3 = M'$.)

**Step 2: The photon energy is below the level gap (part b).**

Writing $E_\gamma = \Delta E\big(1 - \tfrac{\Delta E}{2Mc^2}\big)$, the photon carries slightly less than the gap $\Delta E = (M-M')c^2$; the shortfall is the recoil kinetic energy.

> [!note]- Derivation
> Factor the numerator of the exact result as a difference of squares:
> $$E_\gamma = \frac{(M-M')(M+M')c^2}{2M}.$$
> The naive expectation — ignoring recoil — is that the photon carries the full released internal energy, the level gap $\Delta E = (M-M')c^2$. Compare:
> $$E_\gamma = \frac{(M-M')(M+M')c^2}{2M} = (M-M')c^2\cdot\frac{M+M'}{2M} = \Delta E\cdot\frac{M+M'}{2M}.$$
> Since $M' < M$, the factor $(M+M')/2M < 1$, so
> $$E_\gamma < \Delta E.$$
> **The photon carries less than the level gap.** To see how much less, write $M' = M - \Delta E/c^2$, so $M + M' = 2M - \Delta E/c^2$ and
> $$\frac{M+M'}{2M} = 1 - \frac{\Delta E}{2Mc^2}, \qquad E_\gamma = \Delta E\Big(1 - \frac{\Delta E}{2Mc^2}\Big).$$
> The shortfall is
> $$\Delta E - E_\gamma = \frac{(\Delta E)^2}{2Mc^2}.$$
> This is exactly the **recoil kinetic energy** of the atom. To check: by conservation of momentum the recoiling atom carries momentum $|\mathbf{p}'| = |\mathbf{p}_\gamma| = E_\gamma/c \approx \Delta E/c$ (to leading order), so its kinetic energy is
> $$T_{\text{recoil}} \approx \frac{|\mathbf{p}'|^2}{2M} \approx \frac{(\Delta E/c)^2}{2M} = \frac{(\Delta E)^2}{2Mc^2},$$
> matching the shortfall. The energy released by the atom, $\Delta E$, is *shared*: most goes to the photon, but a sliver $(\Delta E)^2/2Mc^2$ goes into the kinetic energy of the recoiling atom, because momentum conservation forbids the atom from staying at rest. The fractional shortfall is
> $$\frac{\Delta E - E_\gamma}{\Delta E} = \frac{\Delta E}{2Mc^2},$$
> of order (level gap)/(atom rest energy) — typically minuscule, since atomic or nuclear level gaps are tiny compared with the rest energy of the whole atom.

**Step 3: Why the recoil shift matters — the Mössbauer effect (part c).**

> [!note]- Derivation
> Consider **resonant absorption**: an identical atom in its ground state should be able to absorb the photon and jump up to the excited state. But absorption is the time-reverse of emission, and it has its *own* recoil — the absorbing atom must take up the photon's momentum, so it needs the photon to supply the level gap $\Delta E$ *plus* the recoil kinetic energy $(\Delta E)^2/2Mc^2$.
>
> Now the trap. The emitted photon has energy $E_\gamma = \Delta E - (\Delta E)^2/2Mc^2$ — it is *short* of $\Delta E$ by the emission recoil. The absorbing atom needs $E_\gamma^{\text{abs}} = \Delta E + (\Delta E)^2/2Mc^2$ — it is *over* $\Delta E$ by the absorption recoil. The emitted photon is therefore short of the absorption requirement by twice the recoil energy,
> $$E_\gamma^{\text{abs}} - E_\gamma = \frac{(\Delta E)^2}{Mc^2}.$$
> If this gap exceeds the natural linewidth of the transition, the emitted photon simply *cannot* be resonantly absorbed by a like atom — emission and absorption lines are pulled apart by recoil. For nuclear gamma transitions, where $\Delta E$ is large (keV–MeV), the recoil shift is enormous compared with the linewidth, and naive resonant absorption fails entirely.
>
> The **Mössbauer effect** is the escape. If the emitting (or absorbing) atom is locked into a *crystal lattice*, then under the right conditions the *whole crystal* recoils, not the single atom. The recoil energy is $(\Delta E)^2/2Mc^2$ with $M$ now the mass of the entire crystal — astronomically larger than a single atom — so the shift becomes utterly negligible. Recoil-free emission and absorption are restored, and the gamma line becomes extraordinarily sharp. This is what makes the Mössbauer effect a precision tool: it was used to measure the gravitational redshift of photons over a $22.5$-metre tower (the Pound–Rebka experiment), a test of general relativity, precisely because the recoil-free line is narrow enough to resolve a shift of one part in $10^{15}$.

> [!note]- Complete formal solution
> In the initial atom's rest frame, conservation of four-momentum gives $P_{\text{atom}} = P'_{\text{atom}} + P_\gamma$ with $P_{\text{atom}} = (Mc,\mathbf{0})$. Isolate $P'_{\text{atom}} = P_{\text{atom}} - P_\gamma$ and square:
> $$M'^2c^2 = M^2c^2 + \underbrace{P_\gamma\cdot P_\gamma}_{0} - 2P_{\text{atom}}\cdot P_\gamma = M^2c^2 - 2ME_\gamma,$$
> using $P_{\text{atom}}\cdot P_\gamma = ME_\gamma$ in the rest frame. Hence
> $$E_\gamma = \frac{(M^2-M'^2)c^2}{2M} = \Delta E\Big(1 - \frac{\Delta E}{2Mc^2}\Big), \qquad \Delta E = (M-M')c^2.$$
> The photon energy is below the level gap by $\Delta E - E_\gamma = (\Delta E)^2/2Mc^2$, the recoil kinetic energy of the atom. Because emission falls short and absorption requires excess by the same recoil energy, resonant absorption by a free like atom fails by $(\Delta E)^2/Mc^2$; binding the atom in a crystal so the whole lattice recoils (the Mössbauer effect) makes $M$ macroscopic and the shift negligible. $\blacksquare$

---

# Key Takeaways

**A photon emitted by a recoiling source carries less than the energy released — momentum conservation taxes the photon.** The naive picture, that an atom dropping by an energy gap $\Delta E$ emits a photon of energy $\Delta E$, violates momentum conservation: the initial atom is at rest with zero momentum, the photon carries momentum $E_\gamma/c$, so the atom *must* recoil with equal and opposite momentum, and the recoil costs kinetic energy. That kinetic energy can only come from the released $\Delta E$, so the photon is shortchanged by $(\Delta E)^2/2Mc^2$. This is a completely general feature of emission by a free body — an atom, a nucleus, a molecule — and the trigger to remember it is "a body at rest emits a photon": the body cannot stay at rest, and the recoil energy is subtracted from the photon. The same logic, run forwards, taxes absorption.

**Isolate-and-square handles a two-body decay with a massless product exactly as with two massive products.** The technique is identical to [[Ex - Two-body decay kinematics|two-body decay]]: to find one product's energy, isolate the *other* product's four-momentum and square it into its known invariant mass squared. Here the "other product" is the recoil atom, squaring to $M'^2c^2$, and the wanted product is the photon. The photon's masslessness only makes the algebra shorter — its self-term $P_\gamma\cdot P_\gamma$ vanishes. The general lesson: massless and massive products are handled by exactly the same conservation-of-four-momentum machinery; a photon is just a particle with $P\cdot P = 0$, and the isolate-and-square method does not care whether the eliminated particle is massive or null.

**The recoil energy scales as $(\Delta E)^2/Mc^2$, and making $M$ macroscopic is the key to precision spectroscopy.** The fractional recoil shift is $\Delta E/2Mc^2$ — quadratic in the transition energy and inversely proportional to the recoiling mass. For optical atomic transitions ($\Delta E\sim$ eV) the shift is tiny; for nuclear gamma transitions ($\Delta E\sim$ keV–MeV) it is large enough to destroy resonant absorption entirely. The Mössbauer effect's insight is that the recoiling mass need not be a single atom: if the atom is bound rigidly in a crystal, the *whole crystal* absorbs the recoil, $M$ becomes Avogadro's number of atoms, and the shift vanishes. The resulting recoil-free, ultra-narrow gamma line is a frequency standard of extraordinary precision — sharp enough that the Pound–Rebka experiment used it to detect the gravitational redshift of light falling down a tower, confirming a prediction of general relativity. A single conservation-of-four-momentum calculation thus reaches from atomic physics to a precision test of gravity.
