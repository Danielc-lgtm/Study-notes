---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Motion of a Charge in a Uniform Field"
  - "Def - The Lorentz Four-Force"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

A charged particle, starting from rest, is accelerated by a uniform electric field $\mathbf{E}$ (no magnetic field) over a displacement $z$ along $\mathbf{E}$.

1. From the power equation $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$, show that the kinetic energy gained is $\mathfrak{E}_{\mathrm{kin}} = qEz = q\,\Delta V$, where $\Delta V$ is the potential difference traversed — *identical in form to the non-relativistic result*.
2. Show that this energy comes entirely from the electric field, and that adding any magnetic field would not change it (the magnetic field does no work).
3. For a potential difference $\Delta V = 10^6\,$V, compute the Lorentz factor $\Gamma_{\mathcal{P}}$ and speed reached by (a) an electron (rest energy $0.511\,$MeV) and (b) a proton (rest energy $938\,$MeV).
4. Explain, using parts 1–3, why electrostatic and linear accelerators easily bring electrons to relativistic speeds but require many stages (or very high voltage) for protons — and why a single electrostatic gap is limited to $|\Delta V|\lesssim10^7\,$V.

**Recall:**

![[Def - The Lorentz Four-Force#The Definition]]

The relativistic kinetic energy is $\mathfrak{E}_{\mathrm{kin}} = (\Gamma_{\mathcal{P}} - 1)mc^2$ (see [[Thm - Mass-Energy Equivalence]]), with $\Gamma_{\mathcal{P}} = (1 - V^2/c^2)^{-1/2}$. For a uniform electric field, $Ez = V(0) - V(z) = \Delta V$, the potential difference. The magnetic field does no work: $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$.

---

# Convergent Strategy

**Problem class.** An *energy-accounting* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.3]]: compute the kinetic energy a charge gains from an electric field and the resulting Lorentz factor. The routine is to integrate the power equation and apply the kinetic-energy relation.

**Assumption pattern.** A pure electric field accelerating a particle from rest. The assumption "from rest" makes the energy gain the full kinetic energy; the assumption "pure electric field" means all the energy comes from $\mathbf{E}$ (no magnetic contribution). The signpost is that the energy gain $q\Delta V$ is *identical* to the non-relativistic formula — the relativity is hidden in the relation between energy and speed, not in the energy gain itself.

**Theorem routing.** Part 1 routes through the [[Def - The Lorentz Four-Force|power equation]] $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$ to $\mathfrak{E}_{\mathrm{kin}} = qEz$. Part 2 uses the magnetic-field-does-no-work corollary. Part 3 routes through the [[Thm - Mass-Energy Equivalence|kinetic-energy relation]] $\mathfrak{E}_{\mathrm{kin}} = (\Gamma - 1)mc^2$. Part 4 is interpretive.

**Key decision point.** The non-obvious point is that the energy gain $\mathfrak{E}_{\mathrm{kin}} = q\Delta V$ is *exactly* the non-relativistic formula, with no relativistic correction — the relativity enters only when converting energy to speed via $\mathfrak{E}_{\mathrm{kin}} = (\Gamma - 1)mc^2$. The temptation is to look for a relativistic modification of the energy gain; there is none, and recognising this cleanly separates the two regimes.

---

# Legal Operations Used

1. **Operation 7 (use that the magnetic field does no work)** from the topic page: the energy comes entirely from $\mathbf{E}$, $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$. This is parts 1 and 2.

2. **Operation 6 (write the equation of motion)** from the topic page: the hyperbolic motion in a pure electric field underlies the energy gain. This supports part 1.

---

# Hints

> [!note]- Hint 1
> Integrate $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$ over the path: $\mathfrak{E}_{\mathrm{kin}} = \int q\mathbf{E}\cdot\mathbf{V}\,dt = q\int\mathbf{E}\cdot d\mathbf{x} = qEz$ (for uniform $\mathbf{E}$ along the displacement $z$). And $Ez = \Delta V$, the potential difference.

> [!note]- Hint 2
> A magnetic force $q\mathbf{V}\times\mathbf{B}$ is perpendicular to $\mathbf{V}$, so it contributes zero to $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$. The energy gain depends only on $\mathbf{E}$ and the displacement along it — adding $\mathbf{B}$ changes the path but not the energy gained over a given potential drop.

> [!note]- Hint 3
> Set $\mathfrak{E}_{\mathrm{kin}} = q\Delta V = e\times10^6\,\text{V} = 10^6\,$eV $= 1\,$MeV. Then $(\Gamma_{\mathcal{P}} - 1)mc^2 = 1\,$MeV, so $\Gamma_{\mathcal{P}} = 1 + 1\,\text{MeV}/(mc^2)$. For the electron, $mc^2 = 0.511\,$MeV, so $\Gamma \approx 2.96$; for the proton, $mc^2 = 938\,$MeV, so $\Gamma \approx 1.001$.

