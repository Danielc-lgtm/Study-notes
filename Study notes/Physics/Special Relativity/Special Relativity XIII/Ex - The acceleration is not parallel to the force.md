---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Relativistic Newton's Second Law"
  - "Def - Four-Force"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

In Newtonian mechanics $\mathbf{a} = \mathbf{f}/m$, so the acceleration always points along the force. Relativistically this fails. Work with $c = 1$; let $m$ be the rest mass, $\mathbf{u}$ the three-velocity ($u = |\mathbf{u}|$, $\gamma = (1-u^2)^{-1/2}$), $\mathbf{f}$ a **pure** three-force, and $\mathbf{a} = d\mathbf{u}/dt$.

1. By differentiating the relativistic momentum $\mathbf{p} = \gamma m\mathbf{u}$, show that
$$\mathbf{f} = \gamma m\,\mathbf{a} + \gamma^3 m\,(\mathbf{a}\cdot\mathbf{u})\,\mathbf{u}.$$
2. Resolve into components along and across the velocity, and read off the **longitudinal mass** and **transverse mass**:
$$f_\parallel = \gamma^3 m\,a_\parallel, \qquad f_\perp = \gamma m\,a_\perp.$$
3. Hence show that a force at an oblique angle to the velocity produces an acceleration at a *different* angle, and find the relation between the two angles. In which direction does the acceleration lean — toward or away from the velocity?
4. Invert the relation to express $\mathbf{a}$ in terms of $\mathbf{f}$, and use it to explain why a constant force applied to a particle never accelerates it past $c$.

**Recall:**

