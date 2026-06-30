---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Motion of a Charge in a Uniform Field"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

A synchrotron holds particles on a circular ring of *fixed* radius $R$ by a magnetic field perpendicular to the ring, while their momentum is increased by radio-frequency electric fields.

1. From the Larmor-radius relation, derive the condition $B = P/(qR)$ that the magnetic field must satisfy to keep a particle of momentum $P$ on the fixed radius $R$, and explain why the field must be *ramped up* as the particle accelerates.
2. Contrast the synchrotron ($B$ ramped, $R$ fixed) with the cyclotron ($B$ fixed, $R$ grows) and the synchrocyclotron ($B$ fixed, accelerating frequency ramped). Why does the synchrotron avoid the size limitation of the cyclotron?
3. The LHC accelerates protons to kinetic energy $\mathfrak{E}_{\mathrm{kin}} \simeq 7\,$TeV on a ring of circumference $27\,$km (radius $R = 27/(2\pi)\,$km $\approx 4.3\,$km). Treating the protons as ultrarelativistic ($P \simeq \mathfrak{E}/c$), compute the magnetic field $B$ needed to bend them on this radius.
4. Comment on why the actual LHC field is somewhat larger ($\sim8.3\,$T) than your estimate, and why such fields require superconducting magnets.

**Recall:**

![[Thm - Motion of a Charge in a Uniform Field#Statement]]

The Larmor radius of a particle of transverse momentum $P_\perp$ in a field $B$ is $R = P_\perp/(qB)$ (see [[Thm - Motion of a Charge in a Uniform Field]]); for motion in the plane perpendicular to $\mathbf{B}$, $P_\perp = P$. For an ultrarelativistic particle the [[Def - Four-Momentum and Rest Mass|momentum]] is $P \simeq \mathfrak{E}/c$ (since $\mathfrak{E} = \sqrt{P^2c^2 + m^2c^4} \approx Pc$ when $Pc \gg mc^2$).

---

# Convergent Strategy

**Problem class.** An *accelerator-design* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.3]]: find the magnetic field that holds a particle of given momentum on a fixed radius. The routine is to invert the Larmor-radius relation and apply ultrarelativistic kinematics.

**Assumption pattern.** A particle on a fixed-radius ring, with momentum increasing. The assumption "fixed radius" is the defining feature of a synchrotron, and it forces the field to track the momentum, $B = P/(qR)$. The ultrarelativistic assumption $P\simeq\mathfrak{E}/c$ simplifies the numerics. The signpost is "ramp the field as the particle accelerates".

**Theorem routing.** Part 1 routes through the [[Thm - Motion of a Charge in a Uniform Field|Larmor-radius relation]] $R = P/(qB)$, inverted to $B = P/(qR)$. Part 2 contrasts the three machine types. Part 3 routes through the ultrarelativistic [[Def - Four-Momentum and Rest Mass|momentum]] $P\simeq\mathfrak{E}/c$. Part 4 is interpretive.

**Key decision point.** The crucial recognition is that to keep $R$ *fixed* while $P$ grows, the field $B = P/(qR)$ must grow in lockstep — the synchrotron's defining trick, which decouples the machine size from the final energy (unlike the cyclotron, whose radius grows with momentum and whose magnet must therefore cover the whole spiral). The temptation is to treat the field as static; the synchrotron's whole point is that it is dynamic.

---

# Legal Operations Used

1. **Operation 8 (extract the cyclotron frequency and Larmor radius)** from the topic page: invert $R = P/(qB)$ to $B = P/(qR)$. This is part 1.

2. **Operation 6 (write the equation of motion)** from the topic page: the circular motion in a magnetic field underlies the radius relation. This supports part 1.

---

# Hints

> [!note]- Hint 1
> Rearrange $R = P/(qB)$ to $B = P/(qR)$. With $R$ held fixed, $B$ must increase in proportion to $P$ as the radio-frequency cavities raise the momentum — the field is "ramped" in synchrony with the acceleration (hence "synchrotron").

> [!note]- Hint 2
> In a cyclotron, $B$ is fixed so $R = P/(qB)$ grows with momentum — the particle spirals outward, and the magnet must cover the whole spiral, which becomes prohibitively large at high energy. A synchrotron fixes $R$ (the magnets are only a thin ring) and ramps $B$, so the machine size is set by the *final* radius alone.

