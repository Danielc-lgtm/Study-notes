---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Acceleration Relative to an Observer"
  - "Def - Velocity Relative to an Observer"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Lorentz Factor and Relative Velocity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. The observer $\mathcal{O}$ is taken **inertial** for the main statement ($A_0 = 0$, four-rotation $\boldsymbol\omega = 0$), with four-velocity $U_0$ and proper time $t$. The particle $\mathcal{P}$ has four-velocity $U = \Gamma(U_0 + V)$, [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] $\Gamma = U \cdot U_0$, [[Def - Velocity Relative to an Observer|relative velocity]] $V$ (spacelike, $V \cdot U_0 = 0$, speed $|\mathbf V|$), [[Def - Acceleration Relative to an Observer|relative acceleration]] $\boldsymbol\gamma = \mathrm{d}\mathbf V/\mathrm{d}t$, and [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm{d}U/\mathrm{d}\tau'$ ($\tau'$ the particle's proper time, $A \cdot U = 0$, $A$ spacelike). The dot $\boldsymbol\gamma \cdot \mathbf V$ denotes the Euclidean rest-space scalar product of the two spatial vectors. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Statement

> **Theorem (expression of the four-acceleration).** Let $\mathcal{O}$ be an inertial observer with four-velocity $U_0$, and let $\mathcal{P}$ be a massive particle with relative velocity $V$, speed $|\mathbf V|$, Lorentz factor $\Gamma = (1-|\mathbf V|^2)^{-1/2}$, and relative acceleration $\boldsymbol\gamma$. Then the four-acceleration of $\mathcal{P}$ is
> $$A \;=\; \Gamma^2\Big[\boldsymbol\gamma \;+\; \Gamma^2\,(\boldsymbol\gamma \cdot \mathbf V)\,(V + U_0)\Big].$$
> In particular, at the instant $\mathcal{P}$ is **momentarily at rest** relative to $\mathcal{O}$ (so $\mathbf V = 0$ and $\Gamma = 1$),
> $$\boxed{\;A = \boldsymbol\gamma\;}$$
> the four-acceleration equals the relative acceleration measured by the comoving inertial observer — the **proper acceleration**. Its norm is
> $$\|A\|_g = \sqrt{-A\cdot A} = \Gamma^2\sqrt{|\boldsymbol\gamma|^2 + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)^2} = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}\,,$$
> where $\gamma_\parallel$ and $\gamma_\perp$ are the components of $\boldsymbol\gamma$ parallel and transverse to $\mathbf V$.

The boxed identity is the operational definition of proper acceleration: the four-acceleration is the ordinary (rest-space) acceleration that the momentarily comoving inertial observer measures, and its norm is the reading of an accelerometer carried by the particle.

---

# Motivation

