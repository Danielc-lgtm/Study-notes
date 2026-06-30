---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Energy-Momentum Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

The electromagnetic energy-momentum tensor takes its most concrete form when applied to specific field configurations. The exercise is to compute its observed quantities — energy density, momentum density (Poynting vector), and Maxwell stress — for three illustrative fields, and to recognise what the components mean physically. Working with $c = 1$ unless restored, mostly-minus signature, SI units:

1. **Static Coulomb field.** A point charge $q$ at rest at the origin produces $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$, $\mathbf B = 0$. Compute the energy density $\rho_{\text{em}}(r)$, the Poynting vector $\mathbf S$, and the radial-radial Maxwell stress $S_{rr}$ and the angular component $S_{\theta\theta}$. Integrate $\rho_{\text{em}}$ from a cut-off radius $a$ to infinity to get the electrostatic self-energy $W = q^2/(8\pi\varepsilon_0 a)$.

2. **Plane electromagnetic wave.** A wave travelling in direction $\hat{\mathbf n}$ has $\mathbf B = \hat{\mathbf n}\times\mathbf E/c$, $E = cB$, and $\mathbf E\cdot\hat{\mathbf n} = \mathbf B\cdot\hat{\mathbf n} = 0$. Compute $\rho_{\text{em}}$, the Poynting vector $\mathbf S = \mathbf E\times\mathbf B/\mu_0$, the momentum density $\boldsymbol\varpi_{\text{em}} = \varepsilon_0\mathbf E\times\mathbf B = \mathbf S/c^2$, and the field invariant $F^2$. Conclude that the wave is null and that it carries energy at speed $c$ in the direction $\hat{\mathbf n}$.

3. **Static crossed field configuration ("Feynman disk").** A point charge $q$ sits at the origin in the field of a magnetic dipole $\boldsymbol m$ also at the origin; the local fields are $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$ and a dipole $\mathbf B(\mathbf r)$. Show that the Poynting vector $\mathbf S = \mathbf E\times\mathbf B/\mu_0$ is nonzero (energy *appears* to circulate around the magnetic axis), but that $\vec\nabla\cdot\mathbf S = 0$ identically in this static configuration — so no *net* energy crosses any closed surface. Identify the angular momentum density $\mathbf L = \mathbf r\times\boldsymbol\varpi_{\text{em}}$ as the resolution: it is *angular momentum* stored in the field, not radiating energy.

4. Use the results of (1)–(3) to verify the topic page's illegal-but-tempting operation 5: "nonzero Poynting vector $\Rightarrow$ radiation" is false; radiation requires a *time-dependent* field falling as $1/r$.

**Recall:**

The exercise rests on the electromagnetic energy-momentum tensor's observer decomposition.