> [!note]- Hint 3
> $P \simeq \mathfrak{E}/c = 7\,$TeV$/c$. Convert: $7\,\text{TeV} = 7\times10^{12}\times1.6\times10^{-19}\,\text{J} = 1.12\times10^{-6}\,$J, so $P = 1.12\times10^{-6}/(3\times10^8) = 3.73\times10^{-15}\,$kg·m/s. Then $B = P/(qR) = 3.73\times10^{-15}/((1.6\times10^{-19})(4.3\times10^3)) \approx 5.4\,$T.

> [!note]- Hint 4
> The LHC ring is not a perfect circle — it has straight sections (for the RF cavities, detectors, and focusing), so the bending magnets cover less than the full circumference and must bend more sharply (smaller effective radius), needing a larger field $\sim8.3\,$T. Fields this large over kilometres require superconducting magnets (no resistive heating), cooled to $1.9\,$K.

---

# Solution

The plan: invert the Larmor relation to get the field-ramp condition (Step 1), contrast the machine types (Step 2), compute the LHC field (Step 3), and explain the real-world corrections (Step 4). The pivotal idea is that fixing the radius forces the field to track the momentum, decoupling machine size from energy.

**Step 1: The field-ramp condition $B = P/(qR)$.**

> [!note]- Derivation
> A particle of momentum $P$ moving perpendicular to a magnetic field $B$ orbits at the [[Thm - Motion of a Charge in a Uniform Field|Larmor radius]] $R = P/(qB)$. To keep the particle on a *fixed* radius $R$ (the ring), invert this:
> $$B = \frac{P}{qR}.$$
> As the radio-frequency cavities increase the momentum $P$ during acceleration, the field $B$ must be **ramped up** in proportion — synchronously with the rising momentum, which is what gives the *synchrotron* its name. At injection (low $P$) the field is small; at full energy (high $P$) the field is maximal. The radius stays constant throughout, so the particles always orbit the same physical ring. The energy is delivered by the electric cavities (a magnetic field does no work); the magnets only steer, and their job is to keep $R$ fixed by tracking $P$.

**Step 2: Synchrotron versus cyclotron versus synchrocyclotron.**

> [!note]- Derivation
> - **Cyclotron** ($B$ fixed): from $R = P/(qB)$, the radius *grows* with momentum — the particle spirals outward. The magnet must cover the *entire* spiral, from centre to outer edge. At high energy the required momentum, hence radius, hence magnet size, becomes prohibitive (and the orbital frequency $\omega = \omega_B/\Gamma$ detunes, capping the energy anyway).
> - **Synchrocyclotron** ($B$ fixed, frequency ramped): keeps the cyclotron's growing-spiral geometry but ramps the accelerating frequency to follow $\omega = \omega_B/\Gamma$, overcoming the resonance detuning. It still has the size problem (the radius grows as $\Gamma V$), limiting it to a few hundred MeV.
> - **Synchrotron** ($B$ ramped, $R$ fixed): keeps the radius *constant* by ramping $B = P/(qR)$ in step with the momentum. The magnets form only a thin ring of fixed radius — no need to fill a disk. This **decouples the machine size from the final energy**: the ring radius is set by the final field and momentum, not by the whole acceleration history. This is why all the highest-energy machines (LHC, Tevatron) are synchrotrons — a $27\,$km ring of thin magnets is feasible; a $27\,$km-diameter solid magnet is not.

**Step 3: The LHC bending field.**

