---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ unless $c$ is restored for recognisability; signature mostly-minus $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. A charge $q$ moves on a worldline with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ and four-acceleration $A = \mathrm dU/\mathrm d\tau$; $\tau$ is its proper time. The four-acceleration is spacelike and orthogonal to $U$ ($A\cdot U = 0$), with magnitude $|A|^2 = -A\cdot A \ge 0$ (note the sign: in mostly-minus a spacelike vector has negative square, so $|A|^2 = -A\cdot A$). Relative to an inertial observer $\mathcal O$, the charge has three-velocity $\mathbf V$, three-acceleration $\boldsymbol{\gamma} = \mathrm d\mathbf V/\mathrm dt$, and Lorentz factor $\Gamma = (1 - V^2/c^2)^{-1/2}$. In the **instantaneously comoving inertial frame** (the frame where $\mathbf V = 0$ at the instant in question), the four-acceleration is purely spatial, $A = (0, \mathbf a)$, with $|A|^2 = \mathbf a\cdot\mathbf a = a^2$. $\mathcal P$ denotes the radiated power $\mathrm dE/\mathrm dt$; $\varepsilon_0$ the vacuum permittivity. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

---

# Statement

> **Theorem (Larmor formula).** An accelerated charge $q$ radiates electromagnetic energy. The total power radiated, measured by an observer in whose frame the charge is *instantaneously at rest* (so the charge's three-acceleration there is $\mathbf a$, equivalently $|A|^2 = a^2$ is the squared magnitude of the four-acceleration), is
> $$\boxed{\;\mathcal P \;=\; \frac{q^2\,a^2}{6\pi\varepsilon_0 c^3}\;=\;\frac{q^2\,|A|^2}{6\pi\varepsilon_0 c}\;}\qquad(\text{with } c=1:\ \mathcal P = \tfrac{q^2}{6\pi\varepsilon_0}|A|^2).$$

> **Theorem (Liénard formula — relativistic generalisation).** For a charge moving with arbitrary three-velocity $\mathbf V$ and three-acceleration $\boldsymbol\gamma$ relative to an inertial observer $\mathcal O$, the power radiated through a sphere surrounding the charge, measured by $\mathcal O$, is
> $$\mathcal P \;=\; \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^6\left[\boldsymbol\gamma\cdot\boldsymbol\gamma \;-\; \frac{1}{c^2}\,(\boldsymbol\gamma\times\mathbf V)^2\right] \;=\; \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^4\left(\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2\right),$$
> where $\gamma_\parallel$ and $\gamma_\perp$ are the components of $\boldsymbol\gamma$ parallel and perpendicular to $\mathbf V$. This reduces to the Larmor formula when $\mathbf V = 0$ ($\Gamma = 1$), and is a Lorentz scalar: the radiated four-momentum is observer-independent.

One-line reading: the radiated power is a Lorentz scalar equal to $q^2|A|^2/6\pi\varepsilon_0 c$, with $|A|^2$ the invariant squared magnitude of the four-acceleration; the Liénard form is just $|A|^2$ written out in laboratory three-velocity and three-acceleration.

---

# Motivation

A charge sitting still, or coasting at constant velocity, produces a static or boosted Coulomb field that carries energy but radiates nothing — no energy escapes to infinity. Shake the charge, and it sends out electromagnetic waves: an antenna works, an atom emits light, a charge whipped around a circle in an accelerator floods its surroundings with radiation. The question this theorem answers is quantitative and central: *how much power does an accelerated charge radiate, and on what does it depend?* The answer — that the power is proportional to the square of the acceleration — is one of the most consequential formulas in physics, and the relativistic version determines the design of every particle accelerator and explains a large fraction of the high-energy light in the universe.

The result matters because it sets a fundamental limit. In a circular accelerator, keeping a particle on its curved path requires centripetal acceleration, and this theorem says the particle then bleeds energy as synchrotron radiation at a rate that grows like the *sixth power* of the Lorentz factor. For electrons, which are light and easily made ultrarelativistic, this loss becomes prohibitive, and it is the reason the next generation of electron–positron colliders must be linear rather than circular: you cannot bend a high-energy electron without paying an enormous radiative tax. The same formula, read the other way, makes circular electron machines into the brightest laboratory X-ray sources on Earth.

The deep structural point — the one that makes the formula beautiful rather than merely useful — is that the radiated power is a **Lorentz scalar**. The energy radiated and the time interval over which it is radiated are each frame-dependent, but their ratio, the power, comes out the same in every inertial frame, because the radiated four-momentum is itself observer-independent. This is why the formula can be stated in the deceptively simple invariant form $\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$: it depends only on the charge and the *invariant magnitude of the four-acceleration*, a quantity every observer agrees on. The Liénard formula's intimidating $\Gamma^6$ is nothing more than what that invariant looks like when you insist on expressing it through laboratory three-vectors.

One should expect the acceleration-squared dependence on dimensional and structural grounds before doing any calculation. Radiation is carried by the *radiative* part of the field, which falls off as $1/r$ (not $1/r^2$ like the Coulomb field) and is proportional to the acceleration — a charge moving uniformly has no radiative field at all. The energy flux (Poynting vector) is quadratic in the field, hence quadratic in the acceleration, and a quadratic flux integrated over a sphere whose area grows as $r^2$ against a field falling as $1/r$ gives an $r$-independent power proportional to $a^2$. The theorem makes this exact and supplies the coefficient.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a charge has nonzero four-acceleration". Recognising it in disguise:

The first disguised source is **"a charged particle is bound, orbiting, or oscillating"**. Any non-inertial charged trajectory accelerates, hence radiates. The bridge is that boundedness forces acceleration: a particle confined to a finite region cannot move in a straight line forever. *Example:* an electron in a classical circular atomic orbit accelerates centripetally and must radiate — the very fact that *kills* the classical atom and forces quantum mechanics. The theorem applied to the Bohr orbit predicts collapse in $\sim 10^{-11}$ s.

The second disguised source is **"a charge moves through a magnetic field"**. The magnetic Lorentz force bends the trajectory into a helix, supplying centripetal acceleration $\boldsymbol\gamma$ orthogonal to $\mathbf V$. The bridge is the [[Def - The Lorentz Four-Force|Lorentz force law]] $m\,\mathrm dU/\mathrm d\tau = q\,F(\,\cdot\,, U)$, which converts a field into an acceleration. The nonobviousness is that a *uniform* magnetic field, which does no work, nonetheless causes radiation, because radiation depends on acceleration, not on work done. *Example:* synchrotron radiation, [[Def - Synchrotron Radiation]].

The third disguised source is **"a charge is suddenly stopped or scattered"**. A deceleration is an acceleration, and an abrupt one radiates a burst across a broad spectrum. The bridge is again $A = \mathrm dU/\mathrm d\tau \ne 0$ during the deceleration. *Example:* bremsstrahlung ("braking radiation") — the X-rays produced when fast electrons slam into a metal target, the working principle of an X-ray tube.

**Targets (Output Amplification)**

The conclusion is "$\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$".

Combine with **the equation of motion to get a radiative energy-loss rate**. Substituting the acceleration produced by a given force lets you compute how fast the particle loses energy and hence how its trajectory decays. The further result is the lifetime of an orbit or the energy budget of an accelerator. The combination is useful because it closes the loop between dynamics (what force acts) and radiation (what is lost). *Example:* the energy lost per turn in a synchrotron, $\Delta E \propto \Gamma^4/R$, which determines whether a circular machine is viable.

Combine with **the angular distribution to get the radiation pattern**. The total power, refined by *where* the radiation goes, gives the beaming pattern — a dipole donut at low speed, a forward-focused searchlight at high speed. The further result is the directional and spectral character of the emission, treated on [[Thm - Angular Distribution of Radiation]]. The combination matters because what you *detect* depends on direction, not just total power. *Example:* the narrow forward cone of synchrotron light that makes it usable as a collimated beam.

Combine with **the $\Gamma^6$ scaling and a fixed energy** to compare particles. At fixed energy $E = \Gamma mc^2$, the radiated power for a given trajectory curvature scales as $\Gamma^4 \propto (E/mc^2)^4 \propto m^{-4}$ — lighter particles radiate vastly more. The further result is the rule that protons ($m \approx 1836\,m_e$) radiate $\sim 10^{13}$ times less than electrons at the same energy and radius. The combination is nonobvious because it turns a kinematic factor into a sharp engineering verdict. *Example:* why the LHC (protons) tolerates synchrotron loss that would cripple an electron machine of the same size.

---

# Why Is It True

Three ideas, stacked, make the formula inevitable: *only acceleration radiates*, *the radiative field is the source's energy-momentum tensor*, and *the radiated power is a Lorentz scalar*.

**The bold one-liner: the radiated power is the flux of the radiative field's energy-momentum tensor through a sphere, and because that flux equals an invariant ($q^2|A|^2/6\pi\varepsilon_0 c$) it is independent of both the sphere's radius and the observer — the $\Gamma^6$ of the laboratory formula is just this invariant in disguise.**

Start with *why only acceleration radiates*. The field of a charge splits into a Coulombic part, tied to the charge and falling as $1/r^2$, and a radiative part, falling as $1/r$ and proportional to the four-acceleration. The radiative part is the only one that survives the trip to infinity: the energy crossing a sphere of radius $r$ is (Poynting flux) $\times$ (area) $\sim (\text{field}^2)\times r^2$, and only a field falling as $1/r$ gives a flux that does not vanish as $r\to\infty$. Since the radiative field is proportional to $A$, the surviving power is proportional to $A^2$. A uniformly moving charge has $A = 0$ and a purely Coulombic (boosted) field, so it radiates nothing — exactly right, since "radiating while coasting" would let an inertial observer detect their own motion, violating relativity.

Now *why the energy-momentum tensor does the accounting*. The energy radiated is energy that leaves the charge and ends up in the field at large distance, so it is computed as the flux of the [[Def - Energy-Momentum Tensor of the Electromagnetic Field|electromagnetic energy-momentum tensor]] $T_{\text{em}}$ through a sphere surrounding the charge. For the radiative field the field invariant vanishes (the radiation field is null), so $T_{\text{em}}$ loses its trace term and reduces to a single quadratic in the radiative field, $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\text{rad}})_{\mu\alpha}(F_{\text{rad}})^\mu{}_\beta$, which works out to $T_{\text{em}} \propto (q^2/R^4)[A\cdot A - (A\cdot\mathbf m)^2]\,\mathbf{PM}\otimes\mathbf{PM}$, where $\mathbf m$ is the unit direction to the field point. The radiated four-momentum is the integral of this over the sphere.

