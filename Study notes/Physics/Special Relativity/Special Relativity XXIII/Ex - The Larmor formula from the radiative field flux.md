---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

The Larmor formula $\mathcal P = q^2 a^2/(6\pi\varepsilon_0 c^3)$ is one of the most consequential equations in physics — it sets the energy budget of every accelerated charge, from a Bohr-orbit electron to an antenna. The exercise is to *derive* it by computing the energy flux of the radiative field through a sphere surrounding the charge, doing every angular integral by hand and tracking why the answer is a Lorentz scalar. Working with $c = 1$ except where $c$ is restored, mostly-minus signature:

1. **The radiative field.** The total field of an accelerated charge splits into a Coulomb-like piece falling as $1/r^2$ and a *radiative* piece falling as $1/r$. Only the latter contributes to radiation at infinity. In the instantaneous rest frame (the frame where the charge is momentarily at rest, $\mathbf V = 0$, with three-acceleration $\mathbf a$), the radiative electric and magnetic fields at a far point $\mathbf r = r\hat{\mathbf n}$ are
$$\mathbf E_{\text{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a), \qquad \mathbf B_{\text{rad}} = \frac{1}{c}\,\hat{\mathbf n}\times\mathbf E_{\text{rad}}.$$
State the angle $\theta$ between $\hat{\mathbf n}$ and $\mathbf a$ and show that $|\mathbf E_{\text{rad}}| = q|a|\sin\theta/(4\pi\varepsilon_0 c^2 r)$.

2. **The Poynting flux.** The radiated power per unit solid angle is the Poynting vector dotted with $\hat{\mathbf n}$, times $r^2$:
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = r^2\,\mathbf S\cdot\hat{\mathbf n} = r^2\,\frac{|\mathbf E_{\text{rad}}|^2}{\mu_0 c}.$$
(For the radiative field $\mathbf E_{\text{rad}}\perp\hat{\mathbf n}$, so $\hat{\mathbf n}\times\mathbf E_{\text{rad}}$ has magnitude $|\mathbf E_{\text{rad}}|$ and $\mathbf S$ is along $\hat{\mathbf n}$ with magnitude $|\mathbf E_{\text{rad}}|^2/(\mu_0 c)$.) Substitute Part 1 to obtain
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = \frac{q^2 a^2\sin^2\theta}{16\pi^2\varepsilon_0 c^3}.$$
This is the **dipole donut**: emission vanishes along the acceleration axis, maximum perpendicular.

3. **Total radiated power.** Integrate over the sphere using $\int_0^\pi\sin^3\theta\,\mathrm d\theta\cdot 2\pi = 8\pi/3$ (the universal angular integral, derivable via $\sin^3\theta = \sin\theta(1-\cos^2\theta)$) to recover the **Larmor formula**
$$\boxed{\;\mathcal P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}\;.}$$

4. **Lorentz invariance.** Express the result in terms of the invariant four-acceleration magnitude $|A|^2 = -A\cdot A$. In the instantaneous rest frame $A = (0, \mathbf a)$, so $|A|^2 = -A\cdot A = \mathbf a\cdot\mathbf a = a^2$. Show that the invariant form
$$\mathcal P = \frac{q^2\,|A|^2}{6\pi\varepsilon_0 c}$$
holds in *every* inertial frame, not just the instantaneous rest frame — and that this is the deep reason the Larmor formula has the Liénard generalisation $\mathcal P = q^2\Gamma^6[\cdots]/(6\pi\varepsilon_0 c^3)$ in arbitrary frames: it is the same invariant $|A|^2$ written in lab variables.

**Recall:**

The exercise rests on the radiative field of an accelerated charge and the Poynting-flux interpretation of radiated power.

