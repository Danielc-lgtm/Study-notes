---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

A particle (a rocket) undergoes **constant proper acceleration** $a$ along the $x$-axis, starting from rest at the origin at proper time $\tau = 0$. Working with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$:

1. Show that its four-velocity is $U^\mu = (\cosh a\tau, \sinh a\tau, 0, 0)$ and integrate to find its worldline $X^\mu(\tau)$, exhibiting that it is an **arc of a hyperbola** in the $(t, x)$-plane.
2. Express the coordinate time $t$ and position $x$ as functions of the proper time $\tau$, and invert to find the proper time $\tau(t)$ as a function of coordinate time. Confirm $\tau \le t$ and explain the inequality.
3. Now consider the full **Langevin traveller**: a rocket that fires forward, reverses thrust at $t = T/4$ and again at $t = 3T/4$, and shuts off at $t = T$, so that its worldline is three arcs of hyperbola and it returns to its starting point at the end. With the dimensionless acceleration parameter $\alpha = aT$, show that the total proper time elapsed for the traveller is
$$\tau_{\text{trav}} = \frac{4T}{\alpha}\,\operatorname{arsinh}\!\Big(\frac{\alpha}{4}\Big) \;\le\; T,$$
while a stay-at-home inertial observer ages $T$. (Here $\operatorname{arsinh} x = \ln(x + \sqrt{x^2+1})$.)
4. Examine the two limits $\alpha \to 0$ (gentle acceleration) and $\alpha \to \infty$ (ultra-relativistic), and interpret each physically.

**Recall:**