> [!note]- Derivation
> Treat the $7\,$TeV protons as ultrarelativistic, so $P \simeq \mathfrak{E}/c = \mathfrak{E}_{\mathrm{kin}}/c$ (since $\mathfrak{E}_{\mathrm{kin}} = 7\,$TeV $\gg m_pc^2 = 938\,$MeV). Convert the energy to SI:
> $$\mathfrak{E} = 7\,\text{TeV} = 7\times10^{12}\times1.602\times10^{-19}\,\text{J} = 1.12\times10^{-6}\,\text{J},$$
> $$P = \frac{\mathfrak{E}}{c} = \frac{1.12\times10^{-6}}{3.0\times10^8} = 3.74\times10^{-15}\,\text{kg·m/s}.$$
> The ring radius is $R = 27\,\text{km}/(2\pi) = 4.30\times10^3\,$m. The bending field is
> $$B = \frac{P}{qR} = \frac{3.74\times10^{-15}}{(1.602\times10^{-19})(4.30\times10^3)} \approx 5.4\,\text{T}.$$
> So an idealised circular LHC would need a $\sim5.4\,$T bending field — already far beyond ordinary electromagnets (which saturate around $2\,$T due to iron's magnetisation limit).

**Step 4: Why the real field is larger, and superconducting.**

> [!note]- Derivation
> The actual LHC dipole field is $\sim8.3\,$T, larger than the $5.4\,$T estimate, because the ring is *not* a perfect circle. It has long straight sections — for the radio-frequency cavities, the four big detectors (ATLAS, CMS, ALICE, LHCb), and the beam-focusing quadrupoles — where there is no bending. The bending dipoles therefore occupy only a fraction of the $27\,$km circumference (about two-thirds), so they must bend the beam *more sharply* over that fraction: the effective bending radius is smaller than $4.3\,$km, requiring a proportionally larger field, $B = P/(qR_{\text{eff}})\approx8.3\,$T.
>
> A field of $8.3\,$T over kilometres of beam pipe cannot be produced by resistive magnets: the current needed would dissipate gigawatts as ohmic heat. Instead the LHC uses **superconducting magnets** — niobium–titanium coils carrying enormous currents with *zero* resistance, hence no heating — cooled to $1.9\,$K by superfluid helium (colder than outer space). The superconductivity is what makes such high fields sustainable; it is the enabling technology of all the highest-energy synchrotrons. (The energy stored in the LHC magnetic field is enough that a sudden loss of superconductivity — a "quench" — must be managed carefully to avoid damage.)

> [!note]- Complete formal solution
> The Larmor relation $R = P/(qB)$, inverted, gives the synchrotron condition $B = P/(qR)$: to hold a fixed radius $R$ while the momentum $P$ rises, the field must be ramped up in proportion. This decouples machine size from energy (unlike the cyclotron, where $R = P/(qB)$ grows with momentum and the magnet must fill the spiral). For the LHC, ultrarelativistic protons have $P\simeq\mathfrak{E}/c = 7\,\text{TeV}/c = 3.74\times10^{-15}\,$kg·m/s; with $R = 27\,\text{km}/2\pi = 4.30\times10^3\,$m, $B = P/(qR)\approx5.4\,$T. The real field $\sim8.3\,$T is larger because straight sections (cavities, detectors, focusing) reduce the bending fraction, requiring sharper bends; such fields over kilometres demand superconducting magnets at $1.9\,$K. $\blacksquare$

---

# Key Takeaways

**Fixing the radius forces the field to track the momentum: $B = P/(qR)$.** The defining trick of the synchrotron is to hold the orbit radius constant while ramping the magnetic field in lockstep with the rising momentum, $B = P/(qR)$. This single relation — the inverted Larmor formula — is the design equation of every circular collider. Its consequence is profound: the machine size (the ring radius) is set by the *final* field and momentum, not by the acceleration history, so the magnets form only a thin ring rather than filling a disk as in a cyclotron. This decoupling of size from energy is why all the highest-energy machines are synchrotrons. The reusable insight is that "fixed geometry plus ramped field" beats "fixed field plus growing geometry" whenever the final energy is large, because the former economises on the most expensive component — the magnets.

**Ultrarelativistic kinematics simplifies the design numerics: $P\simeq\mathfrak{E}/c$.** For particles whose kinetic energy vastly exceeds their rest energy ($7\,$TeV versus $938\,$MeV for LHC protons), the momentum is essentially the energy over $c$, $P\simeq\mathfrak{E}/c$, because $\mathfrak{E} = \sqrt{P^2c^2 + m^2c^4}\approx Pc$. This collapses the field estimate to $B\approx\mathfrak{E}/(qcR)$, a clean relation between beam energy, ring radius, and bending field. The reusable approximation — drop the rest mass when $Pc\gg mc^2$ — is the standard simplification in high-energy accelerator and collision physics, and it is why TeV-scale machines are designed almost as if the particles were massless. The diagnostic is always to compare $Pc$ (or $\mathfrak{E}_{\mathrm{kin}}$) to $mc^2$: when the former dominates, the ultrarelativistic formulas apply.

**Real machines deviate from the ideal, and the corrections drive the technology.** The factor between the idealised $5.4\,$T and the real $8.3\,$T comes from a geometric reality — the ring has straight sections, so the bending magnets cover less than the full circumference and must bend more sharply. This pushes the field beyond what iron-core electromagnets can provide (they saturate near $2\,$T), forcing **superconducting magnets** cooled to $1.9\,$K, the enabling technology of the LHC and every modern high-field synchrotron. The reusable lesson is that the clean physics relation ($B = P/(qR)$) sets the scale, but the engineering realities (straight sections, magnet saturation, ohmic heating) determine the actual requirements — and those requirements, in turn, drive the development of the underlying technology. The progression from the cyclotron to the LHC is a story of relativistic kinematics meeting materials science, with the field-ramp relation at its heart.
