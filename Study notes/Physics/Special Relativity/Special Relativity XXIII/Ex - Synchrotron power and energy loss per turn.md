---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Synchrotron Radiation"
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Def - The Lorentz Four-Force"
tags: [physics, special-relativity]
---

# Problem Statement

A relativistic charge bent into a helix by a magnetic field radiates **synchrotron radiation**. The exercise is to derive its total power, energy loss per orbital revolution, and the famous $\Gamma^4 \propto m^{-4}$ scaling that decides the design of circular accelerators. Working with $c = 1$ except where $c$ is restored, mostly-minus signature:

1. **Helical motion in a uniform $\mathbf B$ field.** A charge $q$ of mass $m$, speed $V$, Lorentz factor $\Gamma$, moving at pitch angle $\alpha$ (the angle between $\mathbf V$ and $\mathbf B$) in a uniform magnetic field of magnitude $B$. From the Lorentz force $m\,\mathrm dU/\mathrm d\tau = q\,F(\,\cdot\,, U)$ specialised to a pure magnetic field, show the trajectory is a helix and identify the orbit radius
$$R = \frac{\Gamma m V\sin\alpha}{|q|B},$$
the (relativistic) orbital angular frequency $\Omega = V\sin\alpha/R = |q|B/(\Gamma m) = \omega_B/\Gamma$, and the centripetal three-acceleration magnitude
$$|\boldsymbol\gamma| = \frac{V^2\sin^2\alpha}{R} = \frac{|q|BV\sin\alpha}{\Gamma m} = \frac{\omega_B V\sin\alpha}{\Gamma}, \qquad \boldsymbol\gamma\perp\mathbf V,$$
where $\omega_B = |q|B/m$ is the **cyclotron frequency**.