> [!note]- Hint 4
> The electron reaches $\Gamma\approx3$ ($V\approx0.94c$) from a single MV — easily relativistic. The proton barely moves ($\Gamma\approx1.001$, $V\approx0.046c$) — it needs $\sim10^3$ times more voltage to go relativistic. A single gap is limited to $\sim10^7\,$V by electrical breakdown (sparks); to go higher, many gaps in series (a linac) are used.

---

# Solution

The plan: integrate the power equation to get $\mathfrak{E}_{\mathrm{kin}} = qEz = q\Delta V$ (Step 1), confirm the energy is electric-only (Step 2), convert to Lorentz factors for electron and proton (Step 3), and interpret the accelerator design consequences (Step 4). The pivotal point is that the energy gain is the non-relativistic formula, with relativity hidden in the energy–speed relation.

**Step 1: The energy gain is $q\Delta V$.**

> [!note]- Derivation
> The power delivered to the particle is $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$ ([[Def - The Lorentz Four-Force|Lorentz four-force]], temporal component). Integrating over the trajectory, with $\mathbf{V} = d\mathbf{x}/dt$:
> $$\mathfrak{E}_{\mathrm{kin}} = \int \frac{d\mathfrak{E}}{dt}\,dt = \int q\,\mathbf{E}\cdot\mathbf{V}\,dt = q\int\mathbf{E}\cdot d\mathbf{x}.$$
> For a uniform field $\mathbf{E}$ and a displacement $z$ along it, $\int\mathbf{E}\cdot d\mathbf{x} = Ez$, so
> $$\mathfrak{E}_{\mathrm{kin}} = qEz = q\,\Delta V,$$
> where $\Delta V = V(0) - V(z) = Ez$ is the potential difference traversed. (This also follows directly from the hyperbolic-motion solution: $\mathfrak{E}_{\mathrm{kin}} = (\Gamma_{\mathcal{P}} - 1)mc^2 = qEz$ with $\Gamma_{\mathcal{P}} = \cosh(qE\tau/mc)$ and $az = \cosh - 1$.) **This is exactly the non-relativistic formula** $\mathfrak{E}_{\mathrm{kin}} = q\Delta V$ — the energy gained equals charge times potential drop, with no relativistic correction. The relativity is entirely in the *relation* between $\mathfrak{E}_{\mathrm{kin}}$ and the speed, not in the energy gain.

**Step 2: The energy is electric-only.**

> [!note]- Derivation
> The power equation $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$ contains *only* the electric field. A magnetic force $q\mathbf{V}\times\mathbf{B}$ is perpendicular to $\mathbf{V}$, so $\mathbf{V}\cdot(\mathbf{V}\times\mathbf{B}) = 0$ and the magnetic field contributes nothing to the energy. Therefore: adding a magnetic field to the accelerating region changes the *path* the particle takes (it bends) but not the *energy* it gains over a given potential drop. The energy gain depends only on the work done by $\mathbf{E}$, which is $q\Delta V$ regardless of any magnetic field present. This is why accelerators put the accelerating electric field in gaps and use magnetic fields only to steer the beam back through those gaps — the magnets cost no energy, the electric gaps deliver all of it.

**Step 3: Lorentz factors for electron and proton.**

> [!note]- Derivation
> Set $\mathfrak{E}_{\mathrm{kin}} = q\Delta V = e\times10^6\,\text{V} = 1\,\text{MeV}$. From $\mathfrak{E}_{\mathrm{kin}} = (\Gamma_{\mathcal{P}} - 1)mc^2$,
> $$\Gamma_{\mathcal{P}} = 1 + \frac{\mathfrak{E}_{\mathrm{kin}}}{mc^2} = 1 + \frac{1\,\text{MeV}}{mc^2}.$$
> **(a) Electron** ($mc^2 = 0.511\,$MeV): $\Gamma_{\mathcal{P}} = 1 + 1/0.511 \approx 2.96$. The speed: $V = c\sqrt{1 - 1/\Gamma^2} = c\sqrt{1 - 1/8.76} \approx 0.94\,c$. The electron is firmly relativistic after a single MV.
>
> **(b) Proton** ($mc^2 = 938\,$MeV): $\Gamma_{\mathcal{P}} = 1 + 1/938 \approx 1.0011$. The speed: $V = c\sqrt{1 - 1/\Gamma^2} \approx c\sqrt{2\times0.0011} \approx 0.046\,c$. The proton is barely moving — essentially non-relativistic.
>
> The same 1 MeV makes the electron ultrarelativistic and leaves the proton crawling, because the kinetic energy is compared to the rest energy, and the proton's is $\sim1800$ times larger.

**Step 4: Accelerator design consequences.**