![[Thm - Radiation by an Accelerated Charge (Larmor Formula)#Statement]]

The radiative field of a non-relativistic accelerated charge is transverse to the direction of observation ($\mathbf E_{\text{rad}}\perp\hat{\mathbf n}$) and proportional to the component of the acceleration perpendicular to $\hat{\mathbf n}$ — geometrically, $\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a) = (\mathbf a\cdot\hat{\mathbf n})\hat{\mathbf n} - \mathbf a$, whose magnitude is $|\mathbf a|\sin\theta$. The Poynting vector $\mathbf S = \mathbf E\times\mathbf B/\mu_0$ is the energy flux of the [[Def - Energy-Momentum Tensor of the Electromagnetic Field|electromagnetic field]]. The [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm dU/\mathrm d\tau$ is spacelike with $A\cdot U = 0$, and in mostly-minus signature has $|A|^2 = -A\cdot A > 0$.

---

# Convergent Strategy

**Problem class.** A *derive-a-radiation-formula-from-flux* problem. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for radiated power: identify the radiative ($1/r$) part of the field, compute its Poynting vector, integrate over a sphere — the resulting flux is the radiated power. The angular integral $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ does most of the bookkeeping.

**Assumption pattern.** The signpost is "accelerated charge". The instantaneous rest frame ($\mathbf V = 0$, $\mathbf a$ the three-acceleration there) is where the calculation is simplest: the radiative field has the symmetric form $\mathbf E_{\text{rad}}\propto\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)$, exhibiting the dipole donut. The relativistic generalisation comes by recognising the result is an invariant.

**Theorem routing.** Part 1: identify the radiative field's amplitude from the standard Liénard–Wiechert formula in the rest frame, extract the $\sin\theta$ factor. Part 2: compute the Poynting magnitude, get the angular distribution. Part 3: do the $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ integral. Part 4: identify $a^2 = |A|^2 = -A\cdot A$ and lift to invariant form.

**Key decision point.** Three crucial moves. (i) The radiative field is the $1/r$ piece — only it survives at infinity, since the Poynting flux scales as (field)$^2 \cdot r^2$, and a $1/r$ field gives finite flux while $1/r^2$ vanishes. (ii) The angular pattern $\sin^2\theta$ is the *dipole donut*, and the integral $\int\sin^3\theta\,\mathrm d\Omega$ is its signature. (iii) The result is a *Lorentz scalar* depending only on the invariant $|A|^2$, which is what makes the laboratory Liénard formula a relabelling, not new physics.

---

# Legal Operations Used

1. **Compute radiated power as a flux of $T_{\text{em}}$ through a sphere** (operation 7 from the topic page): the energy a charge radiates is $\oint T_{\text{em}}(\,\cdot\,,\hat{\mathbf n})\,\mathrm dS$ over a large sphere; for the radiative null field, the trace term drops, and $\mathbf S = \mathbf E\times\mathbf B/\mu_0$ does all the work.

2. **Express the four-acceleration invariant in laboratory variables** (operation 8): the rest-frame magnitude $a$ is $a^2 = |A|^2 = -A\cdot A$, the invariant magnitude of the four-acceleration. The same scalar in a general frame gives the Liénard $\Gamma^6$ form.

3. **Read the radiative ($1/r$) field as the only contribution at infinity**: the Coulomb ($1/r^2$) piece's Poynting flux falls as $1/r^4 \cdot r^2 = 1/r^2$ and vanishes as $r\to\infty$; only the $1/r$ radiative field survives.

---

# Hints

> [!note]- Hint 1
> Standard fact (from Liénard–Wiechert, instantaneous rest frame): $\mathbf E_{\text{rad}} = \frac{q}{4\pi\varepsilon_0 c^2 r}\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)$. Use the BAC-CAB identity: $\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a) = \hat{\mathbf n}(\hat{\mathbf n}\cdot\mathbf a) - \mathbf a$. The magnitude is $|\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)| = |\mathbf a|\sin\theta$, where $\theta$ is the angle between $\hat{\mathbf n}$ and $\mathbf a$. So $|\mathbf E_{\text{rad}}| = q|a|\sin\theta/(4\pi\varepsilon_0 c^2 r)$.

> [!note]- Hint 2
> $|\mathbf S| = |\mathbf E_{\text{rad}}\times\mathbf B_{\text{rad}}|/\mu_0$. Using $\mathbf B_{\text{rad}} = \hat{\mathbf n}\times\mathbf E_{\text{rad}}/c$ with $\mathbf E_{\text{rad}}\perp\hat{\mathbf n}$ (radiative field is transverse), $|\mathbf B_{\text{rad}}| = |\mathbf E_{\text{rad}}|/c$, so $|\mathbf S| = |\mathbf E_{\text{rad}}|^2/(\mu_0 c)$. Thus $\mathrm d\mathcal P/\mathrm d\Omega = r^2|\mathbf S| = \frac{r^2}{\mu_0 c}|\mathbf E_{\text{rad}}|^2 = \frac{q^2 a^2\sin^2\theta}{16\pi^2\varepsilon_0 c^3}$ (using $\mu_0 c = 1/(\varepsilon_0 c)$).

