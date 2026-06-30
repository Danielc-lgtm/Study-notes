---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A particle starts at rest at the origin of an inertial frame $\mathcal{O}_*$ at $t_* = 0$ and undergoes constant proper acceleration $a$ (the reading of an onboard accelerometer, a constant), moving along the $x_*$-axis. Working with $c = 1$ except where you restore it:

1. Integrate the constant-proper-acceleration condition to find the velocity $u(t_*)$ as a function of inertial-frame time, and show $u \to 1$ but never reaches $1$.
2. Find the position $x_*(t_*)$ and verify that the worldline is the hyperbola $x_*^2 - t_*^2 = a^{-2}$ centred appropriately, i.e. $(ax_* + 1)^2 - (at_*)^2 = 1$ with the origin shift.
3. Find the proper time $\tau(t_*)$ elapsed on the particle's clock, and the rapidity $\varphi$ as a function of $\tau$.
4. Relate the relativists' proper acceleration $a$ (an inverse length) to the Newtonian $g = c^2 a$ (in $\mathrm{m\,s^{-2}}$), and show that the coordinate acceleration $\mathrm{d}^2 x_*/\mathrm{d}t_*^2$ is *not* constant and tends to zero.

**Recall:**

A [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] has constant proper acceleration — the constant being the *norm* $a = \|A\|$ of the four-acceleration, not the four-acceleration vector.