The [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm{d}U/\mathrm{d}\tau'$ is the natural relativistic acceleration — a four-vector, orthogonal to the four-velocity, invariant under change of observer. But it is abstract: defined by differentiating the four-velocity with respect to the particle's own proper time, it does not obviously connect to anything an observer measures. The [[Def - Acceleration Relative to an Observer|relative acceleration]] $\boldsymbol\gamma = \mathrm{d}\mathbf V/\mathrm{d}t$ is concrete — it is what an observer computes from successive velocity measurements — but it is observer-dependent and not a four-vector. This theorem is the bridge between them: it expresses the abstract, invariant $A$ in terms of the concrete, measurable $\boldsymbol\gamma$ and $V$.

The role of the theorem is to give the four-acceleration a *physical meaning*. The general formula is intricate, but its punchline is simple and is the whole reason the theorem matters: at the instant the particle is momentarily at rest relative to the observer, $A = \boldsymbol\gamma$. So the four-acceleration, evaluated in the frame momentarily comoving with the particle, is just the ordinary acceleration — the thing an accelerometer reads. This is what makes $\|A\|_g$ the **proper acceleration**, the frame-independent magnitude of the particle's acceleration, the quantity that is constant for a uniformly accelerated rocket and that an astronaut feels as weight.

The deeper significance is the contrast it draws between the two accelerations, which is the source of the most persistent confusion in relativistic dynamics. In Newtonian physics acceleration is absolute among inertial observers; relativistically the *relative* acceleration $\boldsymbol\gamma$ is *not* — it depends on the velocity $\mathbf V$, as the $\boldsymbol\gamma \cdot \mathbf V$ terms in the formula show, so two inertial observers in relative motion measure different $\boldsymbol\gamma$ for the same particle. The four-acceleration $A$ *is* absolute. The theorem makes this precise: the observer-dependence of $\boldsymbol\gamma$ is concentrated in the $\Gamma$ and $\boldsymbol\gamma \cdot \mathbf V$ factors, which conspire to keep $A$ invariant, and they vanish exactly at momentary rest, where the two notions of acceleration coincide.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\boldsymbol\gamma$ is the relative acceleration of $\mathcal{P}$ as measured by an inertial observer, and $V$ the relative velocity". The point is to recognise this configuration.

The first disguised source is **"a particle's trajectory $x^i(t)$ is given in a lab frame"**. Differentiating once gives $V^i = \dot x^i$, twice gives $\boldsymbol\gamma^i = \ddot x^i$, and the theorem assembles these into the four-acceleration. The bridge is that any coordinate trajectory in an inertial frame supplies $V$ and $\boldsymbol\gamma$ by differentiation. *Example problem:* given a particle's lab-frame path, compute its proper acceleration — the accelerometer reading — at each instant. See [[Ex - Proper acceleration of circular motion and its norm]].

The second disguised source is **"a particle is momentarily at rest relative to the observer"**. Whenever $\mathbf V = 0$ at the instant of interest, the four-acceleration is *just* the relative acceleration, $A = \boldsymbol\gamma$. The bridge is the boxed special case, which collapses the entire formula. The nonobviousness is that this is the *definition* of proper acceleration: to find the invariant $\|A\|_g$, go to the comoving frame, where it is the ordinary acceleration. *Example problem:* a rocket's accelerometer reads $g$; its four-acceleration has norm $g$, because in the rocket's instantaneous rest frame the relative acceleration *is* the four-acceleration.

The third disguised source is **"the proper acceleration is prescribed"**. Setting $\|A\|_g$ to a constant and inverting the norm formula gives a differential equation for the relative acceleration $\boldsymbol\gamma$, hence the trajectory. The bridge is that constant $\|A\|_g$ is the defining property of [[Special Relativity XVI — Accelerated Observers|uniformly accelerated motion]]. *Example problem:* find the worldline of a particle with constant proper acceleration $a$ — the hyperbolic motion $x^2 - t^2 = 1/a^2$ — by imposing $\|A\|_g = a$ and integrating.

**Targets (Output Amplification)**

The conclusion is "$A = \Gamma^2[\boldsymbol\gamma + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)(V + U_0)]$, equal to $\boldsymbol\gamma$ at momentary rest".

Combine the conclusion with **a rest mass $m$**. Multiplying by $m$ gives the [[Def - Four-Force|four-force]] $f = mA$, and projecting onto the rest space gives the three-force $\mathbf f = \mathrm{d}\mathbf p/\mathrm{d}t$. The further result is the relativistic equation of motion, in which the three-force and the relative acceleration $\boldsymbol\gamma$ are related by *direction-dependent* mass factors ($\Gamma^3 m$ along $\mathbf V$, $\Gamma m$ transverse) — the longitudinal and transverse relativistic masses. The combination is useful because it turns the kinematic four-acceleration into Newton's second law and explains why a relativistic particle is "harder to push" along its motion than across it.

Combine the conclusion with **constant norm $\|A\|_g = a$**. The norm formula becomes a constraint, and for collinear motion ($\boldsymbol\gamma \parallel \mathbf V$) it reads $\Gamma^3|\boldsymbol\gamma| = a$, i.e. $|\boldsymbol\gamma| = a(1-|\mathbf V|^2)^{3/2}$, a separable differential equation. The further result is hyperbolic motion: the velocity asymptotes to $c$ and the worldline is a hyperbola. The combination is nonobvious because constant *proper* acceleration produces *decreasing* coordinate acceleration, the opposite of Newtonian uniform acceleration.

Combine the conclusion with **the decomposition of $\boldsymbol\gamma$ into parallel and transverse parts**. Writing $\boldsymbol\gamma = \gamma_\parallel\hat{\mathbf V} + \boldsymbol\gamma_\perp$, the norm formula simplifies to $\|A\|_g^2 = \Gamma^4(\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2)$. The further result is a clean separation of how parallel and transverse accelerations contribute to the proper acceleration, the kinematic input to synchrotron radiation (transverse acceleration in a circular accelerator) versus linac acceleration (parallel). The combination is useful because it isolates the physically distinct effects of accelerating along versus across the velocity.

---

# Why Is It True

The theorem is the chain rule applied to the four-velocity decomposition, and the reason the momentary-rest case is so clean is that at $\mathbf V = 0$ the particle's rest frame *is* the observer's frame.

Start from $A = \mathrm{d}U/\mathrm{d}\tau'$. Convert the proper-time derivative to the observer's time using $\mathrm{d}t = \Gamma\,\mathrm{d}\tau'$, so $A = \Gamma\,\mathrm{d}U/\mathrm{d}t$. Now $U = \Gamma(U_0 + V)$, and for an inertial observer $U_0$ is constant, so differentiating brings down two kinds of term: one from differentiating the relative velocity ($\mathrm{d}V/\mathrm{d}t = \boldsymbol\gamma$, the relative acceleration) and one from differentiating the Lorentz factor ($\mathrm{d}\Gamma/\mathrm{d}t$). The factor $\Gamma$ depends on the speed, and its derivative is $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$ — this is where every $\boldsymbol\gamma\cdot\mathbf V$ in the formula comes from. Assembling the two contributions and using $\mathrm{d}t = \Gamma\mathrm{d}\tau'$ once more gives the stated expression. **The intricate $\boldsymbol\gamma\cdot\mathbf V$ terms are nothing but the rate of change of the Lorentz factor, which is nonzero precisely when the particle speeds up or slows down (parallel acceleration); transverse acceleration changes the direction but not the speed, so it does not contribute to $\mathrm{d}\Gamma/\mathrm{d}t$.**

Now the momentary-rest case. At $\mathbf V = 0$ the speed vanishes, so $\Gamma = 1$ and the factor $\boldsymbol\gamma\cdot\mathbf V = 0$ kills the second bracket entirely. What remains is $A = \boldsymbol\gamma$. The geometric reason is that when the particle is momentarily at rest relative to the observer, the observer's rest space coincides with the particle's instantaneous rest frame, so "the rate of change of the rest-space velocity" (the relative acceleration) and "the rate of change of the four-velocity per unit proper time" (the four-acceleration) are measuring the same thing in the same frame. There is no relative velocity to distinguish the two notions of time or the two notions of space, so they collapse. This is why the comoving inertial observer reads the proper acceleration directly: at that instant, ordinary acceleration *is* four-acceleration.

The norm being invariant despite the formula's observer-dependence is the consistency check. $\|A\|_g$ is a scalar built from a four-vector, so it is the same for all observers; evaluating it in the comoving frame, where $A = \boldsymbol\gamma$, gives $\|A\|_g = |\boldsymbol\gamma_{\mathrm{comoving}}|$, the proper acceleration. The general norm formula $\Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}$ must therefore reduce to this in the comoving frame and to the same number in every other — which it does, because it is computed from the invariant $A \cdot A$.

---

# What Makes This Hard

The derivation is a chain-rule computation, and the place people get lost is the bookkeeping of two times and two factors of $\Gamma$: the conversion $A = \Gamma\,\mathrm{d}U/\mathrm{d}t$ (one $\Gamma$ from $\mathrm{d}t = \Gamma\mathrm{d}\tau'$) and then the derivative of $\Gamma$ itself ($\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3\boldsymbol\gamma\cdot\mathbf V$), which together produce the $\Gamma^2$ and $\Gamma^4$ factors. The non-obvious conceptual step is recognising that the messy $\boldsymbol\gamma\cdot\mathbf V$ terms are exactly the rate of change of the speed — so that transverse acceleration (which leaves the speed fixed) drops out of them — and that the whole formula collapses to $A = \boldsymbol\gamma$ at momentary rest. The common error is to forget that $\Gamma$ is not constant when differentiating $U = \Gamma(U_0 + V)$, dropping the $\mathrm{d}\Gamma/\mathrm{d}t$ contribution and getting the wrong (over-simple) four-acceleration.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write $A = \mathrm{d}U/\mathrm{d}\tau' = \Gamma\,\mathrm{d}U/\mathrm{d}t$, differentiate $U = \Gamma(U_0 + V)$ with $U_0$ constant (inertial observer), and use $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$ for the Lorentz-factor derivative. Then set $\mathbf V = 0$ to get the momentary-rest identity, and take the Minkowski norm for the proper acceleration.

**Subgoal decomposition:**

1. **Convert proper-time to observer-time derivative.** Show $A = \Gamma\,\mathrm{d}U/\mathrm{d}t$.
   - *Hint:* $\mathrm{d}t = \Gamma\,\mathrm{d}\tau'$, so $\mathrm{d}/\mathrm{d}\tau' = \Gamma\,\mathrm{d}/\mathrm{d}t$.
   - *Why needed:* It lets you differentiate the decomposition with respect to the observer's time, which is what $V$ and $\boldsymbol\gamma$ are defined against.

2. **Differentiate the Lorentz factor.** Show $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$.
   - *Hint:* $\Gamma = (1-|\mathbf V|^2)^{-1/2}$; differentiate using $\mathrm{d}|\mathbf V|^2/\mathrm{d}t = 2\mathbf V\cdot\mathrm{d}\mathbf V/\mathrm{d}t = 2\boldsymbol\gamma\cdot\mathbf V$.
   - *Why needed:* This term is the source of every $\boldsymbol\gamma\cdot\mathbf V$ in the formula and the reason transverse acceleration behaves differently from parallel.

3. **Assemble the four-acceleration.** Differentiate $U = \Gamma(U_0 + V)$, substitute, and collect.
   - *Hint:* $\mathrm{d}U/\mathrm{d}t = \dot\Gamma(U_0 + V) + \Gamma\,\boldsymbol\gamma$; multiply by $\Gamma$ and use Step 2; the $\dot\Gamma$ terms give $\Gamma^2(\boldsymbol\gamma\cdot\mathbf V)(V+U_0)$ inside the bracket.
   - *Why needed:* It is the general formula.

4. **Specialise to momentary rest and take the norm.** Set $\mathbf V = 0$, $\Gamma = 1$ for $A = \boldsymbol\gamma$; compute $A\cdot A$ for the norm.
   - *Hint:* At $\mathbf V = 0$ the second bracket vanishes; for the norm, use $A\cdot A$ and the split of $\boldsymbol\gamma$ into parallel/transverse parts.
   - *Why needed:* The momentary-rest identity is the physical meaning; the norm is the proper acceleration.

---

# Lemma Decomposition

> [!note]- Lemma 1: The proper-time derivative is $\Gamma$ times the observer-time derivative
> **Statement:** For any quantity $f$ along $\mathcal{P}$'s worldline, $\mathrm{d}f/\mathrm{d}\tau' = \Gamma\,\mathrm{d}f/\mathrm{d}t$, where $t$ is the inertial observer's proper time and $\tau'$ the particle's.
>
> **Hint:** Use the defining relation $\mathrm{d}t = \Gamma\,\mathrm{d}\tau'$ and the chain rule.
>
> **Why needed:** It converts the four-acceleration (a $\tau'$-derivative) into a derivative with respect to the observer's clock, against which $V$ and $\boldsymbol\gamma$ are defined.
>
> > [!note]- Full proof
> > By definition of the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]], $\mathrm{d}t = \Gamma\,\mathrm{d}\tau'$, so $\mathrm{d}\tau'/\mathrm{d}t = 1/\Gamma$ and $\mathrm{d}t/\mathrm{d}\tau' = \Gamma$. By the chain rule, $\mathrm{d}f/\mathrm{d}\tau' = (\mathrm{d}f/\mathrm{d}t)(\mathrm{d}t/\mathrm{d}\tau') = \Gamma\,\mathrm{d}f/\mathrm{d}t$. In particular $A = \mathrm{d}U/\mathrm{d}\tau' = \Gamma\,\mathrm{d}U/\mathrm{d}t$. $\blacksquare$

> [!note]- Lemma 2: The derivative of the Lorentz factor is $\Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$
> **Statement:** Along $\mathcal{P}$'s worldline, $\dfrac{\mathrm{d}\Gamma}{\mathrm{d}t} = \Gamma^3\,(\boldsymbol\gamma\cdot\mathbf V)$, where $\boldsymbol\gamma\cdot\mathbf V$ is the Euclidean rest-space scalar product.
>
> **Hint:** $\Gamma = (1-|\mathbf V|^2)^{-1/2}$; differentiate and use $\tfrac{\mathrm{d}}{\mathrm{d}t}|\mathbf V|^2 = 2\,\boldsymbol\gamma\cdot\mathbf V$.
>
> **Why needed:** It supplies the $\boldsymbol\gamma\cdot\mathbf V$ terms and shows only the *parallel* part of $\boldsymbol\gamma$ (which changes the speed) contributes.
>
> > [!note]- Full proof
> > Write $\Gamma = (1-|\mathbf V|^2)^{-1/2}$. Then $\dfrac{\mathrm{d}\Gamma}{\mathrm{d}t} = -\tfrac12(1-|\mathbf V|^2)^{-3/2}\cdot\big(-\tfrac{\mathrm{d}}{\mathrm{d}t}|\mathbf V|^2\big) = \tfrac12\Gamma^3\,\tfrac{\mathrm{d}}{\mathrm{d}t}|\mathbf V|^2$. Now $|\mathbf V|^2 = \mathbf V\cdot\mathbf V$, so $\tfrac{\mathrm{d}}{\mathrm{d}t}|\mathbf V|^2 = 2\,\mathbf V\cdot\tfrac{\mathrm{d}\mathbf V}{\mathrm{d}t} = 2\,\mathbf V\cdot\boldsymbol\gamma$ (using $\boldsymbol\gamma = \mathrm{d}\mathbf V/\mathrm{d}t$). Hence $\dfrac{\mathrm{d}\Gamma}{\mathrm{d}t} = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$. Note this vanishes when $\boldsymbol\gamma \perp \mathbf V$ (transverse acceleration leaves the speed unchanged). $\blacksquare$

> [!note]- Lemma 3: The momentary-rest identity $A = \boldsymbol\gamma$
> **Statement:** At an instant where $\mathcal{P}$ is at rest relative to the inertial observer ($\mathbf V = 0$, $\Gamma = 1$), the four-acceleration equals the relative acceleration: $A = \boldsymbol\gamma$.
>
> **Hint:** Set $\mathbf V = 0$ and $\Gamma = 1$ in the general formula; the second bracket vanishes.
>
> **Why needed:** It is the physical heart of the theorem — the definition of proper acceleration as the comoving observer's measured acceleration.
>
> > [!note]- Full proof
> > The general formula is $A = \Gamma^2[\boldsymbol\gamma + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)(V+U_0)]$. At momentary rest, $\mathbf V = 0$, so the speed vanishes, $\Gamma = (1-0)^{-1/2} = 1$, and the scalar product $\boldsymbol\gamma\cdot\mathbf V = \boldsymbol\gamma\cdot 0 = 0$. Substituting, $A = 1\cdot[\boldsymbol\gamma + 1\cdot 0\cdot(0 + U_0)] = \boldsymbol\gamma$. Geometrically, at this instant the observer's rest space coincides with $\mathcal{P}$'s instantaneous rest frame, so the rate of change of the rest-space velocity (the relative acceleration) and the proper-time rate of change of the four-velocity (the four-acceleration) measure the same vector. The comoving inertial observer therefore reads the four-acceleration as an ordinary acceleration; its magnitude is the proper acceleration. $\blacksquare$

> [!note]- Lemma 4: The norm of the four-acceleration
> **Statement:** $\|A\|_g^2 = -A\cdot A = \Gamma^4\big(\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2\big)$, where $\gamma_\parallel = \boldsymbol\gamma\cdot\hat{\mathbf V}$ and $\gamma_\perp = |\boldsymbol\gamma - \gamma_\parallel\hat{\mathbf V}|$ are the components of $\boldsymbol\gamma$ along and across $\mathbf V$.
>
> **Hint:** Form $A\cdot A$ from the general formula; use $V\cdot U_0 = 0$, $U_0\cdot U_0 = 1$, $V\cdot V = -|\mathbf V|^2$, and split $\boldsymbol\gamma$ into parallel and transverse parts.
>
> **Why needed:** It gives the proper acceleration as a frame-independent scalar and shows parallel acceleration is "weighted" by an extra $\Gamma^2$ relative to transverse.
>
> > [!note]- Full proof
> > Taking the Minkowski scalar square of $A = \Gamma^2[\boldsymbol\gamma + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)(V+U_0)]$ and using that $\boldsymbol\gamma$ and $V$ are spacelike rest-space vectors (so $\boldsymbol\gamma\cdot\boldsymbol\gamma = -|\boldsymbol\gamma|^2$, $\boldsymbol\gamma\cdot V = -\boldsymbol\gamma\cdot\mathbf V$ in the Minkowski sense, $V\cdot V = -|\mathbf V|^2$), while $U_0\cdot U_0 = 1$, $U_0\cdot V = 0$, $U_0\cdot\boldsymbol\gamma = 0$, a direct expansion gives
> > $$A\cdot A = -\Gamma^4\Big[|\boldsymbol\gamma|^2 + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)^2\Big].$$
> > Writing $\boldsymbol\gamma = \gamma_\parallel\hat{\mathbf V} + \boldsymbol\gamma_\perp$ so that $|\boldsymbol\gamma|^2 = \gamma_\parallel^2 + \gamma_\perp^2$ and $\boldsymbol\gamma\cdot\mathbf V = \gamma_\parallel|\mathbf V|$, and using $\Gamma^2|\mathbf V|^2 = \Gamma^2 - 1$, the bracket becomes $\gamma_\parallel^2 + \gamma_\perp^2 + (\Gamma^2-1)\gamma_\parallel^2 = \Gamma^2\gamma_\parallel^2 + \gamma_\perp^2$. Hence $\|A\|_g^2 = -A\cdot A = \Gamma^4(\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2)$. (At momentary rest, $\Gamma = 1$ and this is $\gamma_\parallel^2 + \gamma_\perp^2 = |\boldsymbol\gamma|^2$, consistent with $A = \boldsymbol\gamma$.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{O}$ be inertial, so $U_0$ is constant along its worldline and $A_0 = 0$, $\boldsymbol\omega = 0$. The particle's four-velocity is $U = \Gamma(U_0 + V)$ with $V \cdot U_0 = 0$.
>
> By Lemma 1, $A = \mathrm{d}U/\mathrm{d}\tau' = \Gamma\,\mathrm{d}U/\mathrm{d}t$. Differentiating $U = \Gamma(U_0 + V)$ with $U_0$ constant:
> $$\frac{\mathrm{d}U}{\mathrm{d}t} = \frac{\mathrm{d}\Gamma}{\mathrm{d}t}(U_0 + V) + \Gamma\,\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{\mathrm{d}\Gamma}{\mathrm{d}t}(U_0 + V) + \Gamma\,\boldsymbol\gamma,$$
> using $\boldsymbol\gamma = \mathrm{d}V/\mathrm{d}t$. By Lemma 2, $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$. Therefore
> $$\frac{\mathrm{d}U}{\mathrm{d}t} = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)(U_0 + V) + \Gamma\,\boldsymbol\gamma,$$
> and multiplying by $\Gamma$ (Lemma 1),
> $$A = \Gamma\,\frac{\mathrm{d}U}{\mathrm{d}t} = \Gamma^4(\boldsymbol\gamma\cdot\mathbf V)(U_0 + V) + \Gamma^2\boldsymbol\gamma = \Gamma^2\Big[\boldsymbol\gamma + \Gamma^2(\boldsymbol\gamma\cdot\mathbf V)(V + U_0)\Big].$$
> This is the general formula.
>
> By Lemma 3, at momentary rest ($\mathbf V = 0$, $\Gamma = 1$) the bracketed correction vanishes and $A = \boldsymbol\gamma$: the four-acceleration is the relative acceleration measured by the comoving inertial observer, the proper acceleration.
>
> By Lemma 4, the Minkowski norm is $\|A\|_g = \sqrt{-A\cdot A} = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}$, a frame-independent scalar (it is built from the four-vector $A$), equal at momentary rest to $|\boldsymbol\gamma|$. This is the proper acceleration, the accelerometer reading. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Engineering of relativistic rockets — constant-thrust trajectories.** A rocket whose engines deliver constant proper acceleration $a$ (so the crew feels constant artificial gravity $a$) has $\|A\|_g = a$ at all times; inverting the norm formula for collinear motion gives $\mathrm{d}V/\mathrm{d}t = a(1-V^2)^{3/2}$, integrating to $V(t) = at/\sqrt{1+(at)^2}$ and the hyperbolic worldline. Computing the rocket's position, speed, and onboard time as functions of lab time is the staple "relativistic rocket" problem, and it is exactly this theorem inverted. The application is the bridge to [[Special Relativity XVI — Accelerated Observers|hyperbolic motion]].

