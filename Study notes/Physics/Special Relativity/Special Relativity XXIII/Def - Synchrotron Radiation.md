---
type: definition
subject: special-relativity
prereqs:
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Thm - Angular Distribution of Radiation"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ unless restored; signature mostly-minus. A charge $q$ of mass $m$ moves in a uniform magnetic field $\mathbf B$ (magnitude $B$), following a helix of pitch angle $\alpha$ (the angle between the velocity $\mathbf V$ and $\mathbf B$), radius $R = \Gamma m V\sin\alpha/(|q|B)$, with Lorentz factor $\Gamma = (1-V^2/c^2)^{-1/2}$. The **cyclotron (gyration) frequency** is $\omega_B = |q|B/m$, and the orbital (relativistic) angular frequency is $\omega_B/\Gamma$. The three-acceleration $\boldsymbol\gamma$ is centripetal, orthogonal to $\mathbf V$, with $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$. $\mathcal P$ denotes radiated power; $f_c$ the characteristic frequency; $\varepsilon_0$ the vacuum permittivity. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

---

# Axiom Motivation

A charge moving through a uniform magnetic field is bent into a helix — the magnetic Lorentz force is always perpendicular to the velocity, so it cannot change the speed but continually turns the direction. A turning velocity is an accelerating velocity, and by the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Larmor formula]] an accelerated charge radiates. So a charge in a magnetic field must radiate, and the radiation it emits — when the charge is relativistic — is called *synchrotron radiation*. The name is historical: it was first seen as an unwanted energy loss in synchrotron particle accelerators in the late 1940s, and only later recognised as both a powerful laboratory light source and the explanation for a vast amount of cosmic radio and X-ray emission. The concept to define is not a new physical law — it is the *specialisation* of the radiation formulas to the particular case of circular/helical motion, and the rich phenomenology (broad spectrum, sharp beaming, $\Gamma$-scalings) that this special case produces.

Why single out this case for its own name and treatment? Because circular motion is *qualitatively* different from linear acceleration in how it radiates, and the difference is exactly the difference between the parallel and perpendicular terms of the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Liénard formula]]. For acceleration *along* the velocity (a linear accelerator) the radiated power scales as $\Gamma^4$ at fixed applied force; for acceleration *perpendicular* to the velocity (circular motion) it scales as $\Gamma^2$ at fixed force but, crucially, the perpendicular acceleration needed to maintain a circular orbit *grows* with energy, and the net effect is a radiated power per orbit that scales as $\Gamma^4$. This single fact — that bending an ultrarelativistic charge is radiatively expensive — is the central organising idea, and it deserves its own page because it determines accelerator design and dominates non-thermal astrophysics.

The reason circular motion produces a *broad spectrum* rather than a single frequency is the most beautiful part, and it is worth motivating before stating. A slow charge in a magnetic field radiates at exactly one frequency, the cyclotron frequency $\omega_B$ — it traces a circle and emits like a rotating dipole, a pure tone. One might naively expect a relativistic charge to radiate at the (red-shifted) orbital frequency $\omega_B/\Gamma$. But relativistic beaming ([[Thm - Angular Distribution of Radiation|case iii]]) changes everything: the radiation is swept into a forward cone of half-angle $1/\Gamma$, so a distant observer is illuminated only during the brief instant the velocity sweeps past their line of sight — a fraction $1/\Gamma$ of each orbit. The observer thus receives not a smooth sinusoid but a sequence of short flashes, and a short flash, by Fourier's theorem, contains a *broad* band of frequencies extending far above the orbital frequency. The defining feature of synchrotron radiation — its enormous spectral width, from radio to X-rays — is a direct consequence of beaming, and any definition that omits this misses the point.

What the definition must *exclude* is the confusion with cyclotron radiation. At the non-relativistic limit ($V\ll c$, $\Gamma\to1$), synchrotron radiation degenerates into **cyclotron radiation**: monochromatic emission at the single cyclotron frequency $\omega_B$, with the symmetric dipole pattern of a slow rotating charge. The two are the same physical process — a charge radiating in a magnetic field — but they are phenomenologically distinct: cyclotron is narrow-band and isotropic-ish, synchrotron is broadband and tightly beamed. The boundary between them is the onset of relativistic beaming, i.e. $\Gamma$ departing appreciably from $1$. Calling cyclotron radiation "synchrotron" or vice versa erases the very feature — beaming — that makes synchrotron radiation useful and recognisable.