![[Def - Energy-Momentum Tensor of the Electromagnetic Field#The Definition]]

Relative to an observer $U_0$ of four-velocity $(1,\mathbf 0)$ in its rest frame, the electromagnetic energy-momentum tensor produces energy density $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$, Poynting energy flux $\mathbf S = \mathbf E\times\mathbf B/\mu_0$, momentum density $\boldsymbol\varpi_{\text{em}} = \varepsilon_0\mathbf E\times\mathbf B = \mathbf S/c^2$, and Maxwell stress $S^{\text{em}}_{ij} = \varepsilon_0[\tfrac12(E^2 + c^2B^2)\delta_{ij} - E_iE_j - c^2 B_iB_j]$.

---

# Convergent Strategy

**Problem class.** A *compute-the-energetics-of-a-given-field* problem — direct application of the observer-contraction recipe. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for measured energetics: write down $T_{\text{em}}$ for the field, contract with the observer's frame, read off energy density, momentum density, and stress.

**Assumption pattern.** Each part specifies a field; the calculation is then mechanical. The three fields are chosen to illustrate three regimes: *static* ($\mathbf B = 0$, no momentum, no radiation), *null/radiative* (equal electric and magnetic, energy flows at $c$), and *static crossed* (nonzero Poynting *vector* without energy *flow*, the Feynman disk paradox).

**Theorem routing.** For each field: substitute into $\rho_{\text{em}}, \mathbf S, \boldsymbol\varpi_{\text{em}}, S_{ij}$. For Part 1: integrate $\rho_{\text{em}}$ over a spherical shell. For Part 2: verify $E = cB$ and $\mathbf S = \rho_{\text{em}}c\hat{\mathbf n}$, the hallmark of a null field. For Part 3: compute $\mathbf S$ and $\vec\nabla\cdot\mathbf S$, identify the angular-momentum density. For Part 4: use Part 3 as a counterexample.

**Key decision point.** The crux of Part 3 is recognising that a nonzero Poynting vector does *not* imply radiation. Energy flow ($\vec\nabla\cdot\mathbf S \ne 0$) is what radiates; circulating Poynting in a static field carries momentum (and angular momentum) but not net energy. This is the topic page's illegal operation 5, made concrete.

---

# Legal Operations Used

1. **Read off measured quantities by contracting $T$ with the observer's frame** (operation 1): each measured quantity ($\rho_{\text{em}}, \mathbf S, \boldsymbol\varpi, S_{ij}$) is a specific contraction of $T^{\text{em}}$ with $U_0$.

2. **Exploit tracelessness** (operation 6): for the plane wave, $E^2 = c^2B^2$ gives $F^2 = 0$ and the trace term of $T^{\text{em}}$ drops; the wave is a null field.

3. **Use the Poynting vector of a static field with care** (illegal-but-tempting 5): in Part 3, $\mathbf S \ne 0$ but $\vec\nabla\cdot\mathbf S = 0$ — the field stores momentum/angular momentum but does not radiate.

---

# Hints

> [!note]- Hint 1
> Coulomb field: $E^2 = q^2/(4\pi\varepsilon_0)^2/r^4$, $B = 0$, so $\rho_{\text{em}}(r) = \tfrac{\varepsilon_0}{2}E^2 = q^2/(32\pi^2\varepsilon_0 r^4)$. $\mathbf S = 0$ (no magnetic field $\Rightarrow$ no Poynting vector). For the stress: $S_{rr} = \tfrac{\varepsilon_0}{2}E^2 - \varepsilon_0 E_r E_r = -\tfrac{\varepsilon_0}{2}E^2$ (radial tension), $S_{\theta\theta} = \tfrac{\varepsilon_0}{2}E^2$ (azimuthal pressure). The integral: $W = \int_a^\infty \rho_{\text{em}}\cdot 4\pi r^2\,\mathrm dr = q^2/(8\pi\varepsilon_0)\int_a^\infty r^{-2}\,\mathrm dr = q^2/(8\pi\varepsilon_0 a)$.

> [!note]- Hint 2
> Plane wave: $\mathbf B = \hat{\mathbf n}\times\mathbf E/c$, so $|\mathbf B| = E/c$ (B perpendicular to E), giving $c^2B^2 = E^2$ and $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + E^2) = \varepsilon_0 E^2$. Poynting: $\mathbf S = \mathbf E\times\mathbf B/\mu_0 = \mathbf E\times(\hat{\mathbf n}\times\mathbf E)/(\mu_0 c) = E^2\hat{\mathbf n}/(\mu_0 c) = \varepsilon_0 c E^2\hat{\mathbf n} = \rho_{\text{em}}c\hat{\mathbf n}$ (using $\mathbf E\cdot\hat{\mathbf n} = 0$ in the BAC-CAB rule, and $\varepsilon_0\mu_0 c^2 = 1$). Field invariant: $F^2 = 2(B^2 - E^2/c^2)$ — wait, careful: in $c=1$, $F^2 = 2(B^2 - E^2)$, so for the wave $F^2 = 2(E^2/c^2 - E^2) \cdot c^2 / c^2 = 0$ when $E = cB$. The field is null.

> [!note]- Hint 3
> Feynman disk: with $\mathbf E$ radial and $\mathbf B$ dipolar (axial-symmetric about $\boldsymbol m$), $\mathbf E\times\mathbf B$ has *azimuthal* component — Poynting circulates around the magnetic axis. Why $\vec\nabla\cdot\mathbf S = 0$: in a *static* configuration $\partial_t\rho_{\text{em}} = 0$, and Poynting's theorem $\partial_t\rho_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$ with no currents present (charge at rest, no $\mathbf j$) gives $\vec\nabla\cdot\mathbf S = 0$ identically. The angular momentum density $\mathbf L = \mathbf r\times\boldsymbol\varpi_{\text{em}}$ integrated over space gives the *Feynman disk angular momentum* — stored in the field, available to release if the configuration is dismantled.

> [!note]- Hint 4
> Radiation criterion: a nonzero Poynting vector implies *radiation* only if (i) the field is *time-dependent*, so $\partial_t\rho_{\text{em}} \ne 0$, AND (ii) $\mathbf S$ falls as $1/r^2$ at large $r$ (not $1/r^3$ or faster), so the surface flux $\oint\mathbf S\cdot\mathrm d\mathbf A \sim r^2 \cdot 1/r^2$ does not vanish at infinity. The Coulomb field fails (i) — static; the Feynman disk fails both (i) and (ii) — static, and the dipole field falls as $1/r^3$ so $\mathbf S \sim 1/r^5$. The plane wave passes both — time-dependent, energy density constant in the direction of propagation.

---

# Solution

The electromagnetic energy density, Poynting vector, momentum density, and Maxwell stress are obtained by contracting $T^{\text{em}}$ with the observer's four-velocity and frame. For the Coulomb field they give the electrostatic self-energy and the field-line tension/pressure; for the plane wave they give the null-field relation $\mathbf S = \rho_{\text{em}} c\hat{\mathbf n}$; for crossed static fields they expose the Feynman-disk subtlety that a nonzero Poynting vector need not mean radiating energy.

**Step 1: Coulomb field.**

> [!note]- Derivation
> With $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$ and $\mathbf B = 0$,
> $$\rho_{\text{em}}(r) = \frac{\varepsilon_0}{2}E^2 = \frac{\varepsilon_0}{2}\frac{q^2}{(4\pi\varepsilon_0)^2 r^4} = \frac{q^2}{32\pi^2\varepsilon_0 r^4}.$$
> The Poynting vector vanishes: $\mathbf S = \mathbf E\times\mathbf B/\mu_0 = 0$ since $\mathbf B = 0$. So does the momentum density: a static Coulomb field carries energy but no momentum, as expected by spherical symmetry.
>
> The Maxwell stress at a point on the $r$-axis:
> $$S^{\text{em}}_{rr} = \varepsilon_0\!\left[\tfrac12 E^2 - E_r E_r\right] = -\frac{\varepsilon_0}{2}E^2, \qquad S^{\text{em}}_{\theta\theta} = \varepsilon_0\cdot\tfrac12 E^2 = +\frac{\varepsilon_0}{2}E^2.$$
> The negative radial component is a *tension* along field lines (lines under pull, like rubber bands trying to shorten), the positive angular component is a *pressure* across field lines (lines repelling each other sideways). This is the mechanism by which like charges feel their repulsion as a real stress in the field between them: the radial tension is what pulls the field lines from one charge to the other; the lateral pressure between adjacent lines is what pushes the charges apart.
>
> The total field energy outside a cut-off radius $a$:
> $$W = \int_a^\infty \rho_{\text{em}}(r)\,4\pi r^2\,\mathrm dr = \int_a^\infty \frac{q^2}{8\pi\varepsilon_0 r^2}\,\mathrm dr = \frac{q^2}{8\pi\varepsilon_0 a}.$$
> This is the famous **electrostatic self-energy** of a charge $q$ confined within radius $a$. As $a\to 0$ it diverges — the *classical electron radius* $r_e = q^2/(4\pi\varepsilon_0 mc^2)$ is the scale at which this self-energy equals the rest-mass energy $mc^2$, marking the breakdown of the classical point-charge picture.

**Step 2: Plane wave.**

> [!note]- Derivation
> With $\mathbf B = \hat{\mathbf n}\times\mathbf E/c$ and $\mathbf E\cdot\hat{\mathbf n} = 0$:
> $$|\mathbf B|^2 = \frac{|\hat{\mathbf n}\times\mathbf E|^2}{c^2} = \frac{E^2}{c^2}\;(\text{since }\mathbf E\perp\hat{\mathbf n}),$$
> so $c^2B^2 = E^2$ — magnetic and electric energy densities are equal. Hence
> $$\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2) = \varepsilon_0 E^2.$$
> Poynting vector, using $\mathbf E\times(\hat{\mathbf n}\times\mathbf E) = \hat{\mathbf n}(\mathbf E\cdot\mathbf E) - \mathbf E(\hat{\mathbf n}\cdot\mathbf E) = E^2\hat{\mathbf n}$:
> $$\mathbf S = \frac{\mathbf E\times\mathbf B}{\mu_0} = \frac{\mathbf E\times(\hat{\mathbf n}\times\mathbf E)}{\mu_0 c} = \frac{E^2\hat{\mathbf n}}{\mu_0 c} = \varepsilon_0 c E^2\hat{\mathbf n} = \rho_{\text{em}}\,c\,\hat{\mathbf n}.$$
> The energy flows at speed $c$ in direction $\hat{\mathbf n}$, exactly as a photon must. Momentum density $\boldsymbol\varpi_{\text{em}} = \mathbf S/c^2 = \rho_{\text{em}}\hat{\mathbf n}/c$: the wave carries momentum $E/c$ per unit energy — the **radiation pressure** relation.
>
> Field invariant (using $F_{\mu\nu}F^{\mu\nu} = 2(B^2 - E^2/c^2)\cdot c^2 = 2(c^2B^2 - E^2)$, or in $c=1$ units $F^2 = 2(B^2 - E^2)$):
> $$F^2 = 2(c^2B^2 - E^2) = 2(E^2 - E^2) = 0.$$
> The plane wave is a **null field**: $F^2 = 0$. The trace term of $T^{\text{em}}$ drops, leaving only the symmetric quadratic in $F$, and the energy-momentum tensor reduces to $T^{\text{em}}_{\alpha\beta} = \varepsilon_0 F_{\mu\alpha}F^\mu{}_\beta$. This is the source of the simple flux relations and is the hallmark of radiation.