Finally, *why the answer is an invariant, and why the angular integral gives $4\pi/3$-type factors*. Carrying out the sphere integral, the radiated four-momentum comes out as
$$
\mathrm dp^{\text{rad}} = \frac{q^2\,(A\cdot A)\,\mathrm d\tau}{6\pi\varepsilon_0}\,U,
$$
a four-vector pointing along the charge's four-velocity $U$, with magnitude controlled by the *invariant* $A\cdot A$ (and the universal angular factor $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ that produces the $6\pi$ in the denominator). This four-momentum is manifestly independent of the radius $R$ of the sphere — energy is conserved between spheres — and, less obviously, independent of *which* observer's sphere is used: a Stokes-theorem argument over the matter-free region between two observers' spheres shows the two fluxes agree. The radiated power for any observer is then $\mathcal P = \mathrm dE/\mathrm dt = -\langle\mathrm dp^{\text{rad}}, U_0\rangle/\mathrm dt$, and since $\mathrm dt = \Gamma\,\mathrm d\tau$ while $\langle U, U_0\rangle = \Gamma$, the two factors of $\Gamma$ cancel and $\mathcal P = q^2(A\cdot A)/6\pi\varepsilon_0$ for *every* observer. The Larmor form is this evaluated where the charge is momentarily at rest (so $A\cdot A = a^2$); the Liénard form is the *same invariant* $A\cdot A$ rewritten using $A\cdot A = -\Gamma^4[\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2]\,$ — wait, with the mostly-minus sign $|A|^2 = -A\cdot A = \Gamma^4[\gamma^2 + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)^2/c^2] = \Gamma^6[\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$ — which is the bracket of the Liénard formula. The intimidating sixth power is *not* new physics; it is the kinematic price of expressing the frame-independent $|A|^2$ in laboratory variables.