---

# The Definition

**Synchrotron radiation** is the electromagnetic radiation emitted by an ultrarelativistic charged particle moving in a magnetic field, i.e. the radiation of a charge whose [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|four-acceleration]] arises from the magnetic Lorentz force on a helical trajectory. Concretely, for a charge $q$ of mass $m$ in a uniform field $B$, moving with speed $V$ at pitch angle $\alpha$ and Lorentz factor $\Gamma$:

**Total radiated power** (from the Liénard formula with the centripetal acceleration $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$, $\boldsymbol\gamma\perp\mathbf V$):
$$
\boxed{\;\mathcal P \;=\; \frac{q^4 B^2 \Gamma^2 V^2\sin^2\alpha}{6\pi\varepsilon_0 c^3 m^2}\;}
$$

**Energy radiated per orbital revolution** (multiplying $\mathcal P$ by the period $2\pi\Gamma/\omega_B$):
$$
\Delta E \;=\; \frac{|q|^3 B\,\Gamma^3 V^2}{3\varepsilon_0 c^3 m} \;=\; \frac{q^2}{3\varepsilon_0 R}\left(\frac{V}{c}\right)^3\left(\frac{E}{mc^2}\right)^4,
$$
where $E = \Gamma mc^2$ is the particle energy and $R$ the orbit radius — exhibiting the decisive $\Gamma^4 \propto (E/mc^2)^4 \propto m^{-4}$ scaling.

**Spectrum.** The radiation is *not* monochromatic. Because the emission is beamed into a forward cone of half-angle $\sim 1/\Gamma$, a fixed observer receives short pulses of duration $\sim 1/(\Gamma^3\omega_B)$, whose Fourier content extends up to the **characteristic frequency**
$$
f_c \;=\; \Gamma^2\,\omega_B\sin\alpha \;=\; \Gamma^3\,\frac{c}{R}\sin^2\alpha,
$$
far above the orbital frequency $\omega_B/\Gamma$. The spectrum is broad, $f_c/f_s = 2\pi\Gamma^3\sin\alpha \gg 1$ relative to its lower bound $f_s = \omega_B/(2\pi\Gamma)$, extending from radio frequencies (for cosmic electrons) to hard X-rays (for storage-ring electrons). The characteristic photon energy is
$$
\varepsilon_c = h f_c = 12.4\left(\frac{\Gamma}{1000}\right)^3\left(\frac{100\,\text{m}}{R}\right)\,\text{eV}.
$$

**Non-relativistic limit.** When $V \ll c$ ($\Gamma\to 1$), synchrotron radiation degenerates to **cyclotron radiation**: monochromatic emission at the cyclotron frequency $\omega_B = |q|B/m$, in the symmetric dipole pattern, with no beaming and no spectral broadening.

---

# Categorical / Structural Definition

Structurally, synchrotron radiation is the image of two prior constructions composed: it is the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Liénard radiation formula]] evaluated on the trajectory produced by the [[Def - The Lorentz Four-Force|Lorentz force]] in a uniform magnetic field. The Lorentz-force equation $m\,\mathrm dU/\mathrm d\tau = q\,F(\,\cdot\,, U)$ with $F$ a pure magnetic field has, as its solution, a helix; feeding that helix's four-acceleration into $\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$ produces the synchrotron power. So synchrotron radiation is not an independent object but a *value* of a function — the radiation formula — at a *particular input* — magnetic helical motion. This compositional view is why it inherits everything from its parents: the $\Gamma$-scaling from Liénard, the $1/\Gamma$ beaming and broad spectrum from the [[Thm - Angular Distribution of Radiation|angular distribution]], and the energy density from the [[Def - Energy-Momentum Tensor of the Electromagnetic Field|electromagnetic energy-momentum tensor]].

