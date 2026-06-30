---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Thomas Equation"
  - "Def - Thomas Precession"
  - "Def - Spin Four-Vector"
tags: [physics, special-relativity]
---

# Problem Statement

A free gyroscope is carried on a uniform circular orbit of radius $R$ and angular velocity $\Omega$ (with $R\Omega < c$) in the plane $(x_*, y_*)$ of the inertial observer $\mathcal{O}_*$. Its spin is Fermi–Walker transported (torque-free). Working with $c = 1$ except where restored:

1. Write the gyroscope's velocity $\mathbf{V}$ and acceleration $\boldsymbol\gamma$ relative to $\mathcal{O}_*$, and confirm $\boldsymbol\gamma \perp \mathbf{V}$ (centripetal acceleration), so Thomas precession occurs.
2. Substitute into the Thomas precession rate $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$ (equivalently $\frac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V}$) to obtain $\vec\omega_T = -(\Gamma - 1)\Omega\,\mathbf{e}_3^*$.
3. Show the precession is *opposite* to the orbital sense, and amounts to a lag of $2\pi(\Gamma - 1)$ per revolution.
4. Take the low-velocity limit and obtain $\vec\omega_T \simeq -\tfrac12(R\Omega/c)^2\,\Omega\,\mathbf{e}_3^*$.

**Recall:**