![[Def - Uniformly Accelerated Observer (Hyperbolic Motion)#The Definition]]

The four-velocity $U$ is the unit tangent to the worldline, $U\cdot U = 1$ (mostly-minus), and the four-acceleration is $A = c^{-1}\mathrm{d}U/\mathrm{d}\tau$ with $A\cdot U = 0$, so $A$ is spacelike with $\|A\| = \sqrt{-A\cdot A}$. The **rapidity** $\varphi$ parametrises a boost by $u = \tanh\varphi$, $\gamma = \cosh\varphi$, $\gamma u = \sinh\varphi$. The relation between proper acceleration and coordinate acceleration in the instantaneous rest frame is $a = (1 - u^2)^{3/2}\,\mathrm{d}^2 x_*/\mathrm{d}t_*^2$.

---

# Convergent Strategy

**Problem class.** A *compute-a-worldline* problem, the first class named in the [[Special Relativity XVI — Accelerated Observers#Problem-Solving Strategy|topic strategy]]: given a constant proper acceleration, find position, velocity, and proper time as functions of time, and recognise hyperbolic motion. The decisive move is to integrate the proper-acceleration condition rather than to write a Newtonian quadratic.

**Assumption pattern.** The single assumption is "constant proper acceleration $a$", which by the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]] forces the four-velocity to be a hyperbolic rotation $U = \cosh(a\tau)e_0^* + \sinh(a\tau)e_1^*$. The signpost is that the acceleration is the *felt* one (constant accelerometer reading), so it is the proper acceleration, not the coordinate acceleration. The starting condition "at rest at $t_* = 0$" fixes the tangent inertial frame.

**Theorem routing.** The route is: constant proper acceleration $\Rightarrow$ (via the coordinate-acceleration relation $a = (1-u^2)^{3/2}\dot u$) a first-order ordinary differential equation for $u(t_*)$ $\Rightarrow$ integrate to $u = at_*/\sqrt{1+(at_*)^2}$ $\Rightarrow$ integrate once more for $x_*$ $\Rightarrow$ eliminate $t_*$ to get the hyperbola. The proper time follows from $\mathrm{d}\tau = \mathrm{d}t_*/\gamma = \mathrm{d}t_*/\sqrt{1+(at_*)^2}$, and the rapidity from $\varphi = a\tau$.

**Key decision point.** The crux is *which* acceleration is held constant. Holding the *coordinate* acceleration $\mathrm{d}^2 x_*/\mathrm{d}t_*^2$ constant gives the Newtonian parabola $x_* = \tfrac12 g t_*^2$, which lets $u$ exceed $1$ — physically impossible. Holding the *proper* acceleration constant gives the hyperbola, in which $u$ asymptotes to $1$. The whole content of "constant acceleration in relativity" is making this choice correctly; the coordinate acceleration then necessarily decays so that $u$ stays below $1$.

---

# Legal Operations Used

1. **Integrate constant proper acceleration into a hyperbola** (operation 1 from the topic page). The condition $a = (1-u^2)^{3/2}\dot u$ is the coordinate-frame form of $\|A\| = a$; integrating it with $u(0) = 0$ gives the velocity, and a second integration gives the worldline, which collapses to a hyperbola via $\cosh^2 - \sinh^2 = 1$.

2. **Choose the tangent inertial observer and compute there** (operation 2 from the topic page). The frame $\mathcal{O}_*$ in which the particle is momentarily at rest at $t_* = 0$ is the natural one: the initial condition $u(0) = 0$ is set there, and the proper acceleration equals the coordinate acceleration *at that one instant*, fixing the constant of integration.

---

# Hints

> [!note]- Hint 1
> "Constant acceleration" in relativity means constant *proper* acceleration — the accelerometer reading, a Lorentz scalar — not constant coordinate acceleration $\mathrm{d}^2 x_*/\mathrm{d}t_*^2$. The relation between them, with $u = \mathrm{d}x_*/\mathrm{d}t_*$, is $a = (1 - u^2)^{3/2}\,\mathrm{d}^2 x_*/\mathrm{d}t_*^2 = (1-u^2)^{3/2}\dot u$. This is your differential equation for $u(t_*)$.

> [!note]- Hint 2
> Separate variables: $\mathrm{d}u/(1-u^2)^{3/2} = a\,\mathrm{d}t_*$. The left side integrates to $u/\sqrt{1-u^2} = \gamma u$. With $u(0) = 0$ you get $\gamma u = at_*$, i.e. $u/\sqrt{1-u^2} = at_*$; solve for $u$ to find $u = at_*/\sqrt{1 + (at_*)^2}$.

> [!note]- Hint 3
> For the position, integrate $u = \mathrm{d}x_*/\mathrm{d}t_* = at_*/\sqrt{1+(at_*)^2}$. The integral is $x_* = a^{-1}[\sqrt{1+(at_*)^2} - 1]$ (choosing $x_*(0) = 0$). Then $ax_* + 1 = \sqrt{1+(at_*)^2}$, so $(ax_*+1)^2 = 1 + (at_*)^2$, the hyperbola.

> [!note]- Hint 4
> For the proper time, $\mathrm{d}\tau = \mathrm{d}t_*/\gamma$ with $\gamma = \sqrt{1+(at_*)^2}$. So $\tau = \int_0^{t_*}\mathrm{d}t_*/\sqrt{1+(at_*)^2} = a^{-1}\sinh^{-1}(at_*)$. Inverting, $at_* = \sinh(a\tau)$, and the rapidity $\varphi = \tanh^{-1}u = a\tau$ grows *linearly* in proper time — uniform acceleration is uniform rapidity-rate.

---

# Solution

The whole problem is the integration of one first-order equation. Step 1 turns "constant proper acceleration" into a differential equation for the velocity and integrates it; Step 2 integrates again for the position and recognises the hyperbola; Step 3 finds the proper time and the linearly-growing rapidity; Step 4 sorts out the units and shows the coordinate acceleration decays. The non-obvious move is in Step 1, where one must use the *proper* acceleration relation rather than the Newtonian $\dot u = \mathrm{const}$.

**Step 1: The velocity is $u = at_*/\sqrt{1 + (at_*)^2}$, tending to $1$ but never reaching it.**

> [!note]- Derivation
> In the instantaneous rest frame the proper acceleration is the ordinary acceleration; transforming to the lab frame $\mathcal{O}_*$, where the particle moves at $u$, the proper acceleration relates to the coordinate acceleration by $a = (1 - u^2)^{3/2}\,\dot u$ (with $\dot u = \mathrm{d}u/\mathrm{d}t_*$; this is the $A^1$-component computation of the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]], or Tong's coordinate-acceleration relation). Separating variables,
> $$\frac{\mathrm{d}u}{(1 - u^2)^{3/2}} = a\,\mathrm{d}t_*.$$
> The left side integrates to $u/\sqrt{1-u^2}$ (check: $\frac{\mathrm{d}}{\mathrm{d}u}\frac{u}{\sqrt{1-u^2}} = (1-u^2)^{-3/2}$). With $u(0) = 0$,
> $$\frac{u}{\sqrt{1 - u^2}} = at_*.$$
> Squaring and solving, $u^2 = (at_*)^2(1 - u^2)$, so $u^2[1 + (at_*)^2] = (at_*)^2$ and
> $$u(t_*) = \frac{at_*}{\sqrt{1 + (at_*)^2}}.$$
> As $t_*\to+\infty$, $u\to 1$ (the speed of light, $c$) from below; the particle approaches but never reaches $c$. Restoring $c$: $u = a c^2 t_*/\sqrt{c^2 + (act_*)^2}$, or with $g = c^2 a$, $u = gt_*/\sqrt{1 + (gt_*/c)^2}$ — the Newtonian $u = gt_*$ for $gt_*\ll c$, capped at $c$.

**Step 2: The position is $x_* = a^{-1}[\sqrt{1 + (at_*)^2} - 1]$, a hyperbola $(ax_* + 1)^2 - (at_*)^2 = 1$.**

> [!note]- Derivation
> Integrate $u = \mathrm{d}x_*/\mathrm{d}t_*$:
> $$x_* = \int_0^{t_*}\frac{at_*'\,\mathrm{d}t_*'}{\sqrt{1 + (at_*')^2}} = a^{-1}\Big[\sqrt{1 + (at_*)^2} - 1\Big],$$
> choosing $x_*(0) = 0$ (the substitution $w = 1 + (at_*')^2$ makes the integral elementary). Then $ax_* + 1 = \sqrt{1 + (at_*)^2}$, so squaring,
> $$(ax_* + 1)^2 = 1 + (at_*)^2 \quad\Longleftrightarrow\quad (ax_* + 1)^2 - (at_*)^2 = 1.$$
> This is an equilateral hyperbola in the $(t_*, x_*)$ plane with centre at $(t_*, x_*) = (0, -a^{-1})$ and asymptotes $t_* = \pm(x_* + a^{-1})$. (In the centred coordinate $\tilde x = x_* + a^{-1}$ it reads $\tilde x^2 - t_*^2 = a^{-2}$.) The particle comes in from $x_* = +\infty$ in the infinite past, reaches the "top" $x_* = 0$ at $t_* = 0$ (momentarily at rest), and accelerates back out to $x_* = +\infty$. Restoring $c$: $x_* = a^{-1}[\sqrt{1 + (act_*)^2} - 1]$, or $x_* = (c^2/g)[\sqrt{1 + (gt_*/c)^2} - 1]$.

**Step 3: The proper time is $\tau = a^{-1}\sinh^{-1}(at_*)$, and the rapidity is $\varphi = a\tau$.**

> [!note]- Derivation
> The proper time accumulates as $\mathrm{d}\tau = \mathrm{d}t_*/\gamma$, and from Step 1, $\gamma = (1 - u^2)^{-1/2} = \sqrt{1 + (at_*)^2}$ (since $1 - u^2 = 1/[1 + (at_*)^2]$). Hence
> $$\tau = \int_0^{t_*}\frac{\mathrm{d}t_*'}{\sqrt{1 + (at_*')^2}} = a^{-1}\sinh^{-1}(at_*),$$
> using $\int\mathrm{d}w/\sqrt{1+w^2} = \sinh^{-1}w$. Inverting, $at_* = \sinh(a\tau)$, and therefore $\gamma = \cosh(a\tau)$, $\gamma u = \sinh(a\tau)$, $u = \tanh(a\tau)$. The **rapidity** is $\varphi = \tanh^{-1}u = a\tau$: it grows *linearly* in proper time, at the constant rate $a$. This is the cleanest statement of uniform acceleration — *uniform rapidity-rate* — and it is why the speed approaches $c$ only as $\tau\to\infty$ (rapidity infinity). Restoring $c$: $\tau = (c/g)\sinh^{-1}(gt_*/c)$ and $\varphi = a\tau = (g/c)\tau$. At late times $\tau \approx (c/g)\ln(2gt_*/c)$ grows only logarithmically: the traveller's clock runs ever slower relative to the lab.

**Step 4: The relativists' $a$ is an inverse length, $g = c^2 a$, and the coordinate acceleration decays as $a(1 - u^2)^{3/2} = a/\gamma^3 \to 0$.**

> [!note]- Derivation
> Restoring $c$, the four-acceleration norm $a$ has dimensions of inverse length: $[a] = [\,\|A\|\,] = [c^{-1}\mathrm{d}U/\mathrm{d}\tau]$, and $U$ is dimensionless (in $c=1$ units) while $\tau$ carries a length, so $a \sim 1/\mathrm{length}$. The corresponding ordinary acceleration is $g = c^2 a$, in $\mathrm{m\,s^{-2}}$. For $g = 9.8\,\mathrm{m\,s^{-2}}$ (Earth gravity), $a = g/c^2 \approx 1.1\times 10^{-16}\,\mathrm{m^{-1}}$, so $a^{-1} \approx 9\times 10^{15}\,\mathrm{m} \approx 1$ light-year. This astronomically large length scale is why hyperbolic-motion effects are invisible in everyday acceleration.
>
> The coordinate acceleration is *not* constant. From $u = at_*/\sqrt{1+(at_*)^2}$,
> $$\frac{\mathrm{d}^2 x_*}{\mathrm{d}t_*^2} = \frac{\mathrm{d}u}{\mathrm{d}t_*} = \frac{a}{[1 + (at_*)^2]^{3/2}} = a(1 - u^2)^{3/2} = \frac{a}{\gamma^3}.$$
> At $t_* = 0$ it equals $a$ (the proper acceleration), but as $t_*\to\infty$ it tends to $0$. The coordinate acceleration *must* decay this way so that $u$ stays below $1$: a particle that maintained constant coordinate acceleration would cross $c$ in finite time. The proper acceleration $a = \|A\|$, by contrast, is a Lorentz scalar and stays constant — the same for every inertial observer.

> [!note]- Complete formal solution
> Constant proper acceleration in the lab frame reads $a = (1-u^2)^{3/2}\dot u$. Separating, $\mathrm{d}u/(1-u^2)^{3/2} = a\,\mathrm{d}t_*$, integrates with $u(0)=0$ to $\gamma u = u/\sqrt{1-u^2} = at_*$, hence $u = at_*/\sqrt{1+(at_*)^2} \to 1$. Integrating $u = \dot x_*$ with $x_*(0)=0$ gives $x_* = a^{-1}[\sqrt{1+(at_*)^2}-1]$, so $(ax_*+1)^2 - (at_*)^2 = 1$: an equilateral hyperbola of centre $(0,-a^{-1})$ and asymptotes $t_* = \pm(x_*+a^{-1})$. Proper time $\tau = \int_0^{t_*}\mathrm{d}t_*'/\gamma = a^{-1}\sinh^{-1}(at_*)$, so $at_* = \sinh(a\tau)$, $\gamma = \cosh(a\tau)$, $u = \tanh(a\tau)$, and the rapidity $\varphi = a\tau$ grows linearly in proper time. The proper acceleration $a$ is an inverse length, $g = c^2 a$ (so $a^{-1}\approx 1$ light-year for $g = 9.8\,\mathrm{m\,s^{-2}}$); the coordinate acceleration $\mathrm{d}^2x_*/\mathrm{d}t_*^2 = a/\gamma^3 \to 0$, decaying so that $u$ never reaches $c$, while $a = \|A\|$ stays constant as a Lorentz scalar. $\blacksquare$

---

# Key Takeaways

**Constant acceleration means constant rapidity-rate, and that is why hyperbolic functions appear.** The single most reusable insight is that uniform proper acceleration is *uniform rapidity-rate*: $\varphi = a\tau$ grows linearly in proper time, at the constant rate $a$. Once you see this, the whole solution is forced — the velocity $u = \tanh(a\tau)$, the Lorentz factor $\gamma = \cosh(a\tau)$, and the position involving $\sinh(a\tau)$ all follow because a boost of rapidity $\varphi$ acts by $\cosh\varphi, \sinh\varphi$. The trigger to recognise elsewhere is any phrase "constant acceleration", "constant thrust per unit mass", or "constant accelerometer reading": reach immediately for $\cosh(a\tau)$ and $\sinh(a\tau)$, never for a quadratic in time. The parabola $x = \tfrac12 gt^2$ is the $\varphi\ll 1$ approximation; the hyperbola is the exact answer, and the difference is precisely the requirement that rapidity, not velocity, is the additive quantity.

**Proper acceleration is a Lorentz scalar; coordinate acceleration is frame-dependent and must decay.** A persistent confusion in accelerated-motion problems is conflating the proper acceleration $a = \|A\|$ (what the traveller *feels*, the same number for every observer) with the coordinate acceleration $\mathrm{d}^2 x_*/\mathrm{d}t_*^2$ (what a particular inertial observer *computes*, frame-dependent). They agree only at the one instant the particle is at rest in the chosen frame; thereafter the coordinate acceleration falls off as $a/\gamma^3$, and it *has* to, because constant coordinate acceleration would push the speed past $c$. The diagnostic to carry: whenever a problem says "acceleration", ask "felt or coordinate?" — felt is constant and invariant, coordinate is computed and decaying. This same distinction is the source of the warning in the topic page against using the velocity-addition formula for the relative acceleration.

**The length scale $a^{-1}$ is the ruler of all accelerated physics, and it is astronomically large for everyday $g$.** The proper acceleration, restored with $c$, is an inverse length, and $a^{-1} = c^2/g$ is *the* scale at which relativistic effects of acceleration become order-one. For Earth gravity $a^{-1}\approx 1$ light-year, which is why nothing relativistic happens when you drop a ball — you would need to accelerate at $g$ for about a year (of proper time) to reach relativistic speeds, and the [[Def - Rindler Horizon|Rindler horizon]] sits a light-year behind you. Computing $a^{-1}$ first is the right opening move in every problem of this chapter: it tells you whether the relativistic corrections matter (distances comparable to $a^{-1}$) or are negligible (distances $\ll a^{-1}$, where everything is Newtonian). The same $a$ reappears as the curvature of the worldline, the location of the horizon, the strength of the redshift, and — quantum-mechanically — the Unruh temperature.

**The worldline is the Lorentzian analogue of uniform circular motion.** The deepest way to hold this result is that the hyperbola is to Minkowski space what the circle is to Euclidean space: the curve of constant curvature. A circle is parametrised by $(\cos\theta, \sin\theta)$ with arc length $\theta$ and constant curvature $1/r$; the hyperbola by $(\cosh\varphi, \sinh\varphi)$ with proper time as the *hyperbolic* arc length $\varphi = a\tau$ and constant curvature $a$. The centre $(0, -a^{-1})$ sits at distance $a^{-1}$ from the worldline, exactly as a circle's centre sits at distance $1/\kappa = r$. The one difference — that a hyperbola is unbounded while a circle closes — is the whole of why the velocity asymptotes to $c$ (the hyperbola never crosses its asymptote) instead of wrapping around. This picture, "uniform circular motion with the metric sign flipped", makes every feature of §16.1 predictable, and it is the seed of the [[Def - Curvature and Torsions of a Worldline|Serret–Frenet]] view in which $a$ is the worldline's first curvature.

This exercise sets up [[Ex - The Rindler horizon and the light that never catches up]] (the asymptotes become the horizon) and [[Ex - The relativistic rocket and a constant-g voyage]] (the proper-time formula gives the crew time for an interstellar trip).
