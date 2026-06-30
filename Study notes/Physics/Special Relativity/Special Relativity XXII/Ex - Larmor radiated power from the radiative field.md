---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Liénard-Wiechert Potential"
  - "Thm - Electromagnetic Waves"
tags: [physics, special-relativity]
---

# Problem Statement

Compute the power radiated by an accelerating charge, deriving the Larmor formula from the radiative part of the Liénard–Wiechert field.

1. Write the radiative field of a slowly-moving charge ($|\mathbf v| \ll c$) from the Liénard–Wiechert result: $\mathbf E_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$, $\mathbf B_{\mathrm{rad}} = \frac1c\hat{\mathbf n}\times\mathbf E_{\mathrm{rad}}$, with $\boldsymbol\gamma$ the acceleration at the retarded time.
2. Compute the Poynting vector $\mathbf S = \varepsilon_0 c^2\mathbf E_{\mathrm{rad}}\times\mathbf B_{\mathrm{rad}}$ and show it falls off as $1/r^2$, so the energy flux through a large sphere is finite — radiation.
3. Show the angular distribution is $\frac{dP}{d\Omega} = \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\sin^2\Theta$, where $\Theta$ is the angle between $\hat{\mathbf n}$ and $\boldsymbol\gamma$ (the dipole radiation pattern, with no emission along the acceleration).
4. Integrate over all directions to obtain the **Larmor formula** $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$.

**Recall:**

![[Thm - The Liénard-Wiechert Potential#Statement]]

The radiative part of the Liénard–Wiechert field falls off as $1/r$ and is nonzero only under acceleration; in the nonrelativistic limit $\mathbf E_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$, transverse and null. The Poynting vector $\mathbf S = \varepsilon_0 c^2\mathbf E\times\mathbf B$ is the energy flux of the [[Thm - Electromagnetic Waves|electromagnetic field]]; for a wave with $|\mathbf E| = c|\mathbf B|$, $|\mathbf S| = \varepsilon_0 c E^2$. The solid-angle element is $d\Omega = \sin\Theta\,d\Theta\,d\phi$, and $\int\sin^2\Theta\,d\Omega = \frac{8\pi}{3}$.

---

# Convergent Strategy

**Problem class.** A *characterise-a-field-and-compute-its-energy* problem, combining the fourth target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]] (characterise the radiative field) with an energy-flux computation. The routine is to take the radiative field, square it into the Poynting vector, and integrate over a sphere.

**Assumption pattern.** The given is the radiative part of the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]], $\mathbf E_{\mathrm{rad}} \propto a/r$. The signpost is "$1/r$ falloff" — the radiative field dies slowly enough that its energy flux through a sphere ($\sim$ field$^2\times$ area $\sim (1/r)^2\times r^2$) stays finite, which is the signature of radiation. What this unlocks is the radiated power, computed by integrating the Poynting flux.

**Theorem routing.** The route is: radiative field $\mathbf E_{\mathrm{rad}} \propto a/r$ (Step 1) $\to$ Poynting vector $\mathbf S = \varepsilon_0 c^2\mathbf E\times\mathbf B \propto a^2/r^2$ (Step 2) $\to$ angular distribution $\frac{dP}{d\Omega} \propto a^2\sin^2\Theta$ (Step 3) $\to$ integrate $\int\sin^2\Theta\,d\Omega = \frac{8\pi}{3}$ for the Larmor formula (Step 4).

**Key decision point.** The crux is the $1/r$ falloff of the radiative field, which is what makes the energy flux through an arbitrarily large sphere finite and nonzero — energy that escapes to infinity. The Coulomb part, falling as $1/r^2$, gives a flux $\sim 1/r^2$ that vanishes at infinity (no radiation). The decision is to keep *only* the radiative ($1/r$) part for the radiated power, discarding the Coulomb ($1/r^2$) part which carries no net energy away.

---

# Legal Operations Used