> [!note]- Hint 3
> Integrate over the sphere: $\mathcal P = \int(\mathrm d\mathcal P/\mathrm d\Omega)\,\mathrm d\Omega = \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\int_0^{2\pi}\mathrm d\phi\int_0^\pi\sin^2\theta\sin\theta\,\mathrm d\theta = \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\cdot 2\pi\cdot\frac{4}{3} = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$. The key integral: $\int_0^\pi\sin^3\theta\,\mathrm d\theta = \int_0^\pi\sin\theta(1-\cos^2\theta)\,\mathrm d\theta = [-\cos\theta + \cos^3\theta/3]_0^\pi = 2 - 2/3 = 4/3$. Times $2\pi$ gives $8\pi/3$, which over the $16\pi^2$ leaves $1/(6\pi)$.

> [!note]- Hint 4
> The result $\mathcal P = q^2 a^2/(6\pi\varepsilon_0 c^3)$ is a number — it does not depend on which observer measured the radiation. In the instantaneous rest frame, $A = (0, \mathbf a)$ (timelike component zero because $A\cdot U = 0$ and $U = (c, \mathbf 0)$ there), so $A\cdot A = \eta_{\mu\nu}A^\mu A^\nu = \eta_{ii}a_i a_i = -a^2$ (mostly-minus has $\eta_{ii} = -1$). Hence $|A|^2 = -A\cdot A = a^2$. The invariant form is $\mathcal P = q^2|A|^2/(6\pi\varepsilon_0 c)$ (using $a^2/c^2 = |A|^2/c^2$, and the inverse $c$ factor from $\mu_0 c$); this holds in every frame. Different frames see different *components* of $A$, but the *magnitude* $|A|^2$ is the same, and so is $\mathcal P$.

---

# Solution

The radiative ($1/r$) field of an accelerated charge in its instantaneous rest frame has transverse electric component $\mathbf E_{\text{rad}}\propto\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)$, magnitude proportional to $a\sin\theta$. Computing the Poynting flux gives the dipole-donut angular pattern $\mathrm d\mathcal P/\mathrm d\Omega\propto\sin^2\theta$; the sphere integral $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ recovers Larmor $\mathcal P = q^2 a^2/(6\pi\varepsilon_0 c^3)$. The invariant content is $\mathcal P = q^2|A|^2/(6\pi\varepsilon_0 c)$ with $|A|^2 = -A\cdot A$, identical in every frame.

**Step 1: The radiative field's transverse structure.**

> [!note]- Derivation
> The total electromagnetic field of an accelerated charge, the Liénard–Wiechert field, separates into two pieces: a "velocity field" tied to the charge and falling as $1/r^2$ (the boosted Coulomb), and an "acceleration field" — the radiative part — falling as $1/r$. In the instantaneous rest frame where the charge has $\mathbf V = 0$ and three-acceleration $\mathbf a$, the radiative electric field at the far point $\mathbf r = r\hat{\mathbf n}$ (retarded time correction absorbed because $V = 0$) is the standard formula
> $$\mathbf E_{\text{rad}}(\mathbf r) = \frac{q}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a),$$
> and the magnetic field is $\mathbf B_{\text{rad}} = (1/c)\hat{\mathbf n}\times\mathbf E_{\text{rad}}$. Using the BAC-CAB vector identity,
> $$\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a) = (\hat{\mathbf n}\cdot\mathbf a)\hat{\mathbf n} - \mathbf a,$$
> the vector inside the cross product is the *negative* of the component of $\mathbf a$ perpendicular to $\hat{\mathbf n}$. Its magnitude is $|\mathbf a|\sin\theta$, where $\theta$ is the angle between $\hat{\mathbf n}$ and $\mathbf a$:
> $$|\mathbf E_{\text{rad}}| = \frac{q|a|\sin\theta}{4\pi\varepsilon_0 c^2 r}.$$
> Crucially, $\mathbf E_{\text{rad}}\perp\hat{\mathbf n}$ (the dot product $\hat{\mathbf n}\cdot(\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)) = 0$ since the result of a cross product is perpendicular to both factors), so the radiative field is *transverse* to the line of sight — the hallmark of a propagating electromagnetic wave.