![[Def - Proper Time#The Definition]]

The [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is $U^\mu = \gamma(1, \mathbf u)$ with $U \cdot U = 1$; for one-dimensional motion the **proper acceleration** is $a = \|A\| = \gamma^3|du/dt|$, the magnitude of the [[Def - Four-Velocity and Four-Acceleration|four-acceleration]]. A constant-proper-acceleration worldline has a [[Def - Rapidity|rapidity]] $\varphi = \operatorname{arctanh} u$ that grows linearly with proper time, $\varphi = a\tau$.

---

# Convergent Strategy

**Problem class.** A *compute-proper-time-along-a-worldline* problem — the central computation of the chapter, and the one that makes the [[Ex - The twin paradox|twin paradox]] quantitative. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: parametrise the worldline, write $\tau = \int\sqrt{ds^2} = \int dt/\gamma$, and integrate; the only skill is choosing a parametrisation that makes the integral doable.

**Assumption pattern.** "Constant proper acceleration" is the key phrase: it means the [[Def - Rapidity|rapidity]] increases linearly with proper time, $\varphi = a\tau$, which is what makes the four-velocity hyperbolic-trigonometric and the integral elementary. Recognising that constant proper acceleration $\Leftrightarrow$ linear rapidity $\Leftrightarrow$ hyperbolic worldline is the unlock.

**Theorem routing.** Part 1 uses the rapidity parametrisation of the four-velocity, then integrates $U = dX/d\tau$. Part 2 inverts the hyperbolic functions. Part 3 stitches three arcs together by continuity of proper time and integrates $d\tau = dt/\gamma = dt/\sqrt{1 + a^2(t - t_0)^2}$ via the substitution $a(t - t_0) = \sinh\psi$, landing on $\operatorname{arsinh}$. The inequality $\tau_{\text{trav}} \le T$ is the quantitative form of [[Thm - Inertial Worldlines Maximise Proper Time]].

**Key decision point.** The non-obvious move is to parametrise by the *rapidity* (equivalently, to recognise constant proper acceleration as linear-in-$\tau$ rapidity). This converts the daunting "integrate proper time along an accelerated path" into the one-line hyperbolic identity $\int\sqrt{dt^2 - dx^2}$ with $x = a^{-1}\cosh$, $t = a^{-1}\sinh$. The naive alternative — integrating the coordinate acceleration $d^2x/dt^2$, which is *not* constant — leads to a messier $(1 + \cdots)^{-3/2}$ integrand and obscures the hyperbola.

---

# Legal Operations Used

1. **Switch to rapidity to make the boost structure additive** (operation 6 from the topic page). Constant proper acceleration means the rapidity grows linearly, $\varphi = a\tau$, so $U = (\cosh a\tau, \sinh a\tau, 0, 0)$ — the parametrisation that makes the worldline a hyperbola.

2. **Differentiate/integrate with respect to proper time** (operation 5 from the topic page). The worldline is recovered by integrating $U = dX/d\tau$, and the proper time is recovered by integrating $d\tau = dt/\gamma$.

3. **Compute an invariant in the convenient form** (operation 7 from the topic page). The proper time $\int\sqrt{ds^2}$ is frame-independent; evaluating it via the hyperbolic substitution is the clean route.

---

# Hints

> [!note]- Hint 1
> Constant proper acceleration $a$ means the four-velocity satisfies $dU/d\tau = A$ with $\|A\| = a$ constant and $A \cdot U = 0$. In $1+1$ dimensions the unit timelike vector with these properties is $U = (\cosh\varphi, \sinh\varphi, 0, 0)$ with $\varphi = a\tau$ (rapidity linear in proper time). Integrate $dX/d\tau = U$ to get $t(\tau), x(\tau)$.

> [!note]- Hint 2
> From part 1, $t = a^{-1}\sinh a\tau$ and $x = a^{-1}\cosh a\tau$. Invert the first: $a\tau = \operatorname{arsinh}(at)$, so $\tau = a^{-1}\operatorname{arsinh}(at)$. Eliminating $\tau$ gives $x^2 - t^2 = a^{-2}$, a hyperbola.

> [!note]- Hint 3
> Along any single arc, $d\tau = dt\sqrt{1 - u^2} = dt/\gamma$, and for constant proper acceleration $\gamma = \cosh a\tau = \sqrt{1 + (a(t - t_0))^2}$. So $\tau = \int dt/\sqrt{1 + a^2(t-t_0)^2}$; substitute $a(t - t_0) = \sinh\psi$. The full traveller is four arcs each lasting coordinate time $T/4$; by symmetry the total proper time is $4$ times the proper time of the first quarter-arc.

> [!note]- Hint 4
> For $\alpha \to 0$, Taylor-expand $\operatorname{arsinh}(\alpha/4) \approx \alpha/4 - \tfrac{1}{6}(\alpha/4)^3$, so $\tau_{\text{trav}} \to T$ (Newtonian: no differential ageing). For $\alpha \to \infty$, $\operatorname{arsinh}(\alpha/4) \approx \ln(\alpha/2)$, so $\tau_{\text{trav}} \approx (4T/\alpha)\ln(\alpha/2) \to 0$: the worldline approaches a null zigzag (light out and back), which has zero proper time.

---

# Solution

This is the engine behind the twin paradox: a clean, finite-acceleration computation showing exactly how much proper time a wandering clock loses. The plan: Step 1 derives the hyperbolic worldline from constant proper acceleration; Step 2 inverts to get $\tau(t)$; Step 3 assembles the four-arc journey and integrates to the $\operatorname{arsinh}$ formula; Step 4 reads off the Newtonian and ultra-relativistic limits.

**Step 1: Constant proper acceleration gives a hyperbolic worldline.**

> [!note]- Derivation
> The four-velocity is a unit timelike vector, $U \cdot U = 1$. In $1+1$ dimensions every such future-directed vector is $U^\mu = (\cosh\varphi, \sinh\varphi, 0, 0)$ for some [[Def - Rapidity|rapidity]] $\varphi(\tau)$ (this automatically gives $U \cdot U = \cosh^2 - \sinh^2 = 1$). The four-acceleration is
> $$A^\mu = \frac{dU^\mu}{d\tau} = \dot\varphi\,(\sinh\varphi, \cosh\varphi, 0, 0),$$
> with norm $\|A\| = \sqrt{-A \cdot A} = \sqrt{-\dot\varphi^2(\sinh^2 - \cosh^2)} = |\dot\varphi|$. So **constant proper acceleration $a$ means $\dot\varphi = a$, i.e. $\varphi = a\tau$** (taking $\varphi(0) = 0$, rest at $\tau = 0$). Hence
> $$U^\mu = (\cosh a\tau, \sinh a\tau, 0, 0).$$
> Integrating $dX^\mu/d\tau = U^\mu$ with $X(0) = (0, a^{-1}, 0, 0)$ (chosen so the constant of integration is clean):
> $$t(\tau) = \frac{1}{a}\sinh a\tau, \qquad x(\tau) = \frac{1}{a}\cosh a\tau, \qquad y = z = 0.$$
> Eliminating $\tau$ via $\cosh^2 - \sinh^2 = 1$ gives
> $$x^2 - t^2 = \frac{1}{a^2},$$
> the equation of a **hyperbola** in the $(t, x)$-plane with asymptotes the light rays $x = \pm t$. Uniformly accelerated motion is hyperbolic motion — the relativistic replacement for the Newtonian parabola $x = \tfrac12 a t^2$.

**Step 2: Proper time as a function of coordinate time.**

> [!note]- Derivation
> From $t = a^{-1}\sinh a\tau$, invert: $a\tau = \operatorname{arsinh}(at)$, so
> $$\tau(t) = \frac{1}{a}\operatorname{arsinh}(at) = \frac{1}{a}\ln\!\Big(at + \sqrt{1 + a^2 t^2}\Big).$$
> The Lorentz factor along the way is $\gamma = dt/d\tau = \cosh a\tau = \sqrt{1 + \sinh^2 a\tau} = \sqrt{1 + (at)^2}$. Since $\operatorname{arsinh}(at) \le at$ for $at \ge 0$ (equality only at $t = 0$), we have $\tau(t) \le t$: the moving clock reads less than coordinate time, with the deficit growing as the speed builds. This is time dilation, here accumulated continuously along the accelerating worldline; the inequality is the local statement $d\tau = dt/\gamma \le dt$ integrated.

**Step 3: The Langevin traveller's total proper time.**

> [!note]- Derivation
> The traveller's worldline is **four quarter-arcs** of constant proper acceleration, each lasting coordinate time $T/4$: accelerate forward on $[0, T/4]$, decelerate (thrust reversed) on $[T/4, T/2]$, accelerate backward on $[T/2, 3T/4]$, decelerate to rest on $[3T/4, T]$, returning to the start. (This is the "tri-hyperbolic" worldline; the thrust reversals at $T/4$ and $3T/4$ are where the four-acceleration flips sign.) On each arc the speed profile is the mirror image of the others, so each arc contributes the same proper time, and by symmetry
> $$\tau_{\text{trav}} = 4 \times \big(\text{proper time of the first quarter-arc}\big).$$
> On the first arc, starting from rest, $\gamma = \sqrt{1 + (at)^2}$ as in Step 2, so
> $$\tau_{\text{quarter}} = \int_0^{T/4}\frac{dt}{\gamma} = \int_0^{T/4}\frac{dt}{\sqrt{1 + a^2 t^2}}.$$
> Substitute $at = \sinh\psi$, $a\,dt = \cosh\psi\,d\psi$, $\sqrt{1 + a^2t^2} = \cosh\psi$:
> $$\tau_{\text{quarter}} = \int \frac{\cosh\psi\,d\psi/a}{\cosh\psi} = \frac{1}{a}\,\psi\Big|_0^{\,\psi(T/4)} = \frac{1}{a}\operatorname{arsinh}\!\Big(\frac{aT}{4}\Big).$$
> With the dimensionless parameter $\alpha = aT$, so $a = \alpha/T$ and $aT/4 = \alpha/4$,
> $$\tau_{\text{trav}} = 4 \cdot \frac{1}{a}\operatorname{arsinh}\!\Big(\frac{\alpha}{4}\Big) = \frac{4T}{\alpha}\operatorname{arsinh}\!\Big(\frac{\alpha}{4}\Big).$$
> Because $\operatorname{arsinh} x \le x$, we get $\tau_{\text{trav}} \le (4T/\alpha)(\alpha/4) = T$: **the traveller ages no more than the stay-at-home observer**, with strict inequality whenever $\alpha > 0$. The stay-at-home observer, inertial, ages exactly the coordinate time $T$. This is the quantitative twin paradox, and the inequality is the special-relativistic [[Thm - Inertial Worldlines Maximise Proper Time|geodesic principle]] made explicit.

**Step 4: The two limits.**

> [!note]- Derivation
> *Gentle acceleration, $\alpha \to 0$.* Expand $\operatorname{arsinh}(\alpha/4) = \alpha/4 - \tfrac16(\alpha/4)^3 + \cdots$, so
> $$\tau_{\text{trav}} = \frac{4T}{\alpha}\Big[\frac{\alpha}{4} - \frac{1}{6}\Big(\frac{\alpha}{4}\Big)^3 + \cdots\Big] = T\Big[1 - \frac{1}{6}\Big(\frac{\alpha}{4}\Big)^2 + \cdots\Big] \to T.$$
> In the Newtonian limit (low speeds, the traveller never gets close to $c$) there is no differential ageing: $\tau_{\text{trav}} \to T$, as Newtonian absolute time demands. The leading correction is second order in $\alpha$, the relativistic effect switching on quadratically.
>
> *Ultra-relativistic, $\alpha \to \infty$.* Here $\operatorname{arsinh}(\alpha/4) \approx \ln(\alpha/2)$, so
> $$\tau_{\text{trav}} \approx \frac{4T}{\alpha}\ln\!\Big(\frac{\alpha}{2}\Big) \to 0.$$
> As the acceleration (and hence the peak speed) grows without bound, the traveller's worldline approaches a null zigzag — light out to the turning point and back — which has **zero** proper time. The traveller ages arbitrarily little while the stay-at-home observer ages $T$. There is no positive lower bound on the traveller's proper time, exactly matching the statement that the infimum of proper time over worldlines is $0$ (approached but never attained).

> [!note]- Complete formal solution
> Constant proper acceleration $a$ forces the rapidity to grow linearly, $\varphi = a\tau$, so $U = (\cosh a\tau, \sinh a\tau, 0, 0)$; integrating $dX/d\tau = U$ gives $t = a^{-1}\sinh a\tau$, $x = a^{-1}\cosh a\tau$, whence $x^2 - t^2 = a^{-2}$ — a hyperbola. Inverting, $\tau(t) = a^{-1}\operatorname{arsinh}(at) \le t$, with $\gamma = \sqrt{1 + (at)^2}$. The Langevin traveller is four quarter-arcs of coordinate duration $T/4$; by symmetry $\tau_{\text{trav}} = 4\int_0^{T/4} dt/\sqrt{1 + a^2t^2}$, and the substitution $at = \sinh\psi$ gives $\tau_{\text{trav}} = (4/a)\operatorname{arsinh}(aT/4) = (4T/\alpha)\operatorname{arsinh}(\alpha/4)$ with $\alpha = aT$. Since $\operatorname{arsinh} x \le x$, $\tau_{\text{trav}} \le T$, the inertial observer's age. As $\alpha \to 0$, $\tau_{\text{trav}} \to T$ (Newtonian, no differential ageing); as $\alpha \to \infty$, $\tau_{\text{trav}} \approx (4T/\alpha)\ln(\alpha/2) \to 0$ (worldline approaches a null zigzag of zero proper time). $\blacksquare$

> [!warning] Illegal but tempting: using the coordinate acceleration $d^2x/dt^2$ as "the acceleration"
> One might try to model "constant acceleration" by $d^2x/dt^2 = a$ (constant *coordinate* acceleration), giving the Newtonian parabola $x = \tfrac12 a t^2$. This is wrong relativistically and unphysical: it would drive the speed past $c$ in finite time. The physically meaningful, frame-independent quantity is the *proper* acceleration $\|A\| = \gamma^3|d^2x/dt^2|$ — what the rocket's accelerometer reads — and holding *it* constant gives the hyperbola, with coordinate acceleration $d^2x/dt^2 = a/\gamma^3 = a(1 + a^2t^2)^{-3/2}$ that *decreases* as the speed builds, keeping $u < 1$ forever. The lesson: in relativity "constant acceleration" must mean constant *proper* acceleration, and the diagnostic is that $\|A\|$, not $d^2x/dt^2$, is the invariant.

---

# Key Takeaways

**Constant proper acceleration is linear rapidity is hyperbolic motion — the relativistic uniform acceleration.** The phrase "constant proper acceleration" should immediately trigger the substitution $\varphi = a\tau$ (rapidity linear in proper time), giving $U = (\cosh a\tau, \sinh a\tau, 0, 0)$ and the worldline $x^2 - t^2 = a^{-2}$. This is the relativistic analogue of the Newtonian "$x = \tfrac12 a t^2$", with the parabola replaced by a hyperbola whose asymptotes are light rays — so the particle approaches but never reaches $c$, no matter how long it accelerates. The reusable recognition: hyperbolic functions of proper time are the fingerprint of constant proper acceleration, exactly as trigonometric functions of time are the fingerprint of simple harmonic motion. Any "rocket with constant thrust" or "uniformly accelerated observer" problem ([[Special Relativity XVI — Accelerated Observers|Rindler coordinates]]) is this worldline.

**Proper time of an accelerated clock is $\int dt/\gamma$, and the hyperbolic substitution makes it elementary.** The general recipe for "how much time elapses for the moving clock" is $\tau = \int d\tau = \int dt/\gamma$ along the worldline; the art is choosing variables that make the integral doable. For constant proper acceleration, $\gamma = \sqrt{1 + (at)^2}$ and the substitution $at = \sinh\psi$ turns the integral into $\int d\psi$, yielding the inverse hyperbolic sine. The trigger is any $\sqrt{1 + (\text{linear})^2}$ integrand — reach for $\sinh\psi$ (or $\tan\psi$ for $\sqrt{1 - (\cdots)^2}$). The structural payoff is the formula $\tau_{\text{trav}} = (4T/\alpha)\operatorname{arsinh}(\alpha/4)$, which is the *quantitative* twin paradox: it tells you exactly how much the traveller ages for any acceleration, and its limits recover both the Newtonian no-effect regime and the ultra-relativistic light-zigzag regime.

**The proper-time deficit interpolates between zero (Newtonian) and total (light): the geodesic principle, made numerical.** The inequality $\tau_{\text{trav}} \le T$ is the [[Thm - Inertial Worldlines Maximise Proper Time|geodesic principle]] for this specific worldline, and the two limits frame its meaning. At low acceleration the deficit is $O(\alpha^2)$ — negligible, which is why everyday life shows no twin effect. At extreme acceleration the traveller's proper time collapses toward zero, because the worldline bends toward the null zigzag of a light ray, and null worldlines carry no proper time. So "how much ageing the traveller loses" is controlled entirely by how close their worldline comes to the light cone — the bendier and faster the path, the larger the deficit, with the straight inertial path losing nothing and the light-speed path losing everything. This is the same statement as the reversed triangle inequality, now read as a continuous knob ($\alpha$) rather than a discrete kink. See [[Ex - A round trip to the galactic centre]] for these formulas applied to a journey across the galaxy, and [[Ex - The twin paradox]] for the idealised instantaneous-turnaround version.