1. **Operation 8 from the topic page (recognise the exterior product / wave structure).** The radiative field is transverse and null (a wedge), so $|\mathbf E_{\mathrm{rad}}| = c|\mathbf B_{\mathrm{rad}}|$ and the Poynting vector points radially outward.

2. **Operation 9 from the topic page (restore $c$ to recover the textbook form).** The Larmor formula is written with $c$ restored, $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$.

3. **The energy flux of a wave (from [[Thm - Electromagnetic Waves]]).** The radiated power is the integral of the Poynting vector, the energy flux of the radiative field, over a large sphere.

---

# Hints

> [!note]- Hint 1
> The radiative field, keeping only the $1/r$ (acceleration) term of the Liénard–Wiechert field in the nonrelativistic limit, is $\mathbf E_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$. The double cross product gives a vector transverse to $\hat{\mathbf n}$, with magnitude $\frac{q\gamma\sin\Theta}{4\pi\varepsilon_0 c^2 r}$ where $\Theta$ is the angle between $\hat{\mathbf n}$ and $\boldsymbol\gamma$.

> [!note]- Hint 2
> $|\mathbf S| = \varepsilon_0 c^2|\mathbf E_{\mathrm{rad}}||\mathbf B_{\mathrm{rad}}| = \varepsilon_0 c^2\cdot|\mathbf E_{\mathrm{rad}}|\cdot\frac{|\mathbf E_{\mathrm{rad}}|}{c} = \varepsilon_0 c|\mathbf E_{\mathrm{rad}}|^2$. Substitute $|\mathbf E_{\mathrm{rad}}| = \frac{q\gamma\sin\Theta}{4\pi\varepsilon_0 c^2 r}$; the result $\propto 1/r^2$ cancels the $r^2$ in the sphere's area.

> [!note]- Hint 3
> The power per solid angle is $\frac{dP}{d\Omega} = |\mathbf S|r^2 = \varepsilon_0 c|\mathbf E_{\mathrm{rad}}|^2 r^2 = \frac{q^2\gamma^2\sin^2\Theta}{16\pi^2\varepsilon_0 c^3}$. The $\sin^2\Theta$ is the dipole pattern: maximum perpendicular to $\boldsymbol\gamma$, zero along it (a charge does not radiate in the direction it accelerates).

> [!note]- Hint 4
> Integrate over the sphere: $P = \int\frac{dP}{d\Omega}d\Omega = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\int\sin^2\Theta\,d\Omega = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\cdot\frac{8\pi}{3} = \frac{q^2\gamma^2}{6\pi\varepsilon_0 c^3}$, with $\gamma = a$ the acceleration.

---

# Solution

The radiated power comes from squaring the radiative field and integrating over a sphere. Step 1 writes the radiative field; Step 2 forms the Poynting vector; Step 3 finds the angular distribution; Step 4 integrates to the Larmor formula. The non-obvious move is in Step 2: the $1/r$ field gives a $1/r^2$ flux that survives the $r^2$ area, the signature of radiation.

**Step 1: The radiative field of a slowly-moving charge.**

> [!note]- Derivation
> Keeping only the $1/r$ (radiative) part of the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] in the nonrelativistic limit $|\mathbf v| \ll c$, the electric field is
> $$\mathbf E_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma),$$
> with $\boldsymbol\gamma$ the acceleration at the retarded time, $\hat{\mathbf n}$ the direction to the field point. The double cross product $\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma) = \hat{\mathbf n}(\hat{\mathbf n}\cdot\boldsymbol\gamma) - \boldsymbol\gamma$ is the component of $-\boldsymbol\gamma$ transverse to $\hat{\mathbf n}$, with magnitude $\gamma\sin\Theta$ ($\Theta$ the angle between $\hat{\mathbf n}$ and $\boldsymbol\gamma$). So $|\mathbf E_{\mathrm{rad}}| = \frac{q\gamma\sin\Theta}{4\pi\varepsilon_0 c^2 r}$. The magnetic field is $\mathbf B_{\mathrm{rad}} = \frac1c\hat{\mathbf n}\times\mathbf E_{\mathrm{rad}}$, transverse to both, with $|\mathbf B_{\mathrm{rad}}| = |\mathbf E_{\mathrm{rad}}|/c$. The field is transverse and null — locally a [[Thm - Electromagnetic Waves|plane wave]] propagating radially outward.