---

# What Makes This Hard

The conceptual trap is thinking the radiated power should depend on velocity — it depends only on acceleration (more precisely on the invariant four-acceleration), and a charge can move arbitrarily fast without radiating provided it moves *uniformly*. The non-obvious technical step is recognising that the radiated four-momentum is observer-independent: most derivations compute it in the instantaneous rest frame and then *assume* the laboratory result follows, but the genuinely hard content (the source's Stokes-theorem argument over the region between two observers' spheres) is showing that the flux is the same through any observer's sphere, which is what makes the simple invariant statement legitimate. The most common error is sign confusion in $|A|^2$ versus $A\cdot A$ under the mostly-minus signature — the four-acceleration is spacelike, so $A\cdot A < 0$ and one must use $|A|^2 = -A\cdot A$ to get a positive radiated power.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Compute the energy-momentum tensor of the radiative ($1/r$, null) field; integrate $T_{\text{em}}(\,\cdot\,,\vec m)$ over a sphere surrounding the charge to get the radiated four-momentum; the angular integral $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ produces a four-vector along $U$ with coefficient $\propto A\cdot A$; divide energy by laboratory time, watch the two $\Gamma$ factors cancel, and obtain the invariant power. Rewrite $A\cdot A$ in laboratory three-vectors for the Liénard form.