> [!note]- Derivation
> The contrast in Step 3 is the reason electrons and protons are accelerated differently. **Electrons**, with rest energy only $0.511\,$MeV, reach relativistic speeds ($\Gamma\sim3$, $V\sim0.94c$) from a single megavolt — electrostatic accelerators and short linacs suffice to make them relativistic. **Protons**, with rest energy $938\,$MeV, need $\sim10^3$ times more voltage to reach comparable $\Gamma$ — a single gap cannot do it.
>
> A single electrostatic gap is limited to $|\Delta V|\lesssim10^7\,$V by **electrical breakdown**: above this, the field ionises residual gas or sparks across insulators. To exceed $\sim10\,$MeV one chains many gaps in series, each adding $q\Delta V$, with a radio-frequency field synchronised to the particle's arrival at each gap — this is the **linac** (linear accelerator). SLAC's $3.2\,$km linac reaches $50\,$GeV for electrons by summing the potential drops of thousands of cavities; the total energy is $\sum q\Delta V_i$, the sum of the gap voltages. The reusable accounting: total kinetic energy equals charge times the *total* potential drop traversed, however many stages deliver it.

> [!note]- Complete formal solution
> Integrating $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$ over the path gives $\mathfrak{E}_{\mathrm{kin}} = q\int\mathbf{E}\cdot d\mathbf{x} = qEz = q\Delta V$, the non-relativistic formula (relativity is in the energy–speed relation, not the energy gain). The energy is electric-only: $q\mathbf{V}\times\mathbf{B}\perp\mathbf{V}$ contributes nothing, so $\mathbf{B}$ changes the path but not the energy. For $\Delta V = 10^6\,$V, $\mathfrak{E}_{\mathrm{kin}} = 1\,$MeV, giving $\Gamma = 1 + 1\,\text{MeV}/mc^2$: electron $\Gamma\approx2.96$ ($V\approx0.94c$), proton $\Gamma\approx1.001$ ($V\approx0.046c$). Electrons go relativistic from a single MV; protons need $\sim10^3$ times more. A single gap is breakdown-limited to $\lesssim10^7\,$V, so high energies use many gaps in series (a linac), total energy $\sum q\Delta V_i$. $\blacksquare$

---

# Key Takeaways

**The energy gain is $q\Delta V$, the non-relativistic formula — relativity is in the energy–speed relation.** The clean and slightly surprising result is that a charge accelerated through a potential difference gains kinetic energy $q\Delta V$ *exactly*, with no relativistic correction to the energy gain itself. This is because the work–energy theorem $\mathfrak{E}_{\mathrm{kin}} = q\int\mathbf{E}\cdot d\mathbf{x}$ holds unchanged relativistically (the temporal component of the four-force is the work rate). The relativity enters only when you convert that energy to a speed, via $\mathfrak{E}_{\mathrm{kin}} = (\Gamma - 1)mc^2$ — which is where the speed saturates at $c$ as energy grows. The reusable separation is: *energy gain is classical ($q\Delta V$); the energy-to-speed conversion is relativistic*. This is why "electron-volt" is the natural energy unit (a charge $e$ through $1\,$V gains $1\,$eV regardless of regime) and why accelerator energies are quoted in volts.

**Only the electric field does work — magnets steer, fields accelerate.** The energy comes entirely from $\mathbf{E}$ because the magnetic force is perpendicular to the velocity and contributes nothing to $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$. This single fact dictates the architecture of every accelerator: the energy is delivered in electric-field gaps, and magnetic fields only bend the beam (in a cyclotron, back through the gaps; in a synchrotron, around the ring). A magnetic field changes a particle's *direction* of motion but never its *speed* or *energy*. The reusable design principle, and the answer to "how do I add energy to a beam?", is always "with an electric field along the motion" — and the total energy is the sum of all the potential drops the particle traverses, $\sum q\Delta V_i$, however many stages deliver them. This is why the LHC, despite its enormous magnets, gets all its energy from radio-frequency cavities.

**Rest energy sets the scale: electrons go relativistic cheaply, protons expensively.** The factor of $\sim1800$ between the proton and electron rest energies means the same kinetic energy produces wildly different $\Gamma$: a single MeV makes an electron ultrarelativistic ($\Gamma\approx3$) but barely stirs a proton ($\Gamma\approx1.001$). This is why the two species are accelerated by different machines — electrons by linacs and electrostatic accelerators (relativistic from a few MV), protons by long chains of stages or large synchrotrons (GeV needed for relativistic motion). It is also why electron synchrotrons hit a radiation wall (synchrotron radiation scales as $\Gamma^4$) while proton synchrotrons do not until far higher energy. The reusable diagnostic is to always compare the kinetic energy to the rest energy $mc^2$: $\mathfrak{E}_{\mathrm{kin}}\ll mc^2$ is non-relativistic, $\gg mc^2$ is ultrarelativistic, and the ratio is exactly $\Gamma - 1$.