**Step 3: Feynman disk (crossed static fields).**

> [!note]- Derivation
> With both $\mathbf E$ and $\mathbf B$ static and nonzero — say $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$ (Coulomb of point charge $q$) and $\mathbf B$ a dipole field of moment $\boldsymbol m$ —
> $$\mathbf S = \frac{\mathbf E\times\mathbf B}{\mu_0} \ne 0$$
> in general. With both fields axisymmetric about the magnetic axis, $\mathbf S$ has an azimuthal component — energy *appears* to circulate around the magnetic axis.
>
> But this is not radiation. Poynting's theorem $\partial_t\rho_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$ for a *static* field has $\partial_t\rho_{\text{em}} = 0$, and with no free currents present ($\mathbf j = 0$ at the field point) gives $\vec\nabla\cdot\mathbf S = 0$. So although $\mathbf S$ is nonzero, *no net energy crosses any closed surface* — what flows in flows out, and the integrated flux at infinity vanishes.
>
> What *is* nonzero is the **angular momentum density**:
> $$\mathbf L = \mathbf r\times\boldsymbol\varpi_{\text{em}} = \varepsilon_0\,\mathbf r\times(\mathbf E\times\mathbf B),$$
> and its volume integral is the *Feynman disk angular momentum* — angular momentum stored in the field configuration. If the configuration is dismantled (the charge moved away, the magnet shut off), this angular momentum must be released, and the resulting torque accounts for known mechanical effects (the Feynman disk thought experiment, in which a charged ring on a turntable starts to rotate when a current is switched off). The field carries *momentum* (and angular momentum) without carrying net *energy flow* — the seeming paradox dissolves once one distinguishes flow ($\vec\nabla\cdot\mathbf S$) from circulation ($\mathbf S$ itself).