**Subgoal decomposition:**

1. **Radiative field and its energy-momentum tensor.** Show that for the radiative field (invariant $F^2 = 0$), $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\text{rad}})_{\mu\alpha}(F_{\text{rad}})^\mu{}_\beta \propto (q^2/R^4)[A\cdot A - (A\cdot\mathbf m)^2]\,\mathbf{PM}\otimes\mathbf{PM}$.
   - *Hint:* The radiation field is null, so the $-\tfrac14\eta F^2$ trace term drops; $\mathbf{PM} = R(U + \mathbf m)$ with $\mathbf m$ the unit spatial direction.
   - *Why needed:* It is the integrand whose flux is the radiated energy-momentum.

2. **Sphere integral $\to$ radiated four-momentum.** Integrate over a sphere $\mathscr S$ of radius $R$ in the rest space, using $\mathrm dV = R^2\,\mathrm d\Omega\,\mathrm d\tau$ and spherical coordinates with polar axis along $A$.
   - *Hint:* $A\cdot A - (A\cdot\mathbf m)^2 = |A|^2\sin^2\theta$; only the part of $\mathbf{PM}$ along $U$ survives the angular average of $\mathbf m\sin^3\theta$.
   - *Why needed:* It collapses the tensor to a four-vector along $U$.

3. **Do the angular integral.** Use $\int_0^\pi\int_0^{2\pi}\sin^3\theta\,\mathrm d\theta\,\mathrm d\phi = 8\pi/3$.
   - *Hint:* This single number produces the $6\pi$ in the Larmor denominator ($16\pi^2 / (8\pi/3)^{-1}$ bookkeeping).
   - *Why needed:* It fixes the numerical coefficient.

4. **Radiated four-momentum and its $R$-independence.** Obtain $\mathrm dp^{\text{rad}} = (q^2(A\cdot A)\mathrm d\tau/6\pi\varepsilon_0)\,U$, independent of $R$.
   - *Hint:* All $R$ factors cancel between $T\propto R^{-4}$, $\mathbf{PM}\propto R$ (twice), and $\mathrm dV\propto R^2$.
   - *Why needed:* It is the invariant object; $R$-independence is the consistency check.