![[Thm - The Thomas Equation#Statement]]

For a free gyroscope ($\vec C = 0$), the stopped spin $\mathbf{s}_*$ precesses at $\vec\omega_T$: $\mathrm{d}\mathbf{s}_*/\mathrm{d}t_* = \vec\omega_T\times\mathbf{s}_*$. The [[Def - Thomas Precession|Thomas precession]] occurs whenever the acceleration is *not* collinear with the velocity, $\boldsymbol\gamma\times\mathbf{V}\neq 0$. $\Gamma = (1 - V^2/c^2)^{-1/2}$ is the Lorentz factor of the gyroscope relative to $\mathcal{O}_*$; for circular motion $V = R\Omega$ is constant. The identity $\Gamma^2/(1+\Gamma) = (\Gamma-1)c^2/V^2$ relates the two forms of $\vec\omega_T$.

---

# Convergent Strategy

**Problem class.** A *compute-a-precession* problem, the fifth class in the [[Special Relativity XVI — Accelerated Observers#Problem-Solving Strategy|topic strategy]]: substitute a concrete orbit into the Thomas precession rate and extract the physical consequence (the lag per revolution). The decisive move is to compute $\boldsymbol\gamma\times\mathbf{V}$ for circular motion.

**Assumption pattern.** Uniform circular motion: $V = R\Omega$ constant, $\boldsymbol\gamma = -R\Omega^2\hat{\mathbf{r}}$ centripetal, $\boldsymbol\gamma\perp\mathbf{V}$. The signpost that Thomas precession occurs is exactly this perpendicularity — the acceleration is not collinear with the velocity, so $\boldsymbol\gamma\times\mathbf{V}\neq 0$. The constancy of $V$ (hence $\Gamma$) makes $\vec\omega_T$ constant, so the precession is steady.

**Theorem routing.** The route is: circular orbit $\Rightarrow$ $\mathbf{V}, \boldsymbol\gamma$ explicit $\Rightarrow$ $\boldsymbol\gamma\times\mathbf{V} = R^2\Omega^3\,\mathbf{e}_3^*$ (with a sign) $\Rightarrow$ substitute into $\vec\omega_T = \frac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V}$ with $V^2 = R^2\Omega^2$ $\Rightarrow$ $\vec\omega_T = -(\Gamma-1)\Omega\,\mathbf{e}_3^*$ ([[Thm - The Thomas Equation|Thomas equation, free-gyroscope corollary]]). The lag per revolution is $|\vec\omega_T|\cdot(2\pi/\Omega) = 2\pi(\Gamma-1)$.

**Key decision point.** The crux is the *sign*: the Thomas precession is *opposite* to the orbital rotation, $\vec\omega_T \propto \boldsymbol\gamma\times\mathbf{V}$ (acceleration cross velocity, pointing along $-\mathbf{e}_3^*$ for counterclockwise orbit), so the gyroscope *lags* the orbital motion. The trap is to compute $\mathbf{V}\times\boldsymbol\gamma$ instead and get the wrong sign. The lag $2\pi(\Gamma-1)$ per revolution is a *holonomy* — a net rotation accumulated around a closed loop in velocity space, independent of the timing.

---

# Legal Operations Used

1. **Decompose a composition of boosts as boost-times-rotation** (operation 7 from the topic page). The Thomas precession rate $\vec\omega_T$ used here is the differential of the residual [[Def - Thomas Rotation|Thomas rotation]] from composing the boosts along the orbit; the gyroscope's spin picks up this rotation continuously.

2. **Fermi–Walker transport a vector along the worldline** (operation 5 from the topic page). The gyroscope's spin is Fermi–Walker transported (torque-free), so $\vec C = 0$ and the [[Thm - The Thomas Equation|Thomas equation]] reduces to the pure precession $\mathrm{d}\mathbf{s}_*/\mathrm{d}t_* = \vec\omega_T\times\mathbf{s}_*$.

3. **Take the low-velocity / small-distance limit** (operation 9 from the topic page). Expanding $\Gamma - 1 \approx \tfrac12 V^2/c^2 = \tfrac12(R\Omega/c)^2$ gives the low-velocity precession $\vec\omega_T \simeq -\tfrac12(R\Omega/c)^2\Omega\,\mathbf{e}_3^*$.

---

# Hints

> [!note]- Hint 1
> Parametrise the orbit by $\mathcal{O}_*$'s time: $\mathbf{r}(t_*) = R(\cos\Omega t_*, \sin\Omega t_*, 0)$. Then $\mathbf{V} = \dot{\mathbf{r}} = R\Omega(-\sin\Omega t_*, \cos\Omega t_*, 0)$ and $\boldsymbol\gamma = \ddot{\mathbf{r}} = -R\Omega^2(\cos\Omega t_*, \sin\Omega t_*, 0)$. Check $\boldsymbol\gamma\cdot\mathbf{V} = 0$: the acceleration is centripetal, perpendicular to the velocity. Since $\boldsymbol\gamma\times\mathbf{V}\neq 0$, Thomas precession occurs.

> [!note]- Hint 2
> Compute the cross product: $\boldsymbol\gamma\times\mathbf{V} = (-R\Omega^2\hat{\mathbf{r}})\times(R\Omega\,\hat{\boldsymbol\theta})$. With $\hat{\mathbf{r}}\times\hat{\boldsymbol\theta} = \mathbf{e}_3^*$, this is $-R^2\Omega^3\,\mathbf{e}_3^*$. Now $V^2 = R^2\Omega^2$, so using $\vec\omega_T = \frac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V} = \frac{\Gamma-1}{R^2\Omega^2}(-R^2\Omega^3\mathbf{e}_3^*) = -(\Gamma-1)\Omega\,\mathbf{e}_3^*$.

> [!note]- Hint 3
> The orbital angular velocity is $+\Omega\,\mathbf{e}_3^*$ (counterclockwise). The Thomas precession is $\vec\omega_T = -(\Gamma-1)\Omega\,\mathbf{e}_3^*$ — *opposite* sign, so the gyroscope precesses clockwise, *against* the orbit. Over one orbital period $T = 2\pi/\Omega$, the gyroscope's spin rotates by $|\vec\omega_T|T = (\Gamma-1)\Omega\cdot(2\pi/\Omega) = 2\pi(\Gamma-1)$ — a lag relative to a direction fixed in $\mathcal{O}_*$.

> [!note]- Hint 4
> For $R\Omega\ll c$: $\Gamma = (1 - R^2\Omega^2/c^2)^{-1/2}\approx 1 + \tfrac12 R^2\Omega^2/c^2$, so $\Gamma - 1\approx\tfrac12(R\Omega/c)^2$. Hence $\vec\omega_T\simeq -\tfrac12(R\Omega/c)^2\,\Omega\,\mathbf{e}_3^*$. This is the rate that, applied to an atomic electron, gives the Thomas half.

---

# Solution

A gyroscope carried around a circle precesses against the orbital sense at a rate $(\Gamma-1)\Omega$. Step 1 writes the orbital kinematics and confirms the perpendicularity that triggers the precession. Step 2 substitutes into the Thomas rate. Step 3 reads off the sign and the per-revolution lag. Step 4 takes the low-velocity limit. The non-obvious content is the sign (precession opposite to orbit) and the recognition of the lag as a holonomy.

**Step 1: $\mathbf{V} = R\Omega\hat{\boldsymbol\theta}$, $\boldsymbol\gamma = -R\Omega^2\hat{\mathbf{r}}$, with $\boldsymbol\gamma\perp\mathbf{V}$.**

> [!note]- Derivation
> Parametrise the circular orbit in $\mathcal{O}_*$'s rest space by inertial time $t_*$:
> $$\mathbf{r}(t_*) = R(\cos\Omega t_*,\ \sin\Omega t_*,\ 0).$$
> The velocity and acceleration relative to $\mathcal{O}_*$ are
> $$\mathbf{V} = \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}t_*} = R\Omega(-\sin\Omega t_*,\ \cos\Omega t_*,\ 0) = R\Omega\,\hat{\boldsymbol\theta}, \qquad \boldsymbol\gamma = \frac{\mathrm{d}^2\mathbf{r}}{\mathrm{d}t_*^2} = -R\Omega^2(\cos\Omega t_*,\ \sin\Omega t_*,\ 0) = -R\Omega^2\,\hat{\mathbf{r}}.$$
> The acceleration is *centripetal* (pointing inward, $-\hat{\mathbf{r}}$), and $\boldsymbol\gamma\cdot\mathbf{V} = -R^2\Omega^3(\cos\Omega t_*\,(-\sin\Omega t_*) + \sin\Omega t_*\cos\Omega t_*) = 0$: the acceleration is perpendicular to the velocity. Since $\boldsymbol\gamma\times\mathbf{V}\neq 0$, the gyroscope undergoes [[Def - Thomas Precession|Thomas precession]] — unlike the [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] of §16.2, whose acceleration is *parallel* to its velocity and so shows none. The speed $V = R\Omega$ is constant, so $\Gamma = (1 - R^2\Omega^2/c^2)^{-1/2}$ is constant, and $\vec\omega_T$ will be steady.