**Step 4: Radiation criterion.**

> [!note]- Derivation
> The diagnostic for radiation is *not* "$\mathbf S \ne 0$" but "$\oint\mathbf S\cdot\mathrm d\mathbf A \ne 0$ on a large sphere", which requires:
> (i) The field is *time-dependent*, so $\partial_t\rho_{\text{em}} \ne 0$ can balance $\vec\nabla\cdot\mathbf S \ne 0$ via Poynting's theorem;
> (ii) $\mathbf S$ falls as $1/r^2$ at large $r$, so the surface integral $\oint\mathbf S\cdot\mathrm d\mathbf A \sim r^2 \cdot 1/r^2$ remains finite as $r\to\infty$.
>
> Cross-check:
> - *Coulomb field.* Static, fails (i). $\mathbf S = 0$ trivially, no radiation.
> - *Plane wave.* Time-dependent, passes (i). $\mathbf S$ is constant in magnitude (locally) — actually for a real beam, $\mathbf S$ falls as $1/r^2$ from an antenna source. Passes (ii). The wave radiates: $\mathbf S$ carries energy to infinity.
> - *Feynman disk.* Static, fails (i). The dipole field falls as $1/r^3$, so $\mathbf S \sim 1/r^5$ — fails (ii) catastrophically. No radiation; $\mathbf S$ stores angular momentum but transports no energy.
>
> The topic page's illegal-but-tempting operation 5 — "nonzero Poynting vector $\Rightarrow$ radiation" — is *false*. Radiation requires the radiative field, which is the $1/r$, time-dependent part of the field, present only when a source accelerates. A static Poynting circulation is angular-momentum storage; a $1/r^2$ Poynting flux at infinity is radiation.