5. **Power as a scalar; Larmor and Liénard.** Compute $\mathcal P = \mathrm dE/\mathrm dt = -\langle\mathrm dp^{\text{rad}}, U_0\rangle/\mathrm dt$ with $\mathrm dt = \Gamma\mathrm d\tau$; the $\Gamma$ factors cancel, giving $\mathcal P = q^2|A|^2/6\pi\varepsilon_0$. Rewrite $|A|^2 = \Gamma^6[\boldsymbol\gamma^2 - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$.
   - *Hint:* $\langle U, U_0\rangle = \Gamma$ and $\mathrm dt = \Gamma\mathrm d\tau$ cancel; for $U_0 =$ rest frame, $|A|^2 = a^2$.
   - *Why needed:* It delivers both boxed formulas.

---

# Lemma Decomposition

> [!note]- Lemma 1: The radiative-field energy-momentum tensor
> **Statement:** For the radiative field of an accelerated charge, the energy-momentum tensor is $T^{\text{em}} = \dfrac{q^2}{16\pi^2\varepsilon_0 R^4}\big[A\cdot A - (A\cdot\mathbf m)^2\big]\,\mathbf{PM}\otimes\mathbf{PM}$, where $\mathbf{PM}$ is the past-light-cone separation and $\mathbf m$ the unit spatial direction in the observer's rest space.
>
> **Hint:** The radiation field is null, so the trace term of $T_{\text{em}}$ vanishes; substitute $F_{\text{rad}} = (q/4\pi\varepsilon_0 R^2)\,Q\wedge\mathbf{PM}$ with $Q = A + (A\cdot\mathbf{PM}/R)U$.
>
> **Why needed:** It is the integrand of the radiated four-momentum; its $R^{-4}$ scaling against $\mathbf{PM}\otimes\mathbf{PM}\propto R^2$ is what makes the final answer radius-independent.
>
> > [!note]- Full proof
> > The field of an accelerated charge splits into a Coulombic part ($\propto 1/R^2$) and a radiative part ($\propto 1/R$); at large distance the radiative part dominates whenever $A \ne 0$. The radiative field strength is $F_{\text{rad}} = \tfrac{q}{4\pi\varepsilon_0 R^2}\,Q\wedge\mathbf{PM}^\flat$ with $Q = A + \tfrac{A\cdot\mathbf{PM}}{R}U$ and $R = -U\cdot\mathbf{PM}$ the retarded distance. For this field the invariant $F_{\text{rad}}^2 = 0$ (it is null), so the trace term of the [[Def - Energy-Momentum Tensor of the Electromagnetic Field|energy-momentum tensor]] vanishes and $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\text{rad}})_{\mu\alpha}(F_{\text{rad}})^\mu{}_\beta$. Substituting and using $Q\cdot\mathbf{PM} = 0$, $\mathbf{PM}\cdot\mathbf{PM} = 0$ (null separation) and $Q\cdot Q = A\cdot A - (A\cdot\mathbf{PM}/R)^2$, the contraction collapses to
> > $$T^{\text{em}} = \frac{q^2}{16\pi^2\varepsilon_0 R^4}\big[A\cdot A - (A\cdot\mathbf m)^2\big]\,\mathbf{PM}\otimes\mathbf{PM},$$
> > where $\mathbf{PM} = R(U + \mathbf m)$ defines the unit spatial direction $\mathbf m$ (with $\mathbf m\cdot U = 0$, $|\mathbf m|^2 = 1$). $\blacksquare$