**Accelerator physics — synchrotron versus linear acceleration.** In a circular accelerator the acceleration is transverse ($\gamma_\perp$), in a linac it is parallel ($\gamma_\parallel$); the norm formula weights the parallel part by an extra $\Gamma^2$, so the proper acceleration — and hence the radiated power, which scales with $\|A\|_g^2$ — differs enormously between the two geometries at high $\Gamma$. Estimating the proper acceleration of a stored beam from its radius and energy, and comparing to a linac, is a direct application that explains why synchrotron radiation limits circular machines. This connects to the Larmor formula of **Special Relativity XXIII**.

**Differential geometry — the curvature of a worldline.** The proper acceleration $\|A\|_g$ is the first **curvature** (Frenet curvature) of the worldline as a curve in Minkowski space, parametrised by proper time. A worldline of constant proper acceleration is the Lorentzian analogue of a circle (constant curvature), namely a hyperbola. Computing the curvature of a given worldline and identifying constant-curvature worldlines with uniform proper acceleration is the geometric reading, tying this theorem to the [[Def - Curvature and Torsions of a Worldline|Frenet–Serret apparatus]] of Special Relativity V.

---

# Bridges

- **[[Def - Four-Velocity and Four-Acceleration]]** — the object this theorem expresses. The four-acceleration is defined there as $A = \mathrm{d}U/\mathrm{d}\tau'$, an abstract four-vector orthogonal to $U$. This theorem gives it physical content: it is the relative acceleration the momentarily comoving inertial observer measures, and its norm is the proper acceleration. The orthogonality $A \cdot U = 0$ proved there is what allows $A$ to be a purely spatial vector in the comoving frame, where it equals $\boldsymbol\gamma$.