**Step 2: $\vec\omega_T = -(\Gamma - 1)\Omega\,\mathbf{e}_3^*$.**

> [!note]- Derivation
> Compute the cross product:
> $$\boldsymbol\gamma\times\mathbf{V} = (-R\Omega^2\hat{\mathbf{r}})\times(R\Omega\hat{\boldsymbol\theta}) = -R^2\Omega^3\,(\hat{\mathbf{r}}\times\hat{\boldsymbol\theta}) = -R^2\Omega^3\,\mathbf{e}_3^*,$$
> using the right-handed relation $\hat{\mathbf{r}}\times\hat{\boldsymbol\theta} = \mathbf{e}_3^*$ (radial cross tangential equals out-of-plane). Substitute into the [[Thm - The Thomas Equation|Thomas precession rate]] in the form $\vec\omega_T = \frac{\Gamma - 1}{V^2}\boldsymbol\gamma\times\mathbf{V}$, with $V^2 = R^2\Omega^2$:
> $$\vec\omega_T = \frac{\Gamma - 1}{R^2\Omega^2}\,(-R^2\Omega^3\,\mathbf{e}_3^*) = -(\Gamma - 1)\,\Omega\,\mathbf{e}_3^*.$$
> (Restoring $c$: the $\frac{\Gamma-1}{V^2}$ form already carries the $c$'s correctly; $\Gamma = (1 - R^2\Omega^2/c^2)^{-1/2}$.) Equivalently, using $\frac{\Gamma^2}{c^2(1+\Gamma)} = \frac{\Gamma-1}{V^2}$, the same result follows from the $\frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$ form. The precession vector points along $-\mathbf{e}_3^*$ for a counterclockwise ($+\mathbf{e}_3^*$) orbit.

**Step 3: The precession is opposite to the orbit, a lag of $2\pi(\Gamma - 1)$ per revolution.**

> [!note]- Derivation
> The orbital angular velocity is $\boldsymbol\Omega_{\mathrm{orb}} = +\Omega\,\mathbf{e}_3^*$ (counterclockwise). The Thomas precession $\vec\omega_T = -(\Gamma - 1)\Omega\,\mathbf{e}_3^*$ has the *opposite* sign: the gyroscope's spin precesses *clockwise*, against the orbital sense. So a gyroscope carried around the orbit *lags behind* a direction held fixed in $\mathcal{O}_*$.
>
> Over one complete revolution, the orbital period is $T = 2\pi/\Omega$ (in $\mathcal{O}_*$'s time), and the spin rotates by
> $$\Delta\phi_{\mathrm{Thomas}} = |\vec\omega_T|\,T = (\Gamma - 1)\Omega\cdot\frac{2\pi}{\Omega} = 2\pi(\Gamma - 1),$$
> in the direction opposite to the orbit. This is a net rotation per revolution — a **holonomy**: it depends only on the loop traversed in velocity space (the circle of constant speed $V = R\Omega$), not on how fast the loop is traversed in time. After one orbit, the gyroscope points $2\pi(\Gamma - 1)$ *behind* where it started relative to the stars. For relativistic orbital speeds this is substantial; for slow orbits it is tiny but nonzero, vanishing only as $\Gamma\to 1$ (the Newtonian limit). The result is a pure consequence of $\boldsymbol\gamma\not\parallel\mathbf{V}$: the velocity continuously turns, so the boost relating the gyroscope's frame to $\mathcal{O}_*$ continuously reorients, leaving the accumulated [[Def - Thomas Rotation|Thomas rotation]].

**Step 4: Low-velocity limit $\vec\omega_T \simeq -\tfrac12(R\Omega/c)^2\,\Omega\,\mathbf{e}_3^*$.**

> [!note]- Derivation
> For $R\Omega\ll c$, expand the Lorentz factor:
> $$\Gamma = \Big(1 - \frac{R^2\Omega^2}{c^2}\Big)^{-1/2} \approx 1 + \frac12\frac{R^2\Omega^2}{c^2}, \qquad\text{so}\qquad \Gamma - 1\approx \frac12\frac{R^2\Omega^2}{c^2} = \frac12\Big(\frac{R\Omega}{c}\Big)^2.$$
> Substituting into $\vec\omega_T = -(\Gamma - 1)\Omega\,\mathbf{e}_3^*$:
> $$\vec\omega_T \simeq -\frac12\Big(\frac{R\Omega}{c}\Big)^2\,\Omega\,\mathbf{e}_3^* = -\frac{R^2\Omega^3}{2c^2}\,\mathbf{e}_3^*.$$
> This is the precession rate at low speed, quadratic in the orbital velocity $V/c = R\Omega/c$ — the hallmark of a relativistic effect. Applied to an electron orbiting a nucleus (where $V/c\sim 1\%$), this rate is precisely the kinematic contribution that halves the naive spin–orbit coupling — the **Thomas half** of atomic fine structure (see [[Ex - The Thomas half and atomic fine structure]]). The lag per revolution is $2\pi(\Gamma - 1)\approx \pi(R\Omega/c)^2$.

> [!note]- Complete formal solution
> For uniform circular motion $\mathbf{r} = R(\cos\Omega t_*, \sin\Omega t_*, 0)$, the velocity is $\mathbf{V} = R\Omega\hat{\boldsymbol\theta}$ and acceleration $\boldsymbol\gamma = -R\Omega^2\hat{\mathbf{r}}$, with $\boldsymbol\gamma\perp\mathbf{V}$, so Thomas precession occurs. The cross product $\boldsymbol\gamma\times\mathbf{V} = -R^2\Omega^3\mathbf{e}_3^*$; with $V^2 = R^2\Omega^2$ the Thomas rate $\vec\omega_T = \frac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V} = -(\Gamma-1)\Omega\,\mathbf{e}_3^*$, opposite to the orbital $+\Omega\mathbf{e}_3^*$. Over one period $T = 2\pi/\Omega$ the spin lags by $|\vec\omega_T|T = 2\pi(\Gamma-1)$ — a holonomy of velocity-space transport. For $R\Omega\ll c$, $\Gamma - 1\approx\tfrac12(R\Omega/c)^2$, so $\vec\omega_T\simeq -\tfrac12(R\Omega/c)^2\Omega\,\mathbf{e}_3^*$, the rate underlying the atomic Thomas half. $\blacksquare$

---

# Key Takeaways

**A gyroscope carried around a loop lags the orbit — the precession is a holonomy of velocity-space transport.** The headline result, $2\pi(\Gamma - 1)$ of lag per revolution opposite to the orbital sense, is a *holonomy*: a net rotation accumulated around a closed loop, depending only on the loop (the circle of constant speed in velocity space), not on the timing. The trigger to recognise this elsewhere: whenever a frame or a spin is transported around a closed path while the velocity turns, expect a net rotation that is geometric — a property of the path, not of the dynamics. This is the special-relativistic, classical-spin member of a large family: in general relativity the same logic gives **geodetic precession** (a gyroscope lagging as it orbits a mass, measured by Gravity Probe B); in quantum mechanics it gives the **Berry phase**. The reusable diagnostic is that the lag is $2\pi(\Gamma - 1)$ — built from the Lorentz factor alone — and is independent of the orbital radius and frequency separately, depending only on the speed $V = R\Omega$.

**Thomas precession requires turning the velocity — acceleration alone is not enough.** The decisive structural point is that the precession arises *because* $\boldsymbol\gamma\perp\mathbf{V}$ (the acceleration turns the velocity), not merely because the gyroscope accelerates. A [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]], whose acceleration is *parallel* to its velocity, shows *no* Thomas precession despite being strongly accelerated. The trigger: to decide whether a moving frame Thomas-precesses, check whether the acceleration is collinear with the velocity — if so (straight-line acceleration), no precession; if not (any bending of the trajectory), precession at $\vec\omega_T\propto\boldsymbol\gamma\times\mathbf{V}$. The cross product is the quantitative measure of the non-collinearity, and it is why orbits, magnetic bending, and atomic motion all precess while a rocket firing straight ahead does not.