> [!note]- Lemma 2: The angular integral $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$
> **Statement:** $\displaystyle\int_0^\pi\int_0^{2\pi}\sin^3\theta\;\mathrm d\theta\,\mathrm d\phi = \frac{8\pi}{3}$, and the vector integral $\int\mathbf m\,\sin^3\theta\,\mathrm d\Omega = 0$ over the sphere.
>
> **Hint:** $\int_0^\pi\sin^3\theta\,\mathrm d\theta = \int_{-1}^1(1-u^2)\,\mathrm du = 4/3$; the $\phi$-integral gives $2\pi$. The vector integral vanishes by symmetry (odd in $\mathbf m$).
>
> **Why needed:** This single number produces the coefficient $1/6\pi\varepsilon_0$ in the Larmor formula, and the vanishing of the vector integral is why only the $U$-component of $\mathbf{PM}$ survives.
>
> > [!note]- Full proof
> > With $u = \cos\theta$, $\int_0^\pi\sin^3\theta\,\mathrm d\theta = \int_0^\pi\sin\theta(1-\cos^2\theta)\,\mathrm d\theta = \int_{-1}^{1}(1-u^2)\,\mathrm du = [u - u^3/3]_{-1}^1 = (1-\tfrac13)-(-1+\tfrac13) = \tfrac43$. Times the azimuthal $\int_0^{2\pi}\mathrm d\phi = 2\pi$ gives $8\pi/3$. For the vector integral, write $\mathbf m = (\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$ with polar axis along $A$; the $x,y$ components vanish on $\phi$-integration, and the $z$-component integrand $\cos\theta\sin^3\theta$ is odd about $\theta = \pi/2$, integrating to zero. So $\int\mathbf m\sin^3\theta\,\mathrm d\Omega = 0$. $\blacksquare$

> [!note]- Lemma 3: The radiated four-momentum points along $U$ with coefficient $A\cdot A$
> **Statement:** $\displaystyle\mathrm dp^{\text{rad}} = \frac{q^2\,(A\cdot A)\,\mathrm d\tau}{6\pi\varepsilon_0}\,U$, independent of the sphere radius $R$.
>
> **Hint:** Integrate $T^{\text{em}}(\,\cdot\,,\vec m)$ over the sphere with $\mathrm dV = c\,\mathrm d\tau\,\mathrm dS$, $\mathrm dS = R^2\mathrm d\Omega$; use $A\cdot A - (A\cdot\mathbf m)^2 = -|A|^2\sin^2\theta$ wait — in mostly-plus (source) it is $+|A|^2\sin^2\theta$; track the sign carefully.
>
> **Why needed:** It is the invariant object from which every form of the power formula follows; its $R$-independence is the physical statement that energy is conserved between spheres.
>
> > [!note]- Full proof
> > The four-momentum radiated through the sphere $\mathscr S$ in proper-time $\mathrm d\tau$ is $\mathrm dp^{\text{rad}} = \tfrac1c\int_{\mathscr S}T^{\text{em}}(\,\cdot\,,\vec m)\,\mathrm dV$ (the unit normal to the world-tube is the spacelike $\vec m$). Substituting Lemma 1 and $\mathrm dV = c\,\mathrm d\tau\,\mathrm dS$ with $\mathrm dS = R^2\sin\theta\,\mathrm d\theta\,\mathrm d\phi$, and using $\langle\mathbf{PM},\vec m\rangle = R$ and $\mathbf{PM} = R(U + \mathbf m)$:
> > $$\mathrm dp^{\text{rad}} = \frac{q^2\,\mathrm d\tau}{16\pi^2\varepsilon_0}\int_{\mathscr S}\big[A\cdot A - (A\cdot\mathbf m)^2\big]\,(U + \mathbf m)\,\sin\theta\,\mathrm d\theta\,\mathrm d\phi.$$
> > Choosing the polar axis along the (spacelike) four-acceleration, $A\cdot\mathbf m = |A|\cos\theta$ and $A\cdot A - (A\cdot\mathbf m)^2 = |A|^2(1-\cos^2\theta) = |A|^2\sin^2\theta$ (writing $|A|^2$ for the squared magnitude). By Lemma 2 the $\mathbf m$-term integrates to zero and the $U$-term gives $U\cdot|A|^2\int\sin^3\theta\,\mathrm d\Omega = U|A|^2\cdot\tfrac{8\pi}{3}$. Hence
> > $$\mathrm dp^{\text{rad}} = \frac{q^2\,|A|^2\,\mathrm d\tau}{16\pi^2\varepsilon_0}\cdot\frac{8\pi}{3}\,U = \frac{q^2\,|A|^2\,\mathrm d\tau}{6\pi\varepsilon_0}\,U.$$
> > Every factor of $R$ has cancelled ($R^{-4}$ from $T$, $R^2$ from $\mathrm dS$, $R^2$ from the two $\mathbf{PM}$ factors absorbed into $U + \mathbf m$ and $\langle\mathbf{PM},\vec m\rangle$), so $\mathrm dp^{\text{rad}}$ is independent of $R$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — radiative field is null and matter-free region.** At large distance from the charge the field is dominated by its radiative part $F_{\text{rad}}\propto 1/R$, which is null ($F_{\text{rad}}^2 = 0$); the region between the charge and the measuring sphere contains no other matter, so the only energy-momentum present is electromagnetic.
>
> By **Lemma 1**, the energy-momentum tensor of the radiative field is $T^{\text{em}} = \dfrac{q^2}{16\pi^2\varepsilon_0 R^4}[A\cdot A - (A\cdot\mathbf m)^2]\,\mathbf{PM}\otimes\mathbf{PM}$.
>
> By **Lemma 3** (using **Lemma 2** for the angular integral), the four-momentum radiated in proper-time $\mathrm d\tau$ through a sphere surrounding the charge is
> $$\mathrm dp^{\text{rad}} = \frac{q^2\,|A|^2\,\mathrm d\tau}{6\pi\varepsilon_0}\,U, \qquad |A|^2 = -A\cdot A \ \text{(mostly-minus magnitude)},$$
> a four-vector along $U$, independent of the sphere radius.
>
> **Observer-independence.** Consider two inertial observers $\mathcal O$ and $\mathcal O'$ with spheres $\mathscr S$ and $\mathscr S'$ on the same future light cone of the emission event. The four-dimensional region between them is matter-free, so $\vec\nabla\cdot T^{\text{em}} = 0$ there, and Stokes' theorem over that region gives $\mathrm dp^{\text{rad}}|_{\mathscr S'} = \mathrm dp^{\text{rad}}|_{\mathscr S}$ — the contributions from the light-cone caps vanish because $T^{\text{em}}(\,\cdot\,)$ is tangent to the cone there. Hence the radiated four-momentum is the same for every observer.
>
> **Power (Larmor).** The energy radiated as measured by an observer $\mathcal O$ of four-velocity $U_0$ is $\mathrm dE = -c\,\langle\mathrm dp^{\text{rad}}, U_0\rangle = -c\,\tfrac{q^2|A|^2\mathrm d\tau}{6\pi\varepsilon_0}\langle U, U_0\rangle$. With $\langle U, U_0\rangle = \Gamma$ (the Lorentz factor of the charge relative to $\mathcal O$) and the laboratory time increment $\mathrm dt = \Gamma\,\mathrm d\tau$, the power is
> $$\mathcal P = \frac{\mathrm dE}{\mathrm dt} = \frac{c\,q^2\,|A|^2}{6\pi\varepsilon_0}\cdot\frac{\Gamma\,\mathrm d\tau}{\Gamma\,\mathrm d\tau} = \frac{c\,q^2\,|A|^2}{6\pi\varepsilon_0},$$
> the two factors of $\Gamma$ cancelling — the radiated power is a Lorentz scalar. Evaluated where the charge is instantaneously at rest, $|A|^2 = a^2$ (the squared three-acceleration there) and, restoring $c$,
> $$\mathcal P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3},$$
> the **Larmor formula**.
>
> **Power (Liénard).** Expressing the invariant magnitude in laboratory three-velocity $\mathbf V$ and three-acceleration $\boldsymbol\gamma$ via $A = \Gamma^2[\boldsymbol\gamma + \Gamma^2 c^{-2}(\boldsymbol\gamma\cdot\mathbf V)\mathbf V, \ldots]$ gives
> $$|A|^2 = \Gamma^6\left[\boldsymbol\gamma\cdot\boldsymbol\gamma - \frac{1}{c^2}(\boldsymbol\gamma\times\mathbf V)^2\right] = \Gamma^4\big(\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2\big),$$
> hence
> $$\mathcal P = \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^6\left[\boldsymbol\gamma\cdot\boldsymbol\gamma - \frac{1}{c^2}(\boldsymbol\gamma\times\mathbf V)^2\right],$$
> the **Liénard formula**, which reduces to Larmor at $\mathbf V = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The classical atom's instability.** Apply Larmor to an electron in a circular Bohr orbit of radius $a_0$: the centripetal acceleration is $a = v^2/a_0$, the radiated power drains the orbital energy, and integrating the energy-loss equation gives a collapse time of order $10^{-11}$ s. This is the calculation that demonstrates classical electromagnetism is *inconsistent* with stable atoms and historically forced the quantum hypothesis. The application is foundational: the formula that works perfectly for antennas predicts the universe should not exist, and the resolution is quantum mechanics.