> [!note]- Complete formal solution
> For the static Coulomb field ($\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$, $\mathbf B = 0$): $\rho_{\text{em}} = q^2/(32\pi^2\varepsilon_0 r^4)$, $\mathbf S = 0$, $S_{rr} = -\tfrac{\varepsilon_0}{2}E^2$ (tension), $S_{\theta\theta} = +\tfrac{\varepsilon_0}{2}E^2$ (pressure); the self-energy outside radius $a$ is $W = q^2/(8\pi\varepsilon_0 a)$. For the plane wave ($\mathbf B = \hat{\mathbf n}\times\mathbf E/c$, $\mathbf E\perp\hat{\mathbf n}$): $\rho_{\text{em}} = \varepsilon_0 E^2$, $\mathbf S = \rho_{\text{em}}c\hat{\mathbf n}$, $\boldsymbol\varpi_{\text{em}} = \rho_{\text{em}}\hat{\mathbf n}/c$, and $F^2 = 2(c^2B^2 - E^2) = 0$ — a null field. For the Feynman disk (static charge in static magnetic dipole field): $\mathbf S = \mathbf E\times\mathbf B/\mu_0 \ne 0$ (circulating), but $\vec\nabla\cdot\mathbf S = 0$ identically in the static, source-free region, so no net energy crosses any closed surface — the nonzero Poynting carries angular momentum $\mathbf L = \mathbf r\times\boldsymbol\varpi_{\text{em}}$, not radiating energy. Radiation requires both time-dependence ($\partial_t\rho_{\text{em}} \ne 0$) and a $1/r^2$ tail (radiative $1/r$ field); the Coulomb field and Feynman disk fail at least one of these, the plane wave passes both. $\blacksquare$