**Step 2: The Poynting vector falls off as $1/r^2$.**

> [!note]- Derivation
> The energy flux is the Poynting vector $\mathbf S = \varepsilon_0 c^2\mathbf E_{\mathrm{rad}}\times\mathbf B_{\mathrm{rad}}$. Since $\mathbf E_{\mathrm{rad}}\perp\mathbf B_{\mathrm{rad}}$ and $|\mathbf B_{\mathrm{rad}}| = |\mathbf E_{\mathrm{rad}}|/c$, the magnitude is
> $$|\mathbf S| = \varepsilon_0 c^2|\mathbf E_{\mathrm{rad}}||\mathbf B_{\mathrm{rad}}| = \varepsilon_0 c|\mathbf E_{\mathrm{rad}}|^2 = \varepsilon_0 c\left(\frac{q\gamma\sin\Theta}{4\pi\varepsilon_0 c^2 r}\right)^2 = \frac{q^2\gamma^2\sin^2\Theta}{16\pi^2\varepsilon_0 c^3 r^2},$$
> directed radially along $\hat{\mathbf n}$ (the wave carries energy outward). The crucial feature is the **$1/r^2$ falloff**: this is exactly compensated by the $r^2$ in the area of a sphere, so the total flux through a sphere of radius $r$ is *independent of $r$* — energy escapes to infinity. (Contrast the Coulomb part, $|\mathbf E_{\mathrm{Coul}}| \sim 1/r^2$, giving $|\mathbf S| \sim 1/r^4$ and flux $\sim 1/r^2 \to 0$: no radiation.)

**Step 3: The angular distribution is the dipole pattern.**

> [!note]- Derivation
> The power radiated per unit solid angle is the flux times the area element $r^2 d\Omega$:
> $$\frac{dP}{d\Omega} = |\mathbf S|\,r^2 = \frac{q^2\gamma^2\sin^2\Theta}{16\pi^2\varepsilon_0 c^3}.$$
> The $r$-dependence has cancelled, confirming radiation. The angular pattern is $\sin^2\Theta$ — the **dipole radiation pattern**:
> - **Maximum** at $\Theta = \pi/2$ (perpendicular to the acceleration): the charge radiates most strongly to the sides.
> - **Zero** at $\Theta = 0, \pi$ (along the acceleration): a charge does *not* radiate in the direction it accelerates.
> This $\sin^2\Theta$ doughnut, symmetric about the acceleration axis, is the characteristic pattern of dipole radiation — the pattern of a linear antenna, with its null along the antenna axis.

**Step 4: Integrating gives the Larmor formula.**

> [!note]- Derivation
> Integrate over all directions, using $\int\sin^2\Theta\,d\Omega = \int_0^{2\pi}\!d\phi\int_0^\pi\sin^2\Theta\sin\Theta\,d\Theta = 2\pi\cdot\frac43 = \frac{8\pi}{3}$:
> $$P = \int\frac{dP}{d\Omega}\,d\Omega = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\int\sin^2\Theta\,d\Omega = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\cdot\frac{8\pi}{3} = \frac{q^2\gamma^2}{6\pi\varepsilon_0 c^3}.$$
> Writing the acceleration magnitude as $a = |\boldsymbol\gamma|$, this is the **Larmor formula**:
> $$\boxed{P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}}.$$
> The radiated power is proportional to the *square of the acceleration* — a charge radiates only when accelerating, and the power grows as $a^2$. This is the rate at which an accelerating charge loses energy to electromagnetic radiation, the foundation of antenna theory and the reason a classical orbiting electron would spiral into the nucleus.