2. **Synchrotron power from Liénard.** The Liénard formula gives $\mathcal P = (q^2/6\pi\varepsilon_0 c^3)\,\Gamma^6[\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$. Substitute $\boldsymbol\gamma\perp\mathbf V$ (so $\boldsymbol\gamma\times\mathbf V$ has magnitude $|\boldsymbol\gamma|V$) and $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$ to derive the synchrotron power
$$\boxed{\mathcal P = \frac{q^4 B^2\Gamma^2 V^2\sin^2\alpha}{6\pi\varepsilon_0 c^3 m^2}.}$$

3. **Energy radiated per orbit.** The orbital period (measured in lab time) is $T_{\text{orbit}} = 2\pi/\Omega = 2\pi\Gamma/\omega_B$. Multiply $\mathcal P$ by $T_{\text{orbit}}$ to obtain
$$\Delta E_{\text{turn}} = \mathcal P\cdot T_{\text{orbit}} = \frac{|q|^3 B\,\Gamma^3 V^2}{3\varepsilon_0 c^3 m},$$
and use $E_{\text{particle}} = \Gamma mc^2$ together with $R$ from Part 1 (and ultrarelativistic $V \approx c$, $\sin\alpha = 1$) to rewrite this as
$$\Delta E_{\text{turn}} = \frac{q^2}{3\varepsilon_0 R}\left(\frac{V}{c}\right)^3\left(\frac{E}{mc^2}\right)^4,$$
exhibiting the decisive **$\Gamma^4 \propto (E/mc^2)^4 \propto m^{-4}$ scaling**.

4. **Accelerator design verdict.** Apply the formula to LEP (electrons at $E = 104\,\mathrm{GeV}$, $R = 4.3\,\mathrm{km}$) and the LHC (protons at $E = 7\,\mathrm{TeV}$, same tunnel $R = 4.3\,\mathrm{km}$). Verify that LEP loses about $2.4\,\mathrm{GeV}$ per turn (cripplingly large) while the LHC loses about $4.3\,\mathrm{keV}$ per turn (negligible), and conclude that the $m^{-4}$ ratio $(m_p/m_e)^4 \approx 1.13\times 10^{13}$ is what makes proton machines tolerable and forces future high-energy electron–positron colliders (the ILC) to be *linear*.

**Recall:**

The exercise rests on the Liénard formula and the geometry of helical motion in a magnetic field.

![[Def - Synchrotron Radiation#The Definition]]

The [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Liénard formula]] gives the radiated power as $\mathcal P = (q^2/6\pi\varepsilon_0 c^3)\Gamma^6[\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$ in lab three-vectors. The [[Def - The Lorentz Four-Force|Lorentz four-force]] for a pure magnetic field yields a constant-speed helix, with the magnetic force doing no work but continually turning the velocity vector.

---

# Convergent Strategy

**Problem class.** A *specialise-Liénard-to-a-specific-trajectory* problem. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for radiated power: identify the four-acceleration along the trajectory, plug into the invariant Larmor formula or its Liénard lab-frame form, read off the answer; for scaling questions, extract the $\Gamma$- and $m$-dependence.

**Assumption pattern.** Three signposts. (i) "Uniform magnetic field" $\Rightarrow$ pure magnetic Lorentz force $\Rightarrow$ helical motion with constant speed. (ii) "Synchrotron" $\Rightarrow$ ultrarelativistic, $\Gamma\gg 1$, $V \to c$. (iii) "Per turn" $\Rightarrow$ multiply power by orbital period $T_{\text{orbit}} = 2\pi\Gamma/\omega_B$ (note: the relativistic orbital frequency is the *cyclotron frequency divided by $\Gamma$*, time dilation of the gyration).

**Theorem routing.** Part 1: integrate the Lorentz-force equation in a uniform $B$ field; show the speed is constant and the trajectory is a helix; read off $R, \Omega, \boldsymbol\gamma$. Part 2: plug $\boldsymbol\gamma\perp\mathbf V$ into Liénard. Part 3: multiply by period. Part 4: numerical comparison.

**Key decision point.** The crux is recognising the $\Gamma^4$ scaling. From Part 2, $\mathcal P\propto\Gamma^2 V^2 \approx \Gamma^2 c^2$; from Part 3, the period $T_{\text{orbit}}\propto\Gamma$; product $\Delta E\propto\Gamma^3$. But at *fixed* radius $R$ and *fixed* magnetic field $B$, the bend curvature is fixed, so the relevant comparison is at fixed $R$, and then one $\Gamma$ from $V \sim c$ (already used) plus a hidden $\Gamma$ from rewriting via $E = \Gamma mc^2$ gives $\Gamma^4$ in terms of energy. The order of these substitutions is the source of confusion; carefully tracking what is held fixed gives the right scaling.

---

# Legal Operations Used

1. **Express the four-acceleration invariant in laboratory variables** (operation 8): for $\boldsymbol\gamma\perp\mathbf V$, $|A|^2 = \Gamma^4|\boldsymbol\gamma|^2$ — pure perpendicular case.

2. **Use the Liénard formula** ([[Thm - Radiation by an Accelerated Charge (Larmor Formula)]]): specialise to circular motion, identify the perpendicular acceleration, plug in.

3. **Read beaming from the Doppler factor** (operation 9): the orbital period is $2\pi\Gamma/\omega_B$ (relativistic time dilation), not $2\pi/\omega_B$ — getting the period right requires the $\Gamma$ factor.

---

# Hints

> [!note]- Hint 1
> Lorentz force in a pure magnetic field: $m\,\mathrm d(\Gamma\mathbf V)/\mathrm dt = q\,\mathbf V\times\mathbf B$. The magnetic force is perpendicular to $\mathbf V$ and does no work, so $\Gamma$ is constant, $|\mathbf V|$ is constant. The component of $\mathbf V$ along $\mathbf B$ is unaffected (no force along $\mathbf B$); the perpendicular component rotates at the relativistic cyclotron frequency $\Omega = qB/(\Gamma m) = \omega_B/\Gamma$. Trajectory: helix of radius $R = V\sin\alpha/\Omega = \Gamma m V\sin\alpha/(qB)$, pitch determined by the angle $\alpha$.

> [!note]- Hint 2
> Centripetal acceleration: $|\boldsymbol\gamma| =$ (perpendicular velocity)$^2$/$R = (V\sin\alpha)^2/R = (V\sin\alpha)^2\cdot qB/(\Gamma m V\sin\alpha) = qBV\sin\alpha/(\Gamma m)$. So $|\boldsymbol\gamma|^2 = q^2B^2V^2\sin^2\alpha/(\Gamma^2 m^2)$. With $\boldsymbol\gamma\perp\mathbf V$, Liénard bracket: $\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2 = |\boldsymbol\gamma|^2 - |\boldsymbol\gamma|^2 V^2/c^2 = |\boldsymbol\gamma|^2(1 - V^2/c^2) = |\boldsymbol\gamma|^2/\Gamma^2$. So $\mathcal P = (q^2/6\pi\varepsilon_0 c^3)\Gamma^6\cdot|\boldsymbol\gamma|^2/\Gamma^2 = (q^2/6\pi\varepsilon_0 c^3)\Gamma^4|\boldsymbol\gamma|^2 = (q^2/6\pi\varepsilon_0 c^3)\Gamma^4\cdot q^2B^2V^2\sin^2\alpha/(\Gamma^2 m^2) = q^4B^2\Gamma^2 V^2\sin^2\alpha/(6\pi\varepsilon_0 c^3 m^2)$.

> [!note]- Hint 3
> Orbital period: $T_{\text{orbit}} = 2\pi/\Omega = 2\pi\Gamma m/(qB)$. Energy per turn: $\Delta E = \mathcal P\cdot T_{\text{orbit}} = \frac{q^4 B^2\Gamma^2 V^2\sin^2\alpha}{6\pi\varepsilon_0 c^3 m^2}\cdot\frac{2\pi\Gamma m}{qB} = \frac{q^3 B\Gamma^3 V^2\sin^2\alpha}{3\varepsilon_0 c^3 m}$. For ultrarelativistic charge, $V\to c$, $\sin\alpha = 1$ (planar circular orbit). Use $R = \Gamma m V/(qB) \approx \Gamma m c/(qB)$, so $\Gamma m/(qB) = R/c$. Substitute: $\Delta E = \frac{q^3 B\Gamma^3 c^2}{3\varepsilon_0 c^3 m}\cdot\frac{\Gamma m}{\Gamma m} =$ — let me redo: $\Delta E = q^3 B\Gamma^3 V^2/(3\varepsilon_0 c^3 m)$. Multiply numerator and denominator by $R$ via $qB = \Gamma m c/R$ (at $V \approx c$): $qB\cdot R = \Gamma mc$, so $\Delta E = q^2\Gamma^3 V^2\cdot(qBR)/[3\varepsilon_0 c^3 m R] = q^2\Gamma^3 V^2\cdot\Gamma mc/[3\varepsilon_0 c^3 m R] = q^2\Gamma^4(V/c)^3/[3\varepsilon_0 R]\cdot(V/c)^{-1}\cdot c$ — getting messy. Use the cleaner identity: $\Gamma^4 = (E/mc^2)^4$, and the final form $\Delta E = q^2(V/c)^3(E/mc^2)^4/(3\varepsilon_0 R)$.

> [!note]- Hint 4
> Numerical: with $q = e$, $V = c$, $\sin\alpha = 1$, $\Delta E = e^2(E/mc^2)^4/(3\varepsilon_0 R)$. Compute $e^2/(3\varepsilon_0 R)$ with $R = 4300\,\mathrm m$, $e^2/(4\pi\varepsilon_0) = 1.44\,\mathrm{nm\cdot eV} = 1.44\times 10^{-9}\,\mathrm{m\cdot eV}$, so $e^2/(3\varepsilon_0 R) = (4\pi/3)\cdot 1.44\times 10^{-9}\,\mathrm{m\cdot eV}/(4300\,\mathrm m) = 1.4\times 10^{-12}\,\mathrm{eV}$. LEP electron: $E/m_e c^2 = 104\,\mathrm{GeV}/0.511\,\mathrm{MeV} = 2.04\times 10^5$, fourth power $1.7\times 10^{21}$; product $\sim 2.4\,\mathrm{GeV}$. LHC proton: $E/m_p c^2 = 7000\,\mathrm{GeV}/938\,\mathrm{MeV} = 7460$, fourth power $3.1\times 10^{15}$; product $\sim 4.3\,\mathrm{keV}$. Ratio: $(m_p/m_e)^4 = 1836^4 \approx 1.13\times 10^{13}$ — exactly the suppression factor for protons.

---

# Solution

A charge in a magnetic field follows a helix at constant speed; the relativistic cyclotron frequency is $\omega_B/\Gamma$ and the centripetal acceleration is $\omega_B V\sin\alpha/\Gamma$. Plugging into Liénard with $\boldsymbol\gamma\perp\mathbf V$ gives synchrotron power $\mathcal P = q^4 B^2\Gamma^2 V^2\sin^2\alpha/(6\pi\varepsilon_0 c^3 m^2)$. Multiplying by the orbital period $2\pi\Gamma/\omega_B$ and ultrarelativising yields energy loss per turn $\Delta E = (q^2/3\varepsilon_0 R)(V/c)^3(E/mc^2)^4$, exhibiting the decisive $\Gamma^4 \propto m^{-4}$ scaling — the reason LHC protons tolerate what crippled LEP electrons.

**Step 1: Helical trajectory and centripetal acceleration.**

> [!note]- Derivation
> In a uniform magnetic field, with no electric field, the [[Def - The Lorentz Four-Force|Lorentz force]] on the charge is $\mathbf F = q\mathbf V\times\mathbf B$. Decompose $\mathbf V = \mathbf V_\parallel + \mathbf V_\perp$ into components parallel and perpendicular to $\mathbf B$. The force has $\mathbf V_\parallel\times\mathbf B = 0$, so the parallel component is unaffected: $\mathbf V_\parallel$ is constant. The perpendicular force is $q\mathbf V_\perp\times\mathbf B$, perpendicular to $\mathbf V_\perp$, so $|\mathbf V_\perp|$ is constant — the perpendicular velocity rotates at fixed magnitude.
>
> The result is *helical* motion: drifting at $\mathbf V_\parallel$ along $\mathbf B$ while rotating $\mathbf V_\perp$ at angular frequency $\Omega = qB/(\Gamma m) = \omega_B/\Gamma$ (the factor of $\Gamma$ is time dilation of the gyration in the lab frame, since the proper-time cyclotron frequency is $\omega_B = qB/m$). The pitch angle $\alpha$ is the angle between $\mathbf V$ and $\mathbf B$, with $V_\perp = V\sin\alpha$, $V_\parallel = V\cos\alpha$.
>
> Orbit radius (perpendicular projection): from $V_\perp = \Omega R$,
> $$R = \frac{V_\perp}{\Omega} = \frac{V\sin\alpha}{\omega_B/\Gamma} = \frac{\Gamma m V\sin\alpha}{|q|B}.$$
> Centripetal acceleration: circular motion at speed $V_\perp = V\sin\alpha$ in a circle of radius $R$:
> $$|\boldsymbol\gamma| = \frac{V_\perp^2}{R} = \frac{(V\sin\alpha)^2}{\Gamma m V\sin\alpha/(|q|B)} = \frac{|q|BV\sin\alpha}{\Gamma m} = \frac{\omega_B V\sin\alpha}{\Gamma},$$
> with $\boldsymbol\gamma$ radially inward (perpendicular to $\mathbf V_\perp$, hence perpendicular to $\mathbf V$). The magnetic Lorentz force does no work — its scalar product with $\mathbf V$ vanishes — so the *speed* is constant, but it is constantly changing the direction of $\mathbf V$, i.e. accelerating it.

**Step 2: Synchrotron power from Liénard.**

> [!note]- Derivation
> The [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Liénard formula]] in lab three-vectors:
> $$\mathcal P = \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^6\!\left[\boldsymbol\gamma\cdot\boldsymbol\gamma - \frac{(\boldsymbol\gamma\times\mathbf V)^2}{c^2}\right].$$
> Specialise to $\boldsymbol\gamma\perp\mathbf V$ (helical motion has perpendicular acceleration): $|\boldsymbol\gamma\times\mathbf V|^2 = |\boldsymbol\gamma|^2|\mathbf V|^2 = |\boldsymbol\gamma|^2 V^2$. So the bracket becomes
> $$|\boldsymbol\gamma|^2 - \frac{|\boldsymbol\gamma|^2 V^2}{c^2} = |\boldsymbol\gamma|^2\!\left(1 - \frac{V^2}{c^2}\right) = \frac{|\boldsymbol\gamma|^2}{\Gamma^2}.$$
> Substituting:
> $$\mathcal P = \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^6\cdot\frac{|\boldsymbol\gamma|^2}{\Gamma^2} = \frac{q^2\Gamma^4|\boldsymbol\gamma|^2}{6\pi\varepsilon_0 c^3}.$$
> Now plug in $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$ with $\omega_B = |q|B/m$:
> $$|\boldsymbol\gamma|^2 = \frac{q^2 B^2 V^2\sin^2\alpha}{\Gamma^2 m^2},$$
> giving
> $$\boxed{\mathcal P = \frac{q^2\Gamma^4}{6\pi\varepsilon_0 c^3}\cdot\frac{q^2 B^2 V^2\sin^2\alpha}{\Gamma^2 m^2} = \frac{q^4 B^2\Gamma^2 V^2\sin^2\alpha}{6\pi\varepsilon_0 c^3 m^2}.}$$
> Two factors of $\Gamma$ remain after the cancellation between $\Gamma^6$ (from Liénard) and $\Gamma^4$ (from the $1 - V^2/c^2$ bracket combined with $1/\Gamma^2$ in $|\boldsymbol\gamma|^2$). The mass-squared in the denominator is the seed of the catastrophic $m^{-4}$ scaling we will see in Part 3.

**Step 3: Energy radiated per orbit and the $\Gamma^4$ scaling.**

> [!note]- Derivation
> The orbital period in lab time is
> $$T_{\text{orbit}} = \frac{2\pi}{\Omega} = \frac{2\pi\Gamma m}{|q|B}.$$
> Energy lost per turn:
> $$\Delta E_{\text{turn}} = \mathcal P\cdot T_{\text{orbit}} = \frac{q^4 B^2\Gamma^2 V^2\sin^2\alpha}{6\pi\varepsilon_0 c^3 m^2}\cdot\frac{2\pi\Gamma m}{|q|B} = \frac{|q|^3 B\Gamma^3 V^2\sin^2\alpha}{3\varepsilon_0 c^3 m}.$$
> Now rewrite in terms of the orbit radius $R$ and the particle energy $E_{\text{particle}} = \Gamma mc^2$. From Part 1 (ultrarelativistic limit $V \approx c$, $\sin\alpha = 1$ for planar circular motion),
> $$R = \frac{\Gamma m c}{|q|B} \quad\Longrightarrow\quad |q|B = \frac{\Gamma m c}{R}.$$
> Substitute $|q|^3 B = q^2\cdot |q|B = q^2\cdot\Gamma mc/R$:
> $$\Delta E_{\text{turn}} = \frac{q^2\Gamma mc/R\cdot\Gamma^3 V^2\sin^2\alpha}{3\varepsilon_0 c^3 m} = \frac{q^2\,\Gamma^4 V^2\sin^2\alpha}{3\varepsilon_0 c^2 R}.$$
> For the ultrarelativistic limit $V/c \to 1$ but keeping the explicit $(V/c)^3$ factor (small ${1\over\Gamma^2}$ corrections to $V/c$ matter for precision but not for the scaling), and using $\Gamma^4 = (E_{\text{particle}}/mc^2)^4$:
> $$\boxed{\Delta E_{\text{turn}} = \frac{q^2}{3\varepsilon_0 R}\!\left(\frac{V}{c}\right)^3\left(\frac{E_{\text{particle}}}{mc^2}\right)^4.}$$
> The $\Gamma^4 \propto (E/mc^2)^4 \propto m^{-4}$ scaling at fixed energy is the dominant feature: light particles radiate vastly more than heavy ones at the same energy. The $\sin^2\alpha$ factor disappears because we took planar circular ($\alpha = \pi/2$); a general helical pitch reintroduces it.

**Step 4: LEP vs LHC.**

> [!note]- Derivation
> Numerical comparison at the same tunnel, $R = 4.3\,\mathrm{km}$, $V \approx c$, $\sin\alpha = 1$.
>
> *LEP electrons*, $E = 104\,\mathrm{GeV}$:
> $$\frac{E}{m_e c^2} = \frac{104\,\mathrm{GeV}}{0.511\,\mathrm{MeV}} = 2.035\times 10^5, \quad\left(\frac{E}{m_e c^2}\right)^4 \approx 1.71\times 10^{21}.$$
> Coupling factor (with $V/c\to 1$):
> $$\frac{q^2}{3\varepsilon_0 R} = \frac{4\pi}{3}\cdot\frac{e^2}{4\pi\varepsilon_0 R} = \frac{4\pi}{3}\cdot\frac{1.44\,\mathrm{nm\cdot eV}}{4300\,\mathrm m} = \frac{4\pi}{3}\cdot 3.35\times 10^{-13}\,\mathrm{eV} \approx 1.4\times 10^{-12}\,\mathrm{eV}.$$
> Product:
> $$\Delta E_{\text{LEP}} \approx 1.4\times 10^{-12}\,\mathrm{eV}\cdot 1.7\times 10^{21} \approx 2.4\times 10^9\,\mathrm{eV} = 2.4\,\mathrm{GeV}.$$
> This is **about $2\%$ of the beam energy lost every revolution** — a crippling tax. To maintain the beam, RF cavities had to replace this much energy each turn, and ultimately this scaling capped LEP's energy: doubling the energy would have quadrupled $\Gamma$ and the per-turn loss would have grown as $\Gamma^4 = 16$×. LEP was decommissioned in 2000 at its design ceiling.
>
> *LHC protons*, $E = 7\,\mathrm{TeV}$:
> $$\frac{E}{m_p c^2} = \frac{7000\,\mathrm{GeV}}{938\,\mathrm{MeV}} = 7460, \quad\left(\frac{E}{m_p c^2}\right)^4 \approx 3.1\times 10^{15}.$$
> Product:
> $$\Delta E_{\text{LHC}} \approx 1.4\times 10^{-12}\,\mathrm{eV}\cdot 3.1\times 10^{15} \approx 4.3\times 10^3\,\mathrm{eV} = 4.3\,\mathrm{keV}.$$
> A factor of $\sim 6\times 10^5$ smaller than LEP per turn, in the *same tunnel at higher energy* — utterly negligible. The ratio is
> $$\frac{\Delta E_{\text{LEP}}}{\Delta E_{\text{LHC}}} = \frac{(E_e/m_e c^2)^4}{(E_p/m_p c^2)^4} = \left(\frac{E_e}{E_p}\right)^4\cdot\left(\frac{m_p}{m_e}\right)^4 \cdot 1.$$
> The mass ratio alone gives $(m_p/m_e)^4 = 1836^4 \approx 1.13\times 10^{13}$ — *thirteen orders of magnitude* of suppression by going from electrons to protons. This is the **$m^{-4}$ verdict**: at the same circular geometry and roughly comparable energies, protons radiate $\sim 10^{13}$ times less than electrons, the reason the LHC is feasible in a ring while a successor electron–positron collider at TeV energies must be linear (the ILC, $\sim 30\,\mathrm{km}$ straight-line layout).

> [!note]- Complete formal solution
> A charge in a uniform $\mathbf B$ follows a helix at constant speed, with relativistic cyclotron frequency $\Omega = qB/(\Gamma m) = \omega_B/\Gamma$, radius $R = \Gamma mV\sin\alpha/(|q|B)$, and centripetal acceleration $|\boldsymbol\gamma| = \omega_B V\sin\alpha/\Gamma$, perpendicular to $\mathbf V$. The Liénard formula with $\boldsymbol\gamma\perp\mathbf V$ gives $\Gamma^6[\boldsymbol\gamma^2 - (\boldsymbol\gamma V)^2/c^2] = \Gamma^4|\boldsymbol\gamma|^2$, and substituting $|\boldsymbol\gamma|^2 = q^2B^2V^2\sin^2\alpha/(\Gamma^2 m^2)$ gives the **synchrotron power** $\mathcal P = q^4B^2\Gamma^2V^2\sin^2\alpha/(6\pi\varepsilon_0 c^3 m^2)$. Multiplying by the orbital period $T_{\text{orbit}} = 2\pi\Gamma m/(|q|B)$ and ultrarelativising yields **energy lost per turn** $\Delta E_{\text{turn}} = (q^2/3\varepsilon_0 R)(V/c)^3(E/mc^2)^4$, exhibiting $\Gamma^4 \propto m^{-4}$ scaling. Numerical evaluation in the LEP/LHC tunnel ($R = 4.3$ km): LEP electrons (104 GeV) lose $\sim 2.4$ GeV per turn (crippling), LHC protons (7 TeV) lose $\sim 4.3$ keV per turn (negligible); the ratio is $(m_p/m_e)^4 \approx 1.1\times 10^{13}$, the verdict that forces future high-energy electron colliders to be linear. $\blacksquare$

---

# Key Takeaways

**Synchrotron radiation is Liénard evaluated on a magnetic helix — a *value* of a function, not a new physical law.** The whole content of this exercise is recognising that the synchrotron-power formula is what you get when you plug the centripetal acceleration of helical motion into the Liénard formula. There is no new physics; the entire phenomenology — total power, energy loss per orbit, broad spectrum, beaming cone — is the radiation formulas of §23.3 specialised to a single trajectory. This compositional view (formula composed with trajectory) is the most reusable way to think about radiation: when you meet "synchrotron", "betatron", "undulator", "wiggler", "bremsstrahlung", do not memorise separate formulas. Each is Liénard evaluated on a particular four-acceleration: synchrotron on a helix, undulator on a periodic sinusoid, bremsstrahlung on a sudden deceleration. The radiated power, spectrum, and angular distribution all follow from $|A|^2$ on the trajectory and the universal beaming/integrating apparatus.

**The $\Gamma^4 \propto m^{-4}$ scaling is the single most consequential power law in accelerator physics, and it follows from a transparent chain of cancellations.** Tracking what $\Gamma$'s and $m$'s appear *where* is the difference between confusion and clarity. The power $\mathcal P\propto q^4 B^2\Gamma^2/m^2$ has $\Gamma^2$ (kinematic) and $m^{-2}$ (mass-squared in the denominator from the inverse mass appearing in the cyclotron frequency). Multiplying by the period $T_{\text{orbit}}\propto\Gamma m$ adds $\Gamma m$, giving $\Delta E\propto\Gamma^3 m^{-1}$ at *fixed magnetic field*. Switching to *fixed orbit radius* (the realistic constraint — accelerators have fixed tunnel size) uses $|q|B = \Gamma mc/R$ to substitute, replacing $B$ in $\mathcal P$ with $\Gamma m/R$, which adds another $\Gamma m$, giving $\Delta E\propto\Gamma^4 m^{-4}$ at fixed $R$. The $m^{-4}$ is half from the Larmor formula's intrinsic $m$-dependence and half from the cyclotron geometry (heavier particles need stronger fields to maintain the same orbit, but with $B$ fixed by tunnel design they orbit at larger radius, and the substitution introduces the second factor). The reusable lesson is that *scaling verdicts depend on what you hold fixed*: at fixed $B$ the dependence is $\Gamma^3 m^{-1}$, at fixed $R$ it is $\Gamma^4 m^{-4}$, and accelerator engineering uses the fixed-$R$ scaling because the cost of a circular machine is dominated by tunnel construction.

**The forced linearisation of future high-energy electron colliders is the macroscopic consequence of a microscopic Lorentz invariant.** The Larmor formula's invariant content $\mathcal P = q^2|A|^2/(6\pi\varepsilon_0 c)$ depends only on the magnitude of the four-acceleration. At fixed energy, the four-acceleration needed to bend a charge into a circle grows as $\Gamma^2$ (centripetal acceleration $\Gamma V\Omega = V^2/R$ in the lab, multiplied by appropriate $\Gamma$ factors to convert to the four-acceleration magnitude), and the power radiated grows as $|A|^2 \propto \Gamma^4$. For electrons at TeV energies, $\Gamma \sim 2\times 10^6$ and the per-turn loss is $\sim 4\times 10^{25}$ times the proton value — completely unfeasible. The only way out is to *eliminate the bending*, which is what a linear collider does: a straight-line accelerator has $\boldsymbol\gamma\parallel\mathbf V$ (collinear acceleration), for which the radiated power per unit accelerating force is much smaller (linear scaling instead of $\Gamma^4$). The macroscopic engineering choice — linear vs circular — is a direct consequence of the microscopic invariance $\mathcal P \propto |A|^2$, scaled up by twenty orders of magnitude. The Larmor formula, written in 1897, dictates the architecture of TeV-scale colliders in the twenty-first century.