**Step 2: The angular distribution from the Poynting vector.**

> [!note]- Derivation
> The Poynting vector is $\mathbf S = \mathbf E_{\text{rad}}\times\mathbf B_{\text{rad}}/\mu_0$. Using $\mathbf B_{\text{rad}} = \hat{\mathbf n}\times\mathbf E_{\text{rad}}/c$ and $\mathbf E_{\text{rad}}\perp\hat{\mathbf n}$,
> $$\mathbf E_{\text{rad}}\times(\hat{\mathbf n}\times\mathbf E_{\text{rad}}) = \hat{\mathbf n}(\mathbf E_{\text{rad}}\cdot\mathbf E_{\text{rad}}) - \mathbf E_{\text{rad}}(\hat{\mathbf n}\cdot\mathbf E_{\text{rad}}) = |\mathbf E_{\text{rad}}|^2\,\hat{\mathbf n}$$
> (the second term vanishes by transversality). So
> $$\mathbf S = \frac{|\mathbf E_{\text{rad}}|^2}{\mu_0 c}\,\hat{\mathbf n},$$
> energy flowing radially outward with magnitude proportional to the squared radiative field.
>
> The power radiated per unit solid angle is the flux through an element $r^2\,\mathrm d\Omega$ of the far sphere:
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = r^2\,\mathbf S\cdot\hat{\mathbf n} = \frac{r^2|\mathbf E_{\text{rad}}|^2}{\mu_0 c} = \frac{r^2}{\mu_0 c}\cdot\frac{q^2 a^2\sin^2\theta}{(4\pi\varepsilon_0 c^2 r)^2} = \frac{q^2 a^2\sin^2\theta}{16\pi^2\mu_0\varepsilon_0^2 c^5},$$
> and using $\mu_0\varepsilon_0 c^2 = 1$, i.e. $\mu_0 = 1/(\varepsilon_0 c^2)$,
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = \frac{q^2 a^2\sin^2\theta}{16\pi^2\varepsilon_0 c^3}.$$
> This is the **dipole donut**: zero emission along the acceleration axis ($\theta = 0$ or $\pi$, where $\sin\theta = 0$, geometric "no transverse component"), maximum perpendicular to it ($\theta = \pi/2$). The total pattern looks like a donut with the acceleration axis through the hole.

**Step 3: Total power by sphere integral.**

> [!note]- Derivation
> Integrate the angular distribution over the full sphere:
> $$\mathcal P = \int_0^{2\pi}\!\!\mathrm d\phi\int_0^\pi\frac{\mathrm d\mathcal P}{\mathrm d\Omega}\sin\theta\,\mathrm d\theta = \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\cdot 2\pi\cdot\int_0^\pi\sin^3\theta\,\mathrm d\theta.$$
> The angular integral is universal in radiation problems:
> $$\int_0^\pi\sin^3\theta\,\mathrm d\theta = \int_0^\pi\sin\theta\,(1 - \cos^2\theta)\,\mathrm d\theta = \left[-\cos\theta + \frac{\cos^3\theta}{3}\right]_0^\pi = \left(1 - \frac{1}{3}\right) + \left(1 - \frac{1}{3}\right) = \frac{4}{3}.$$
> Therefore
> $$\mathcal P = \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\cdot 2\pi\cdot\frac{4}{3} = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}.$$
> This is the **Larmor formula** — the total power an accelerated charge radiates, in the instantaneous rest frame. In Heaviside–Lorentz / Gaussian units ($\varepsilon_0 = 1/4\pi$ absorbed into the charge definition), it reads $\mathcal P = 2q^2 a^2/(3c^3)$, the form most physicists first meet.

**Step 4: Lorentz-invariant form.**