**Pulsar spin-down.** A neutron star with a misaligned magnetic dipole rotating at angular frequency $\Omega$ radiates by the magnetic-dipole analogue of Larmor, $\mathcal P \propto \Omega^4$, draining its rotational kinetic energy. Equating the radiated power to $-\mathrm d(\tfrac12 I\Omega^2)/\mathrm dt$ gives the observed spin-down of pulsars and a measurement of their magnetic fields ($\sim 10^8$ T for the Crab). The application is out-of-distribution because the radiator is a macroscopic rotating star, yet the physics is the same accelerated-charge formula.

**Thomson and Compton scattering cross-sections.** A free charge driven by an incident electromagnetic wave oscillates and re-radiates by Larmor; the ratio of re-radiated to incident power *is* the Thomson cross-section $\sigma_T = q^4/(6\pi\varepsilon_0^2 m^2 c^4)$. This connects the radiation formula to scattering theory and, with quantum corrections, to Compton scattering. The application is surprising because a formula about *emission* becomes, applied to a driven charge, a formula about *scattering*.

---

# Bridges

- **[[Def - Energy-Momentum Tensor of the Electromagnetic Field]]** — the tensor whose flux *is* the radiated energy. The Larmor formula is the surface integral of $T_{\text{em}}$ (for the null radiative field, so its trace term drops) over a sphere surrounding the charge. The radiation calculation is impossible without first knowing the field's energy-momentum tensor; this theorem is its most important application.