- **[[Def - Four-Force]]** — the dynamical sequel. Multiplying $A$ by the rest mass gives the four-force $f = mA$, and this theorem's decomposition becomes the relativistic equation of motion. The momentary-rest identity $A = \boldsymbol\gamma$ shows that in the instantaneous rest frame the four-force reduces to the ordinary Newtonian force $m\boldsymbol\gamma$ — which is why the rest frame is where relativistic dynamics looks Newtonian, the basis of [[Special Relativity XIII — Energy and Momentum|relativistic dynamics]].

- **Uniformly accelerated (hyperbolic) motion** — the constant-norm case. Imposing $\|A\|_g = a$ constant and integrating the resulting differential equation for $\boldsymbol\gamma$ gives the worldline $x^2 - t^2 = 1/a^2$, the relativistic uniformly accelerated motion. The decreasing relative acceleration $\boldsymbol\gamma = a/\Gamma^3$ (collinear) is the hallmark: constant *proper* acceleration produces *decreasing* coordinate acceleration as the speed nears $c$, the kinematic foundation of **Special Relativity XVI** and the Rindler horizon.

- **[[Def - Curvature and Torsions of a Worldline]]** — the geometric reading. The proper acceleration $\|A\|_g$ is the first curvature of the worldline as a curve in Minkowski space; a constant-curvature timelike worldline is a hyperbola, the Lorentzian analogue of a circle. The theorem's norm formula is the curvature expressed in terms of the observer-relative acceleration, connecting the kinematics to the Frenet–Serret description of worldlines.