![[Thm - Relativistic Newton's Second Law#Statement]]

The [[Def - Four-Momentum and Rest Mass|relativistic momentum]] is $\mathbf{p} = \gamma m\mathbf{u}$ and the spatial equation of motion ([[Thm - Relativistic Newton's Second Law]]) is $d\mathbf{p}/dt = \mathbf{f}$. A **pure** [[Def - Four-Force|four-force]] preserves the rest mass, $dm/dt = 0$. The Lorentz factor obeys $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$ (differentiate $\gamma = (1-u^2)^{-1/2}$). "Longitudinal" means parallel to $\mathbf{u}$, "transverse" means perpendicular to $\mathbf{u}$.

---

# Convergent Strategy

**Problem class.** A *differentiate-the-momentum* problem: the non-parallelism of force and acceleration is hidden inside $\mathbf{p} = \gamma m\mathbf{u}$, and it emerges the moment you differentiate honestly, keeping the speed-dependence of $\gamma$.

**Assumption pattern.** A pure force (so $m$ constant) and a velocity-dependent $\gamma$. The signpost is any question about the *direction* of the acceleration, or about "longitudinal versus transverse" response — these are exactly where the extra $\gamma^3$ term lives.

**Theorem routing.** Everything is [[Thm - Relativistic Newton's Second Law|the relativistic second law]] $d\mathbf{p}/dt = \mathbf{f}$ with $\mathbf{p} = \gamma m\mathbf{u}$, plus the chain-rule fact $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$. Resolving into $\parallel$ and $\perp$ components gives the two effective masses; inverting gives $\mathbf{a}(\mathbf{f})$.

**Key decision point.** The crux is to *not* write $\mathbf{a} = \mathbf{f}/(\gamma m)$. The factor $\gamma$ in $\mathbf{p} = \gamma m\mathbf{u}$ depends on the speed, so differentiating produces a second term $\propto d\gamma/dt$ that points along $\mathbf{u}$. Keeping this term is the entire content of the exercise; dropping it is the standard error. Once kept, resolving along and across $\mathbf{u}$ separates the two responses cleanly because the extra term is purely longitudinal.

---

# Legal Operations Used

1. **Differentiate four-momentum with respect to time to get the force** (operation 9, projected). $d\mathbf{p}/dt = \mathbf{f}$ with $\mathbf{p} = \gamma m\mathbf{u}$ is the spatial part of the equation of motion.

2. **Use the mass-shell / kinematic identities.** The relation $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$ (from $\gamma = (1-u^2)^{-1/2}$) supplies the longitudinal term.

3. **Resolve a vector into components** along and perpendicular to $\mathbf{u}$ — the device that exposes the longitudinal and transverse masses.

---

# Hints

> [!note]- Hint 1
> Apply the product rule to $\mathbf{p} = \gamma m\mathbf{u}$, holding $m$ constant (pure force): $\mathbf{f} = d\mathbf{p}/dt = m(\dot\gamma\,\mathbf{u} + \gamma\,\dot{\mathbf{u}}) = m\dot\gamma\,\mathbf{u} + \gamma m\,\mathbf{a}$. You need $\dot\gamma$.

> [!note]- Hint 2
> Differentiate $\gamma = (1-u^2)^{-1/2}$ with $u^2 = \mathbf{u}\cdot\mathbf{u}$: $\dot\gamma = -\tfrac12(1-u^2)^{-3/2}\cdot(-2\mathbf{u}\cdot\mathbf{a}) = \gamma^3(\mathbf{u}\cdot\mathbf{a})$. Substitute into Hint 1 to get $\mathbf{f} = \gamma m\mathbf{a} + \gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$.

> [!note]- Hint 3
> Split $\mathbf{a} = \mathbf{a}_\parallel + \mathbf{a}_\perp$ (parallel and perpendicular to $\mathbf{u}$). The extra term $\gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$ is purely along $\mathbf{u}$, and $\mathbf{a}\cdot\mathbf{u} = a_\parallel u$. Collect: the perpendicular part of $\mathbf{f}$ is $\gamma m\mathbf{a}_\perp$; the parallel part is $\gamma m a_\parallel + \gamma^3 m u^2 a_\parallel = \gamma m a_\parallel(1 + \gamma^2 u^2) = \gamma^3 m a_\parallel$ (using $1 + \gamma^2 u^2 = \gamma^2$).

> [!note]- Hint 4
> Invert each component: $a_\parallel = f_\parallel/(\gamma^3 m)$, $a_\perp = f_\perp/(\gamma m)$. For a constant longitudinal force, as $u\to c$, $\gamma\to\infty$ and $a_\parallel = f/(\gamma^3 m)\to 0$ — the acceleration is choked off, so the speed approaches $c$ asymptotically without reaching it.

---

# Solution

The non-parallelism of force and acceleration is the speed-dependence of $\gamma$ made visible. Differentiating $\mathbf{p} = \gamma m\mathbf{u}$ produces, besides the expected $\gamma m\mathbf{a}$, a second term along $\mathbf{u}$ that makes the particle stiffer to being sped up than to being turned — and that stiffness is what enforces the speed limit.

**Step 1: Differentiate the momentum.**

> [!note]- Derivation
> The spatial equation of motion is $\mathbf{f} = d\mathbf{p}/dt$ with $\mathbf{p} = \gamma m\mathbf{u}$. For a pure force the rest mass $m$ is constant, so by the product rule
> $$\mathbf{f} = \frac{d}{dt}(\gamma m\mathbf{u}) = m\frac{d\gamma}{dt}\mathbf{u} + \gamma m\frac{d\mathbf{u}}{dt} = m\dot\gamma\,\mathbf{u} + \gamma m\,\mathbf{a}.$$
> The Lorentz factor's time derivative is, differentiating $\gamma = (1 - \mathbf{u}\cdot\mathbf{u})^{-1/2}$,
> $$\dot\gamma = -\tfrac12(1-u^2)^{-3/2}\frac{d}{dt}(-\mathbf{u}\cdot\mathbf{u}) = \tfrac12\gamma^3\cdot 2(\mathbf{u}\cdot\mathbf{a}) = \gamma^3(\mathbf{u}\cdot\mathbf{a}),$$
> using $(1-u^2)^{-3/2} = \gamma^3$. Substituting,
> $$\boxed{\ \mathbf{f} = \gamma m\,\mathbf{a} + \gamma^3 m\,(\mathbf{a}\cdot\mathbf{u})\,\mathbf{u}\ }.$$
> The first term $\gamma m\mathbf{a}$ is the naive "mass times acceleration" (with the relativistic mass-factor $\gamma$); the second term $\gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$ is purely along the velocity and has no Newtonian counterpart. It is present whenever the acceleration has a component along the motion — that is, whenever the *speed* is changing — and it is the source of all the non-parallelism that follows.

**Step 2: Longitudinal and transverse masses.**

> [!note]- Derivation
> Resolve the acceleration into a part along the velocity and a part across it, $\mathbf{a} = \mathbf{a}_\parallel + \mathbf{a}_\perp$ with $\mathbf{a}_\parallel = a_\parallel\,\hat{\mathbf{u}}$ and $\mathbf{a}_\perp\perp\mathbf{u}$. The extra term is longitudinal: $(\mathbf{a}\cdot\mathbf{u})\mathbf{u} = (a_\parallel u)\,u\,\hat{\mathbf{u}} = a_\parallel u^2\,\hat{\mathbf{u}}$. So the force splits as
> $$\mathbf{f}_\perp = \gamma m\,\mathbf{a}_\perp, \qquad \mathbf{f}_\parallel = \gamma m\,a_\parallel\hat{\mathbf{u}} + \gamma^3 m\,a_\parallel u^2\,\hat{\mathbf{u}} = \gamma m\,a_\parallel(1 + \gamma^2 u^2)\,\hat{\mathbf{u}}.$$
> Using the identity $1 + \gamma^2 u^2 = \gamma^2$ (since $\gamma^2 u^2 = \gamma^2 - 1$), the parallel coefficient simplifies:
> $$\boxed{\ f_\parallel = \gamma^3 m\,a_\parallel, \qquad f_\perp = \gamma m\,a_\perp\ }.$$
> So the particle has an anisotropic inertia: a **longitudinal mass** $\gamma^3 m$ resisting changes in speed, and a **transverse mass** $\gamma m$ resisting changes in direction. (The names are historical; "mass" here means "the ratio of force to acceleration", and that ratio depends on the direction of the force relative to the motion.) The longitudinal mass is larger by a factor $\gamma^2$: it is much harder to speed a fast particle up than to deflect it.

**Step 3: The acceleration leans away from the force.**

> [!note]- Derivation
> Because the longitudinal response is suppressed by $\gamma^2$ relative to the transverse, a force at angle to the velocity produces an acceleration at a *different* angle. Quantitatively, from $a_\parallel = f_\parallel/(\gamma^3 m)$ and $a_\perp = f_\perp/(\gamma m)$, the tangent of the angle $\alpha$ that $\mathbf{a}$ makes with $\mathbf{u}$ is
> $$\tan\alpha_{\mathbf{a}} = \frac{a_\perp}{a_\parallel} = \frac{f_\perp/(\gamma m)}{f_\parallel/(\gamma^3 m)} = \gamma^2\,\frac{f_\perp}{f_\parallel} = \gamma^2\tan\alpha_{\mathbf{f}},$$
> where $\alpha_{\mathbf{f}}$ is the angle $\mathbf{f}$ makes with $\mathbf{u}$. Since $\gamma^2 > 1$, $\tan\alpha_{\mathbf{a}} > \tan\alpha_{\mathbf{f}}$: the acceleration is tilted *further from the velocity* than the force is. The transverse component is relatively amplified — the particle responds more readily across its motion than along it — so $\mathbf{a}$ "leans away" from $\mathbf{u}$ compared with $\mathbf{f}$. Only when the force is purely longitudinal ($\alpha_{\mathbf{f}} = 0$) or purely transverse ($\alpha_{\mathbf{f}} = \pi/2$) are $\mathbf{a}$ and $\mathbf{f}$ parallel; for every oblique force they point in different directions, a phenomenon with no Newtonian analogue.

**Step 4: Inversion and the speed limit.**

> [!note]- Derivation
> Inverting the component relations gives the acceleration produced by a given force:
> $$\mathbf{a} = \frac{1}{\gamma m}\Big(\mathbf{f} - (\mathbf{f}\cdot\mathbf{u})\,\mathbf{u}\Big),$$
> which one checks reproduces $a_\parallel = f_\parallel/(\gamma^3 m)$ (the bracket removes a fraction $u^2$ of the longitudinal force, leaving $f_\parallel(1-u^2) = f_\parallel/\gamma^2$, divided by $\gamma m$) and $a_\perp = f_\perp/(\gamma m)$. Now apply a *constant* force $\mathbf{f}$ along the direction of motion (a one-dimensional accelerator). Then $a = f/(\gamma^3 m)$, and as the particle speeds up, $\gamma\to\infty$, so
> $$a = \frac{f}{\gamma^3 m} \;\xrightarrow{\;u\to c\;}\; 0.$$
> The acceleration is *choked off* by the diverging longitudinal mass: the closer the particle gets to $c$, the more its inertia resists further speeding up, and the acceleration falls to zero. The speed therefore approaches $c$ asymptotically but never reaches it, however long the constant force acts. (Integrating $d(\gamma u)/dt = f/m$ gives $\gamma u = (f/m)t$, hence $u = (f/m)t/\sqrt{1 + (ft/m)^2}\to 1$ as $t\to\infty$ — the hyperbolic motion of [[Special Relativity XVI — Accelerated Observers|a uniformly accelerated observer]].) This is the dynamical mechanism enforcing the speed limit: not a sudden barrier, but a smoothly growing reluctance encoded in the $\gamma^3$ longitudinal mass.

> [!note]- Complete formal solution
> For a pure force $m$ is constant, so $\mathbf{f} = d(\gamma m\mathbf{u})/dt = m\dot\gamma\,\mathbf{u} + \gamma m\mathbf{a}$ with $\dot\gamma = \gamma^3(\mathbf{u}\cdot\mathbf{a})$, giving $\mathbf{f} = \gamma m\mathbf{a} + \gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$. Resolving along/across $\mathbf{u}$ and using $1+\gamma^2 u^2 = \gamma^2$: $f_\parallel = \gamma^3 m a_\parallel$ (longitudinal mass $\gamma^3 m$), $f_\perp = \gamma m a_\perp$ (transverse mass $\gamma m$). The acceleration angle satisfies $\tan\alpha_{\mathbf{a}} = \gamma^2\tan\alpha_{\mathbf{f}}$, so $\mathbf{a}$ leans further from $\mathbf{u}$ than $\mathbf{f}$ does, and the two are parallel only for purely longitudinal or transverse forces. Inverting, $\mathbf{a} = (\mathbf{f} - (\mathbf{f}\cdot\mathbf{u})\mathbf{u})/(\gamma m)$; for a constant longitudinal force $a = f/(\gamma^3 m)\to 0$ as $u\to c$, so the speed approaches but never reaches $c$. $\blacksquare$

---

# Key Takeaways

**Inertia is anisotropic at relativistic speeds — longitudinal mass $\gamma^3 m$, transverse mass $\gamma m$.** The headline result is that "the ratio of force to acceleration" is no longer a single number $m$ but depends on whether the force pushes along the motion or across it. Pushing along the motion changes the *speed*, which fights the $\gamma^3$ growth of energy near $c$, so the effective inertia is $\gamma^3 m$; pushing across changes only the *direction*, which fights only the $\gamma$ in the momentum, so the effective inertia is $\gamma m$. The longitudinal mass exceeds the transverse by a factor $\gamma^2$, and both diverge as $u\to c$. The reusable content is that the relativistic momentum $\mathbf{p} = \gamma m\mathbf{u}$ cannot be differentiated as if $\gamma$ were constant — the speed-dependence of $\gamma$ generates a longitudinal term that is the whole story — so any problem involving acceleration, force direction, or beam stiffness must keep that term. The historical "longitudinal/transverse mass" language is a compact way to carry the two responses, though modern usage prefers the single invariant rest mass $m$ and the explicit $\gamma$-factors.

**The acceleration is not parallel to the force, and it leans away from the velocity.** This is the most counterintuitive purely-mechanical consequence of special relativity, and it has no Newtonian shadow: in Newtonian mechanics $\mathbf{a} = \mathbf{f}/m$ is rigidly parallel to $\mathbf{f}$, whereas relativistically $\tan\alpha_{\mathbf{a}} = \gamma^2\tan\alpha_{\mathbf{f}}$, so the acceleration is tilted further from the direction of motion than the force is. The physical reading is that the particle responds more easily across its motion (transverse mass $\gamma m$) than along it (longitudinal mass $\gamma^3 m$), so the transverse component of any oblique force is relatively amplified in the resulting acceleration. The reflex to carry away: never assume $\mathbf{a}\parallel\mathbf{f}$ for a fast particle, and when you need the acceleration from a force, invert the full relation $\mathbf{a} = (\mathbf{f} - (\mathbf{f}\cdot\mathbf{u})\mathbf{u})/(\gamma m)$ rather than dividing by a single mass. This anisotropy is why accelerating a relativistic beam (longitudinal) is enormously harder than steering it (transverse), the practical fact behind the design of synchrotrons.

**The $\gamma^3$ longitudinal mass is the dynamical enforcer of the speed limit.** The kinematic statement "nothing exceeds $c$" acquires here its mechanical mechanism: a constant longitudinal force produces acceleration $a = f/(\gamma^3 m)$, which falls to zero as $u\to c$ because the longitudinal inertia diverges. There is no wall and no sudden cutoff — just a smoothly growing reluctance to be sped up, so the velocity approaches $c$ asymptotically (the hyperbolic worldline $\gamma u = ft/m$) no matter how long or how hard you push. This is the same divergence of $\gamma$ that makes the work to reach $c$ infinite ([[Ex - The relativistic work-energy theorem|the work–energy theorem]]) and the rocket's required mass ratio unbounded ([[Ex - The relativistic rocket|the relativistic rocket]]); all three are faces of the single fact that $\gamma\to\infty$ as $u\to c$. The reusable diagnostic: whenever a Newtonian argument would let a constant force push a particle past $c$, the relativistic correction inserts a $\gamma$-power that chokes the relevant rate exactly at the light speed — here the $\gamma^3$ in the longitudinal acceleration.