> [!note]- Complete formal solution
> The radiative field of a slowly-moving charge is $\mathbf E_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$, magnitude $\frac{q\gamma\sin\Theta}{4\pi\varepsilon_0 c^2 r}$, with $\mathbf B_{\mathrm{rad}} = \frac1c\hat{\mathbf n}\times\mathbf E_{\mathrm{rad}}$. The Poynting vector $|\mathbf S| = \varepsilon_0 c|\mathbf E_{\mathrm{rad}}|^2 = \frac{q^2\gamma^2\sin^2\Theta}{16\pi^2\varepsilon_0 c^3 r^2}$ falls off as $1/r^2$, so $\frac{dP}{d\Omega} = |\mathbf S|r^2 = \frac{q^2\gamma^2\sin^2\Theta}{16\pi^2\varepsilon_0 c^3}$ — the dipole pattern, zero along $\boldsymbol\gamma$, maximal transverse. Integrating with $\int\sin^2\Theta\,d\Omega = \frac{8\pi}{3}$ gives the Larmor formula $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$. $\blacksquare$

---

# Key Takeaways

**The $1/r$ falloff of the radiative field is the signature of radiation: it makes the energy flux through a sphere finite and nonzero.** The single most important fact distinguishing radiation from the static field is the rate of falloff. The radiative field dies as $1/r$, so its energy flux (Poynting vector $\sim$ field$^2$) dies as $1/r^2$ — exactly the rate that survives multiplication by the $r^2$ area of a sphere, giving a constant flux to infinity. The Coulomb field dies as $1/r^2$, so its flux dies as $1/r^4$, which vanishes at infinity: no energy escapes. The reusable diagnostic, applicable across all radiation theory, is to check the falloff: a $1/r$ field radiates, a $1/r^2$ field does not. This is why the radiative part of the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] — the part proportional to acceleration — is the only part that carries energy away, and why uniform motion (no acceleration, no $1/r$ field) produces no radiation. The trigger to identify radiation is "does the field fall off as $1/r$?"; if so, integrate its Poynting flux for the radiated power.

**Radiated power scales as the square of acceleration, and a charge does not radiate along its acceleration.** The Larmor formula $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$ encodes two reusable facts. First, the power is $\propto a^2$: radiation is quadratic in acceleration, so doubling the acceleration quadruples the radiated power — this is why high-acceleration systems (synchrotrons, where the centripetal acceleration is enormous) radiate intensely, and why the radiation reaction force is proportional to the rate of change of acceleration. Second, the angular distribution is the $\sin^2\Theta$ dipole pattern, with a null along the acceleration axis: a charge radiates most strongly perpendicular to its acceleration and not at all in the direction it accelerates. The reusable picture is the doughnut-shaped emission pattern of a dipole antenna, with the acceleration playing the role of the antenna axis. These facts organise antenna theory, the physics of synchrotron light, and the classical instability of atoms — all governed by "power $\propto a^2$, emitted in a dipole pattern transverse to the acceleration".

**Squaring a field and integrating its flux over a surface is the universal method for energy transport.** The technique here — form the Poynting vector $\mathbf S = \varepsilon_0 c^2\mathbf E\times\mathbf B$ from the field, then integrate it over a closed surface — is the general recipe for computing energy flow in field theory, and it generalises directly to the electromagnetic energy–momentum tensor $T^{\mu\nu}$ of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]], where the Poynting vector is the $T^{0i}$ (energy-flux) component. The reusable principle: the energy carried by a field is quadratic in the field, and the power crossing a surface is the surface integral of the energy flux. This same method gives the radiated power of gravitational waves (quadratic in the wave amplitude, integrated over a sphere), the intensity of light (quadratic in the electric field, the basis of all of optics), and the momentum carried by radiation (radiation pressure). Recognising "energy flux = field squared, integrated over a surface" connects the Liénard–Wiechert field to the energetics of every radiating system.