---

# Unlocked by This

> [!tip] Relativistic Mass and the Equation of Motion *(from Relativistic Dynamics)*
> Multiplying by the rest mass, the four-force $f = mA$ projects to the three-force $\mathbf f = \mathrm{d}\mathbf p/\mathrm{d}t$, and this theorem's structure shows the three-force relates to the relative acceleration $\boldsymbol\gamma$ by direction-dependent factors: $\mathbf f_\parallel = \Gamma^3 m\,\boldsymbol\gamma_\parallel$ and $\mathbf f_\perp = \Gamma m\,\boldsymbol\gamma_\perp$. These are the **longitudinal and transverse relativistic masses** — the precise statement that a fast particle resists acceleration more along its motion than across it — developed in **Special Relativity XIII**.

> [!tip] Hyperbolic Motion, the Rindler Horizon, and the Unruh Effect *(from Accelerated Observers)*
> A particle with constant proper acceleration $\|A\|_g = a$ traces the hyperbola $x^2 - t^2 = 1/a^2$, the relativistic uniformly accelerated worldline. Behind it lies the **Rindler horizon**, a surface beyond which no signal can ever reach it, and a uniformly accelerated detector responds as if immersed in a thermal bath at the **Unruh temperature** $T = a/2\pi$. This theorem, with $\|A\|_g$ held constant, is the kinematic input; the rest is **Special Relativity XVI**, itself the special-relativistic shadow of the Hawking effect in [[General Relativity I — Einstein's Equations and Schwarzschild]].