---

# Key Takeaways

**Energy density, Poynting vector, momentum density, and Maxwell stress are all contractions of one tensor $T^{\text{em}}$ — and the rest-frame matrix is the right calculational object.** When asked for any electromagnetic energetic quantity — field energy, radiation pressure, force on a surface, momentum carried by a beam — the workflow is the same: write $T^{\text{em}}$ for the field, contract with $U_0$ to get $\rho_{\text{em}}$, with $\perp_{U_0}\otimes U_0$ to get $\boldsymbol\varpi_{\text{em}}$, with $\perp_{U_0}\otimes\perp_{U_0}$ to get $S^{\text{em}}_{ij}$. The Maxwell stress's two qualitatively different pieces — *tension* along field lines (negative diagonal in the radial direction, the field "pulls together" along lines) and *pressure* across them (positive diagonal in the perpendicular direction, lines push each other apart) — are not separate principles but the structure of $S^{\text{em}}_{ij} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)\delta_{ij} - \varepsilon_0(E_iE_j + c^2B_iB_j)$ at a point. The reusable insight: the field-line picture of stress (tension along, pressure across) is *exactly* the trace-and-subtracted-outer-product structure of the Maxwell stress tensor, and recognising this lets you read mechanical consequences (the force on a capacitor plate, the magnetic pressure compressing a plasma) directly from $T^{\text{em}}$.

**The plane wave's $E = cB$ is *the* defining property of radiation, and it manifests as the vanishing of the field invariant $F^2 = 2(c^2B^2 - E^2)$.** A plane wave's electric and magnetic field strengths are not independent; they are locked together by the wave equation, with magnitudes related by $E = cB$ and directions both perpendicular to the propagation. This single relation forces three things at once: the field invariant vanishes (the radiative field is *null*, like a light cone), the trace term of $T^{\text{em}}$ drops, and the Poynting vector points in the propagation direction with magnitude $\rho_{\text{em}}c$ — energy flowing at the speed of light. The reusable diagnostic: any time you suspect a field is radiative, compute $F^2$; if it vanishes, the field is on the light cone (in field space), and the simple radiation formulas apply. This is also the algebraic root of the **radiation pressure** $P = \rho_{\text{em}}$ at normal incidence on an absorber (and $2\rho_{\text{em}}$ at a reflector): the wave delivers momentum density $\rho_{\text{em}}/c$ at speed $c$, exerting force per unit area $\rho_{\text{em}}/c \cdot c = \rho_{\text{em}}$.

**A nonzero Poynting vector in a static configuration carries momentum and angular momentum but not radiating energy — and this distinction is the heart of the Feynman disk paradox.** The naive equation "$\mathbf S \ne 0 \Rightarrow$ energy flows" is wrong. What flows is the *divergence* of $\mathbf S$; the Poynting vector itself can circulate without transporting net energy across any closed surface. The crossed-static-field configuration — a charge in the field of a magnet — has nonzero circulating $\mathbf S$ and stores genuine angular momentum $\mathbf L = \int\varepsilon_0\mathbf r\times(\mathbf E\times\mathbf B)\,\mathrm dV$ in the field, which is released as mechanical angular momentum when the configuration is dismantled (the Feynman disk experiment). The reusable lesson is structural: $\mathbf S$ is *both* the energy flux and ($c^2$ times) the momentum density, and these two roles are *not* identical — momentum density that circulates without flowing energy across surfaces is the hallmark of stored angular momentum. The diagnostic for radiation requires *both* time-dependence and a $1/r^2$ asymptotic tail in $\mathbf S$; either failing kills radiation. The topic page's illegal operation 5 is the formal version of this lesson: scrutinise the Poynting vector before declaring something radiates.