**Get the sign right — the precession opposes the orbit.** A persistent error is computing $\mathbf{V}\times\boldsymbol\gamma$ instead of $\boldsymbol\gamma\times\mathbf{V}$ and obtaining the wrong sign. The Thomas precession is along $\boldsymbol\gamma\times\mathbf{V}$ (acceleration cross velocity), which for a counterclockwise orbit points *into* the page ($-\mathbf{e}_3^*$), so the gyroscope precesses *clockwise*, against the orbital rotation. The reusable check: the gyroscope always *lags* the orbital motion, never leads it, and a velocity turning counterclockwise produces a clockwise spin precession. This sign is physically important — in the atomic application it is what makes the Thomas contribution *subtract* from the naive spin–orbit energy, halving it rather than doubling it. Whenever you compute a Thomas precession, sanity-check the sign against "the gyroscope lags".

**The low-velocity rate $\tfrac12(R\Omega/c)^2\Omega$ is the atomic Thomas half.** The quadratic-in-velocity precession $\vec\omega_T\simeq -\tfrac12(R\Omega/c)^2\Omega\,\mathbf{e}_3^*$ is the form that matters for atomic physics: an electron orbiting a nucleus at $V/c\sim 1\%$ has its spin precess at this rate, and that precession contributes an energy exactly cancelling half of the naive spin–orbit coupling — the famous **Thomas half** that brings the predicted fine-structure splitting into agreement with experiment and with the Dirac equation. The diagnostic this leaves: the factor of $\tfrac12$ in the low-velocity precession is *the* factor of $\tfrac12$ in the fine-structure formula, and it is purely kinematic — no dynamics, no quantum mechanics, just the geometry of how a Fermi–Walker-transported frame appears in the laboratory. This is developed in [[Ex - The Thomas half and atomic fine structure]], and the field-with-torque generalisation is the BMT equation of accelerator physics.

This exercise applies the [[Thm - The Thomas Equation|Thomas equation]] (free-gyroscope corollary) and pairs with [[Ex - Thomas precession from the composition of two boosts]] (the kinematic origin of $\vec\omega_T$) and [[Ex - The Thomas half and atomic fine structure]] (the atomic application of the low-velocity rate).