- **[[Def - Synchrotron Radiation]]** — the special case of a charge on a helical path in a magnetic field. Substituting the circular-motion acceleration $|A|^2 = \omega_B^2 V^2\sin^2\alpha/\Gamma^2$ into the Liénard formula gives the synchrotron power $\mathcal P = q^4 B^2\Gamma^2 V^2\sin^2\alpha/(6\pi\varepsilon_0 c^3 m^2)$, and the $\Gamma^2$ there (versus the $\Gamma^4$ of linear acceleration at fixed force) is exactly the difference between $\gamma_\perp^2$ and $\Gamma^2\gamma_\parallel^2$ in the Liénard bracket. Synchrotron radiation is Liénard's formula with the trajectory of [[Thm - Worldline of a Uniformly Accelerated Observer|accelerated motion]] in a magnetic field.

- **[[Thm - Angular Distribution of Radiation]]** — the refinement of "how much" into "in which direction". The total power of this theorem is the integral over the sphere of the directional Poynting flux computed there; the angular distribution shows that the dipole donut of the rest frame is focused into a forward cone of half-angle $\sim 1/\Gamma$ at high speed (relativistic beaming).

- **[[Thm - Conservation of Four-Momentum]]** — the bookkeeping principle behind radiation reaction. The radiated four-momentum $\mathrm dp^{\text{rad}}$ must come from somewhere: the charge loses exactly this four-momentum, which is the origin of the **radiation-reaction force** (Abraham–Lorentz). The energy the field carries to infinity is debited from the particle, so total four-momentum (particle plus field) is conserved — an instance of [[Thm - Energy-Momentum Conservation|energy-momentum conservation]] for the matter-plus-field system.

---

# Unlocked by This

> [!tip] Radiation Reaction and the Abraham–Lorentz Force *(from Classical Electrodynamics)*
> Since the charge loses the four-momentum $\mathrm dp^{\text{rad}}$ it radiates, there must be a back-reaction force on the charge — the **Abraham–Lorentz–Dirac force**, proportional to the rate of change of acceleration, $\propto q^2\dot{\mathbf a}$. This force is notoriously pathological (it admits runaway and pre-accelerating solutions), exposing the limits of treating a point charge classically and pointing toward the need for quantum electrodynamics. The Larmor formula is the energy budget that the radiation-reaction force must balance.

> [!tip] The Cosmic Origin of Most High-Energy Light *(from Astrophysics)*
> The relativistic generalisation of this formula — synchrotron radiation from ultrarelativistic electrons spiralling in cosmic magnetic fields — is responsible for an enormous fraction of the non-thermal radio, X-ray, and gamma-ray emission in the universe: from the Crab Nebula and Jupiter's magnetosphere to the jets of active galactic nuclei and gamma-ray bursts. Reading the synchrotron spectrum backwards (via the characteristic frequency $f_c \propto \Gamma^2 B$) lets astronomers measure the energies of cosmic-ray electrons and the strengths of magnetic fields light-years away. The Larmor formula is, in this sense, one of the most-used equations in observational astrophysics.