There is a unifying frame that organises all magnetic radiation into one family parametrised by $\Gamma$: at $\Gamma\approx 1$ it is *cyclotron* radiation (one tone, the cyclotron line); at intermediate $\Gamma$ (a few) it is *gyro-synchrotron* radiation (a few harmonics of the cyclotron frequency, mildly beamed); and at $\Gamma\gg 1$ it is *synchrotron* radiation (a continuum of harmonics merging into a smooth broad spectrum, sharply beamed). The single continuous parameter $\Gamma$ slides between these regimes, and the qualitative transitions — discrete-to-continuous spectrum, unbeamed-to-beamed — happen as beaming sets in. This is the same one-parameter-family pattern that organises many relativistic phenomena: a Newtonian limit, a "mildly relativistic" intermediate, and an ultrarelativistic regime with qualitatively new features, all governed by where $\Gamma$ sits relative to $1$.

---

# Relate to Other Fields / Compression

Synchrotron radiation is the relativistic completion of cyclotron radiation, and the relationship is precisely that between the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Liénard and Larmor formulas]]: cyclotron is the $\Gamma\to1$ corner. To an accelerator physicist it is the dominant energy-loss mechanism that caps the energy of circular electron machines; to a radio astronomer it is the most important non-thermal emission process in the universe; to a materials scientist it is the brightest available source of tunable X-rays. These are three faces of one formula.

**True name:** synchrotron radiation is *the Liénard radiation of a charge on a magnetic helix, beamed into a $1/\Gamma$ cone and therefore broadband.* The two clauses are the whole content: "Liénard radiation of a magnetic helix" gives the power and its $\Gamma$-scaling, and "beamed into a $1/\Gamma$ cone" gives the broad spectrum. When you need to reason about synchrotron radiation, do not reach for a special formula — reconstruct it by putting circular motion into Liénard and then invoking beaming for the spectrum.

The deepest cross-field connection is to **astrophysical magnetic-field measurement**. Because the characteristic frequency $f_c \propto \Gamma^2 B$ couples the (unknown) electron energy to the (unknown) magnetic field, observing the synchrotron spectrum of a cosmic source — its turnover frequency, its spectral index — lets one infer both the energies of the relativistic electrons and the strength of the magnetic field threading the source, across distances of light-years. The synchrotron formula is, in this sense, a remote-sensing tool: it is how we know the Crab Nebula's field is $\sim10^{-8}$ T and its electrons reach $\Gamma\sim10^6$, and how we map magnetic fields in radio galaxies we will never visit.

---

# Examples / Corollaries

**Is an instance — a storage-ring light source.** At a synchrotron facility (SOLEIL, ESRF, the APS), electrons are held at $\Gamma\sim10^3$–$10^4$ in a ring of radius tens of metres; the synchrotron radiation they emit on the bending magnets, with $\varepsilon_c$ in the keV range, is extracted as intense, collimated, tunable X-ray beams used for crystallography, protein structure determination, and X-ray absorption spectroscopy. Insertion devices (undulators, wigglers) add controlled wiggles to extend and tune the spectrum. Here synchrotron radiation is the *product*, deliberately maximised.

**Is an instance — LEP and the LHC.** In the LEP electron–positron collider ($R = 4.3$ km, $E = 104$ GeV, so $\Gamma\sim 2\times10^5$), the energy lost per turn was $\Delta E \approx 2.4$ GeV — about $2\%$ of the beam energy *every revolution*, a crippling tax that ultimately limited LEP's energy. In the *same tunnel*, the LHC accelerates protons ($m \approx 1836\,m_e$) to $7$ TeV with a per-turn loss of only $\sim 4.3$ keV, because the $m^{-4}$ scaling suppresses proton synchrotron loss by $\sim10^{13}$. Here synchrotron radiation is the *enemy*: it is why future high-energy electron colliders (the ILC) must be linear.

**Is an instance — the Crab Nebula.** The Crab is the remnant of the supernova of 1054, powered by a central pulsar that injects ultrarelativistic electrons ($\Gamma\sim10^6$) into the nebula's magnetic field ($B\sim10^{-8}$ T). These electrons radiate synchrotron emission from radio frequencies to X-rays; the bluish glow at the nebula's centre is synchrotron light, and its spectral cutoff near $10^{16}$ Hz, fed into $f_c$, yields the electron Lorentz factor. Here synchrotron radiation is the *diagnostic* by which we read the source's physics.