> [!note]- Derivation
> The result $\mathcal P = q^2 a^2/(6\pi\varepsilon_0 c^3)$ was derived in the instantaneous rest frame. But $\mathcal P$ is a *scalar* — the radiated power is the energy radiated per unit time, and the radiated four-momentum $\mathrm dp^{\text{rad}}$ is observer-independent (proved by a Stokes argument over matter-free regions between observers' spheres, see [[Thm - Radiation by an Accelerated Charge (Larmor Formula)#Lemma Decomposition|Larmor theorem proof]]). For a single observer, $\mathcal P = \mathrm dE/\mathrm dt = -\langle\mathrm dp^{\text{rad}}, U_0\rangle/\mathrm dt$, and with $\mathrm dt = \Gamma\mathrm d\tau$ and $\langle\mathrm dp^{\text{rad}}, U_0\rangle = \Gamma\cdot\langle\mathrm dp^{\text{rad}}, U\rangle/\langle U, U_0\rangle$ — the two $\Gamma$ factors cancel — so $\mathcal P$ is the same for every observer.
>
> In the rest frame the four-acceleration is $A = (0, \mathbf a)$ (timelike component zero from $A\cdot U = 0$ and $U = (1, \mathbf 0)$ in $c=1$ units). Its squared norm:
> $$A\cdot A = \eta_{\mu\nu}A^\mu A^\nu = 0\cdot 0 + \eta_{ij}a^i a^j = -a^2 \quad(\text{mostly-minus}).$$
> So $|A|^2 := -A\cdot A = a^2 > 0$, and the Larmor formula reads in invariant form
> $$\boxed{\mathcal P = \frac{q^2|A|^2}{6\pi\varepsilon_0 c}}\qquad (\text{equivalently } \tfrac{q^2 a^2}{6\pi\varepsilon_0 c^3} \text{ in rest-frame variables})$$
> (the $c^3$ versus $c$ factor comes from $a^2$ in rest-frame three-acceleration vs. the invariant $|A|^2$ which carries different units; the precise relation depends on whether $A$ is the proper-time derivative of $U$ or of $\mathrm d\mathbf x/\mathrm d\tau$). This is the formula's deep content: only the invariant magnitude of the four-acceleration matters; the formula's value is observer-independent.
>
> In a *general* frame where the charge moves at three-velocity $\mathbf V$ with three-acceleration $\boldsymbol\gamma = \mathrm d\mathbf V/\mathrm dt$, the four-acceleration is $A = (\Gamma^4(\boldsymbol\gamma\cdot\mathbf V)/c, \Gamma^2\boldsymbol\gamma + \Gamma^4(\boldsymbol\gamma\cdot\mathbf V)\mathbf V/c^2)$ (after computing $\mathrm dU/\mathrm d\tau$), with
> $$|A|^2 = -A\cdot A = \Gamma^6\!\left[\boldsymbol\gamma\cdot\boldsymbol\gamma - \frac{(\boldsymbol\gamma\times\mathbf V)^2}{c^2}\right].$$
> Substituting yields the **Liénard formula**
> $$\mathcal P = \frac{q^2}{6\pi\varepsilon_0 c^3}\,\Gamma^6\!\left[\boldsymbol\gamma\cdot\boldsymbol\gamma - \frac{(\boldsymbol\gamma\times\mathbf V)^2}{c^2}\right],$$
> the same invariant power expressed in laboratory variables. The intimidating $\Gamma^6$ is not new physics — it is the kinematic price of expressing the frame-independent $|A|^2$ in three-vectors.

> [!note]- Complete formal solution
> The radiative field in the instantaneous rest frame is $\mathbf E_{\text{rad}} = q\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)/(4\pi\varepsilon_0 c^2 r)$, with magnitude $q a\sin\theta/(4\pi\varepsilon_0 c^2 r)$ — transverse, dipole-pattern. The Poynting flux per unit solid angle is $\mathrm d\mathcal P/\mathrm d\Omega = r^2|\mathbf E_{\text{rad}}|^2/(\mu_0 c) = q^2 a^2\sin^2\theta/(16\pi^2\varepsilon_0 c^3)$. Integrating over the sphere with $\int_0^\pi\sin^3\theta\,\mathrm d\theta\cdot 2\pi = 8\pi/3$ gives the Larmor formula $\mathcal P = q^2 a^2/(6\pi\varepsilon_0 c^3)$. The result is a Lorentz scalar: $a^2 = -A\cdot A = |A|^2$ in mostly-minus is the invariant four-acceleration magnitude, so $\mathcal P = q^2|A|^2/(6\pi\varepsilon_0 c)$ in every frame, and the Liénard $\Gamma^6$ form is $|A|^2$ expressed in lab three-velocity and three-acceleration: $|A|^2 = \Gamma^6[\boldsymbol\gamma\cdot\boldsymbol\gamma - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$. The radiated four-momentum is $\mathrm dp^{\text{rad}} = (q^2|A|^2/6\pi\varepsilon_0)\,U\,\mathrm d\tau$, manifestly observer-independent. $\blacksquare$

---

# Key Takeaways

**Radiation is the energy flux of the radiative ($1/r$) field through a sphere — the recipe is universal.** Whenever an accelerated source produces radiation, the radiated power is the integral of the Poynting vector over a far sphere, with only the $1/r$ part of the field contributing (the $1/r^2$ Coulomb piece's flux falls off as $1/r^2$ at infinity). This pattern recurs everywhere: classical antenna theory, dipole radiation, gravitational radiation (where $h_{\mu\nu} \sim 1/r$ is the radiative metric perturbation and the flux is the Landau–Lifshitz pseudotensor), neutrino radiation from a stellar oscillation. The trigger is "what is the power radiated by this accelerated source"; the strategy is "find the radiative field (the $1/r$ piece), compute its Poynting flux, integrate over a sphere". The reusable bookkeeping is the universal angular integral $\int\sin^3\theta\,\mathrm d\Omega = 8\pi/3$ for dipole patterns — the same number appearing in atomic transition rates, Rayleigh scattering, and Thomson scattering, because they are all dipole radiation in disguise.

**The Larmor formula's deep content is that $\mathcal P$ is a Lorentz scalar — and recognising this prevents the most common error in relativistic radiation problems.** Many students, looking at the Liénard formula $\mathcal P \propto \Gamma^6[\boldsymbol\gamma^2 - (\boldsymbol\gamma\times\mathbf V)^2/c^2]$, conclude "fast charges radiate more". This is wrong. The radiated power depends *only* on the invariant $|A|^2 = -A\cdot A$, and a charge moving at $0.9999c$ in a straight line radiates *exactly nothing*. The $\Gamma^6$ appears because expressing the frame-independent $|A|^2$ in laboratory three-vectors picks up powers of $\Gamma$ — *maintaining* a given laboratory acceleration at high speed requires a large four-acceleration, and that is what the $\Gamma$-factors count. The disciplined workflow: compute $|A|^2 = -A\cdot A$ first, plug into the invariant $\mathcal P = q^2|A|^2/(6\pi\varepsilon_0 c)$, and only at the end expand $|A|^2$ in lab variables if needed. This separates the physics (acceleration radiates) from the kinematics (Lorentz-factor bookkeeping), and prevents the misattribution of velocity-dependence to a primary law.

**The dipole donut $\sin^2\theta$ is the angular signature of all transverse-field radiation, and it appears far beyond the Larmor formula.** The $\sin^2\theta$ pattern in $\mathrm d\mathcal P/\mathrm d\Omega$ originates from $|\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)|^2 = |\mathbf a|^2\sin^2\theta$: the transverse component of the acceleration is what radiates, and "transverse" means $\sin\theta$ in the angle to the acceleration axis. The same pattern governs (i) **classical antenna theory** — a small oscillating dipole, where $\mathbf a$ becomes the dipole moment's second time derivative; (ii) **Thomson scattering** — an oscillating electron driven by an incoming wave, where the scattered radiation has $\sin^2\theta$ pattern relative to the *polarisation* axis; (iii) **atomic E1 transitions** — quantum electric-dipole radiation, with the same angular pattern weighted by atomic matrix elements; (iv) **NMR radiation** — precessing nuclear magnetic moments, where the rotating dipole produces $\sin^2\theta$ around the precession axis. The reusable lesson is that whenever radiation has a *single direction* (an acceleration, a polarisation, a precession axis), the angular pattern is the donut $\sin^2\theta$ in the angle from that axis. The relativistic modifications add beaming-cone factors $(1 - V\cos\theta/c)^{-n}$, but the fundamental $\sin^2\theta$ donut is the slow-source baseline that every radiation pattern starts from.