**Is NOT an instance — thermal (blackbody) radiation.** The glow of a hot body is thermal radiation, set by temperature and following the Planck spectrum, with no preferred direction and no dependence on any magnetic field. Synchrotron radiation is *non-thermal*: its spectrum reflects the energy distribution of relativistic particles, not a temperature, it is beamed, and it requires both a magnetic field and relativistic charges. Jupiter's radio image shows both: the planet's disk glows thermally, while the surrounding radiation belt glows by synchrotron emission from trapped relativistic electrons — two physically distinct mechanisms in one picture.

**Is NOT an instance — bremsstrahlung.** Braking radiation from a charge decelerated by an *electric* field (as in an X-ray tube) is also non-thermal and broadband, but its acceleration is collisional and typically *along* the velocity, not the smooth perpendicular acceleration of magnetic circular motion. Bremsstrahlung is [[Thm - Angular Distribution of Radiation|case (ii)]] (collinear) radiation from scattering; synchrotron is case (iii) (orthogonal) radiation from steady magnetic bending. Both radiate, but the geometry, spectrum shape, and angular pattern differ.

**Corollary — the $m^{-4}$ rule.** At fixed energy $E$ and fixed orbit radius $R$, the synchrotron power scales as $(E/mc^2)^4 = \Gamma^4 \propto m^{-4}$, so a proton radiates $(m_p/m_e)^4 \approx 1.1\times10^{13}$ times less than an electron of the same energy on the same orbit. This single corollary is the reason particle physics splits its machines by particle type.

**Calibration check.** If you have understood the definition you should be able to: (i) recover the synchrotron power $\mathcal P = q^4B^2\Gamma^2V^2\sin^2\alpha/6\pi\varepsilon_0 c^3 m^2$ by inserting the centripetal acceleration $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$ into the Liénard formula and using $\omega_B = |q|B/m$; (ii) explain in one sentence why the spectrum is broad rather than monochromatic (beaming $\Rightarrow$ short pulses $\Rightarrow$ broad Fourier content); and (iii) state how the radiated power per turn scales with particle mass at fixed energy and radius, and hence why the LHC tolerates what crippled LEP.

---

# Unlocked by This

> [!tip] Synchrotron Astrophysics and Cosmic Magnetism *(from High-Energy Astrophysics)*
> Synchrotron radiation is the dominant non-thermal emission mechanism across the universe: radio galaxies and quasar jets, supernova remnants like the Crab, pulsar wind nebulae, the diffuse Galactic radio background, and gamma-ray-burst afterglows all shine by relativistic electrons spiralling in magnetic fields. Because the characteristic frequency $f_c\propto\Gamma^2 B$ and the spectral index encodes the electron energy distribution, observing a source's synchrotron spectrum is a remote measurement of *both* its relativistic-particle energies and its magnetic-field strength — across intergalactic distances. This makes the formula on this page one of the most-used relations in observational astronomy.

> [!tip] Synchrotron Light Sources and Free-Electron Lasers *(from Accelerator Physics)*
> Dedicated storage rings and the magnetic insertion devices within them (undulators, wigglers) turn the synchrotron "energy loss" into the world's brightest tunable X-ray and ultraviolet beams, enabling protein crystallography, time-resolved chemistry, and materials science under extreme conditions. Pushed further, the **free-electron laser** uses a long undulator to make a relativistic electron bunch radiate coherently, producing X-ray pulses billions of times brighter still — the basis of facilities like the LCLS and European XFEL. The radiation formula that limits accelerators is, turned around, an unrivalled scientific instrument.

> [!tip] Curvature Radiation and Pulsar Magnetospheres *(from Compact-Object Astrophysics)*
> In the extreme magnetic fields of a pulsar ($B\sim10^8$ T), electrons are forced to follow curved field lines almost exactly, radiating **curvature radiation** — the close cousin of synchrotron radiation in which the "orbit radius" is the radius of curvature of the field line rather than the gyroradius. The same beaming and broad-spectrum physics governs the coherent radio pulses and high-energy gamma rays of pulsars, and underlies models of the pulsar lighthouse beam.
