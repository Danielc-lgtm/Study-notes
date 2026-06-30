---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Expression of the Four-Acceleration"
  - "Def - Acceleration Relative to an Observer"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ and an inertial observer $\mathcal{O}$ of four-velocity $U_0$:

1. A particle $\mathcal{P}$ moves collinearly along $e_1$ with speed $V(t)$ and relative acceleration $\boldsymbol\gamma = \dot V\,e_1$ (so $\boldsymbol\gamma \parallel \mathbf V$). Using [[Thm - Expression of the Four-Acceleration|the expression of the four-acceleration]], show that the norm of the four-acceleration is $\|A\|_g = \Gamma^3|\dot V|$, and that at momentary rest ($V = 0$) this is just $\|A\|_g = |\dot V| = |\boldsymbol\gamma|$.
2. A spaceship maintains a constant proper acceleration — its onboard accelerometer reads a fixed $a$ at all times (the crew feels constant artificial gravity $a$). Show that this means $\|A\|_g = a$ for all time, hence $\Gamma^3\dot V = a$, and integrate to find $V(t)$ with $V(0) = 0$.
3. From $V(t)$, find the spaceship's lab-frame position $x(t)$ and show the worldline is a branch of the hyperbola $\big(x + 1/a\big)^2 - t^2 = 1/a^2$ — *hyperbolic motion*, not the parabola of Newtonian constant acceleration.
4. Explain physically why the *relative* acceleration $\boldsymbol\gamma = \dot V$ decreases toward zero as $t \to \infty$, even though the *proper* acceleration $a$ stays constant, and what this says about the spaceship's approach to the speed of light.

**Recall:**

The exercise rests on the expression of the four-acceleration and the distinction between the two accelerations.

![[Thm - Expression of the Four-Acceleration#Statement]]

The [[Def - Acceleration Relative to an Observer|relative acceleration]] $\boldsymbol\gamma = \mathrm{d}\mathbf V/\mathrm{d}t$ is differentiated with respect to the observer's clock and is observer-dependent; the [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm{d}U/\mathrm{d}\tau'$ is a four-vector, observer-independent, and its norm $\|A\|_g = \sqrt{-A\cdot A}$ is the *proper acceleration*, the accelerometer reading. The two coincide, $A = \boldsymbol\gamma$, exactly at momentary rest.

---

# Convergent Strategy

**Problem class.** An *acceleration* problem of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|third strategy]]: to find the physically meaningful, frame-independent proper acceleration, use the expression of the four-acceleration and specialise to momentary rest, then impose constancy of the proper acceleration to integrate the trajectory.

**Assumption pattern.** Collinear motion ($\boldsymbol\gamma \parallel \mathbf V$) simplifies the norm formula to a single $\Gamma^3$ factor — the signal that the parallel component is "weighted" by $\Gamma^2$ relative to transverse. The phrase "accelerometer reads a constant $a$" is the signpost (per the third source of the four-acceleration theorem) that the *proper* acceleration is prescribed, $\|A\|_g = a$, which becomes a differential equation. The boundary condition $V(0) = 0$ fixes the integration constants.

**Theorem routing.** Part 1 specialises the norm formula of [[Thm - Expression of the Four-Acceleration]] to collinear motion ($\gamma_\perp = 0$, $\gamma_\parallel = \dot V$), giving $\|A\|_g = \Gamma^2\sqrt{\Gamma^2\dot V^2} = \Gamma^3|\dot V|$, and to momentary rest. Part 2 sets this constant, $\Gamma^3\dot V = a$, and integrates using [[Def - Acceleration Relative to an Observer|the relative acceleration]] $\boldsymbol\gamma = \dot V$. Part 3 integrates $V = \dot x$ to get the hyperbola, the worldline of [[Special Relativity XVI — Accelerated Observers|uniformly accelerated motion]]. Part 4 interprets the falling relative acceleration via the speed ceiling of [[Thm - Maximum Relative Velocity is c]].

**Key decision point.** The conceptual crux is that *constant proper acceleration produces decreasing coordinate acceleration* — the opposite of the Newtonian intuition that constant acceleration means $V$ grows without bound. The resolution is the factor $\Gamma^3$: as the speed grows, $\Gamma^3$ grows, so to keep $\Gamma^3\dot V = a$ constant, $\dot V$ must shrink. The natural error is to set $\dot V = a$ constant (Newtonian), which would push $V$ past $c$; the correct constant is the *proper* acceleration $\Gamma^3\dot V$, which keeps $V$ below $c$ forever.

---

# Legal Operations Used

1. **Differentiate the four-velocity to get the four-acceleration** (operation 6 from the topic page). The norm $\|A\|_g$ is computed from the four-acceleration via the expression theorem.

2. **Specialise to the simplest case** (operation 7). Collinear motion ($\gamma_\perp = 0$) and momentary rest ($V = 0$) collapse the general norm formula to $\Gamma^3|\dot V|$ and then to $|\dot V|$.

3. **Evaluate a four-vector invariant in any frame** (operation 9). The proper acceleration $\|A\|_g$ is a scalar; setting it constant is a frame-independent condition that integrates to the trajectory.

4. **Use the speed–Lorentz-factor relation** (operation 4). $\Gamma = (1-V^2)^{-1/2}$ converts the differential equation $\Gamma^3\dot V = a$ into a separable form integrable in closed form.

---

# Hints

> [!note]- Hint 1
> For collinear motion the transverse part $\gamma_\perp = 0$ and $\gamma_\parallel = \dot V$, so the norm formula $\|A\|_g = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}$ becomes $\Gamma^2\sqrt{\Gamma^2\dot V^2} = \Gamma^3|\dot V|$. At $V = 0$, $\Gamma = 1$, so $\|A\|_g = |\dot V|$.

> [!note]- Hint 2
> Constant proper acceleration means $\|A\|_g = a$, i.e. $\Gamma^3\dot V = a$. Since $\Gamma^3 = (1-V^2)^{-3/2}$, this is $\dot V/(1-V^2)^{3/2} = a$. The left side is $\mathrm{d}/\mathrm{d}t[V/\sqrt{1-V^2}]$ — recognise the derivative of $\gamma V$ — so $\gamma V = at$ (with $V(0)=0$), giving $V = at/\sqrt{1 + (at)^2}$.

> [!note]- Hint 3
> Integrate $V = \dot x = at/\sqrt{1+(at)^2}$. The antiderivative is $x(t) = \frac{1}{a}\sqrt{1 + (at)^2} + C$ for a constant $C$. Choosing $x(0) = 0$ gives $x + 1/a = \frac{1}{a}\sqrt{1+(at)^2}$, and squaring yields $(x+1/a)^2 - t^2 = 1/a^2$ — a hyperbola.

> [!note]- Hint 4
> From $V = at/\sqrt{1+(at)^2}$, the relative acceleration is $\dot V = a/(1+(at)^2)^{3/2} = a/\Gamma^3 \to 0$ as $t \to \infty$. The proper acceleration stays $a$, but the *observed* acceleration falls because the speed asymptotes to $c$ ($V \to 1$) and can change ever more slowly as it nears the ceiling.

---

# Solution

The route is to compute the proper acceleration for collinear motion, set it constant to get a differential equation for the velocity, integrate twice for the hyperbolic worldline, and interpret the falling coordinate acceleration. Step 1 gives $\|A\|_g = \Gamma^3|\dot V|$ and its momentary-rest value; Step 2 integrates the constant-proper-acceleration condition for $V(t)$; Step 3 integrates again for $x(t)$ and identifies the hyperbola; Step 4 explains why $\dot V \to 0$. The non-obvious thread is the factor $\Gamma^3$: it is what makes constant proper acceleration produce a bounded, asymptotic velocity rather than an unbounded one.

**Step 1: For collinear motion, $\|A\|_g = \Gamma^3|\dot V|$, reducing to $|\dot V| = |\boldsymbol\gamma|$ at momentary rest.**

> [!note]- Derivation
> By [[Thm - Expression of the Four-Acceleration|the expression of the four-acceleration]], the proper-acceleration norm is
> $$\|A\|_g = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2},$$
> where $\gamma_\parallel$ and $\gamma_\perp$ are the components of $\boldsymbol\gamma$ parallel and transverse to $\mathbf V$. For collinear motion $\boldsymbol\gamma = \dot V\,e_1$ is entirely parallel to $\mathbf V = V e_1$, so $\gamma_\parallel = \dot V$ and $\gamma_\perp = 0$. Hence
> $$\|A\|_g = \Gamma^2\sqrt{\Gamma^2\dot V^2 + 0} = \Gamma^2\cdot\Gamma|\dot V| = \Gamma^3|\dot V|.$$
> At momentary rest, $V = 0$ so $\Gamma = 1$, and
> $$\|A\|_g\big|_{V=0} = |\dot V| = |\boldsymbol\gamma|.$$
> This is the boxed identity of the theorem: at momentary rest the four-acceleration equals the relative acceleration, so its norm — the proper acceleration — is just the magnitude of the relative acceleration measured by the comoving observer. The factor $\Gamma^3$ at general speeds is what distinguishes the proper acceleration from the observed one.

**Step 2: Constant proper acceleration gives $V(t) = at/\sqrt{1 + (at)^2}$.**

> [!note]- Derivation
> The accelerometer reads a constant $a$, so the proper acceleration is constant: $\|A\|_g = a$, i.e.
> $$\Gamma^3\dot V = a,\qquad\text{i.e.}\qquad \frac{\dot V}{(1 - V^2)^{3/2}} = a.$$
> The left-hand side is a total derivative: note $\dfrac{\mathrm{d}}{\mathrm{d}t}\dfrac{V}{\sqrt{1-V^2}} = \dfrac{\dot V}{\sqrt{1-V^2}} + \dfrac{V^2\dot V}{(1-V^2)^{3/2}} = \dfrac{\dot V(1-V^2) + V^2\dot V}{(1-V^2)^{3/2}} = \dfrac{\dot V}{(1-V^2)^{3/2}}$. So the equation is
> $$\frac{\mathrm{d}}{\mathrm{d}t}\big(\Gamma V\big) = a,$$
> which integrates immediately, with $V(0) = 0$ (hence $\Gamma V = 0$ at $t=0$), to
> $$\Gamma V = at,\qquad\text{i.e.}\qquad \frac{V}{\sqrt{1-V^2}} = at.$$
> Solving for $V$: square to get $V^2 = a^2t^2(1-V^2)$, so $V^2(1 + a^2t^2) = a^2t^2$, giving
> $$V(t) = \frac{at}{\sqrt{1 + (at)^2}}.$$
> The combination $\Gamma V$ — the *proper velocity* (celerity) — grows linearly with lab time, $\Gamma V = at$, which is the clean statement of constant proper acceleration. The ordinary velocity $V$ asymptotes to $1$ as $t \to \infty$ but never reaches it.

**Step 3: The worldline is the hyperbola $(x + 1/a)^2 - t^2 = 1/a^2$.**

> [!note]- Derivation
> Integrate $V = \dot x = at/\sqrt{1 + (at)^2}$. Let $u = 1 + (at)^2$, $\mathrm{d}u = 2a^2 t\,\mathrm{d}t$, so
> $$x(t) = \int \frac{at}{\sqrt{1 + (at)^2}}\,\mathrm{d}t = \frac{1}{a}\sqrt{1 + (at)^2} + C.$$
> Choosing $x(0) = 0$ gives $0 = \frac{1}{a}\sqrt{1} + C$, so $C = -1/a$ and
> $$x(t) + \frac{1}{a} = \frac{1}{a}\sqrt{1 + (at)^2}.$$
> Squaring,
> $$\Big(x + \frac{1}{a}\Big)^2 = \frac{1}{a^2}\big(1 + a^2t^2\big) = \frac{1}{a^2} + t^2,$$
> so
> $$\boxed{\;\Big(x + \tfrac{1}{a}\Big)^2 - t^2 = \frac{1}{a^2}\;}$$
> a branch of a hyperbola in the $(t, x)$-plane, with asymptotes $x + 1/a = \pm t$ (the light cone through the point $x = -1/a$, $t = 0$). This is **hyperbolic motion** — the relativistic worldline of constant proper acceleration — and it is emphatically *not* the Newtonian parabola $x = \tfrac12 a t^2$, which it approximates only for small $at$ (early times, low speed). The asymptote $x + 1/a = t$ means the spaceship's worldline never crosses the light ray emitted from $x = -1/a$ at $t = 0$: that ray is the **Rindler horizon**, a boundary the eternally accelerating ship can never receive a signal from beyond.

**Step 4: The relative acceleration $\dot V = a/\Gamma^3 \to 0$ as the speed asymptotes to $c$.**

> [!note]- Derivation
> Differentiate $V(t) = at/\sqrt{1 + (at)^2}$:
> $$\dot V = \frac{a\sqrt{1+(at)^2} - at\cdot\frac{a^2 t}{\sqrt{1+(at)^2}}}{1 + (at)^2} = \frac{a(1+(at)^2) - a^3t^2}{(1+(at)^2)^{3/2}} = \frac{a}{(1 + (at)^2)^{3/2}}.$$
> Since $\Gamma = \sqrt{1 + (at)^2}$ here (from $\Gamma V = at$ and $V = at/\sqrt{1+(at)^2}$, one finds $\Gamma = \sqrt{1+(at)^2}$), this is exactly
> $$\dot V = \frac{a}{\Gamma^3} = \boldsymbol\gamma\quad(\text{collinear}),$$
> consistent with $\|A\|_g = \Gamma^3\dot V = a$ from Step 1. As $t \to \infty$, $\Gamma \to \infty$ and $\dot V = a/\Gamma^3 \to 0$: the *relative* (observed) acceleration falls to zero. The physical reason is the speed ceiling. The spaceship's speed $V \to 1 = c$ asymptotically, and as it crowds against the light barrier it has less and less room to speed up, so the *observed* rate of change of velocity must shrink even though the crew feels the same steady push $a$. The proper acceleration stays $a$ — the engines work just as hard, the artificial gravity is constant — but the lab sees the velocity creep toward $c$ ever more slowly. This is the kinematic content of [[Thm - Maximum Relative Velocity is c|the speed ceiling]] for an accelerating particle: constant proper acceleration, asymptotic approach to $c$, never reaching it.

> [!note]- Complete formal solution
> For collinear motion the proper-acceleration norm from [[Thm - Expression of the Four-Acceleration|the four-acceleration]] is $\|A\|_g = \Gamma^2\sqrt{\Gamma^2\dot V^2} = \Gamma^3|\dot V|$, reducing at momentary rest ($V=0$, $\Gamma=1$) to $|\dot V| = |\boldsymbol\gamma|$. Constant proper acceleration $\|A\|_g = a$ gives $\Gamma^3\dot V = a$, i.e. $\frac{\mathrm{d}}{\mathrm{d}t}(\Gamma V) = a$, which integrates (with $V(0)=0$) to $\Gamma V = at$, hence $V = at/\sqrt{1+(at)^2}$. Integrating $V = \dot x$ gives $x + 1/a = \frac{1}{a}\sqrt{1+(at)^2}$, so $(x+1/a)^2 - t^2 = 1/a^2$ — hyperbolic motion, with asymptote the Rindler horizon $x + 1/a = t$, not the Newtonian parabola. The relative acceleration $\dot V = a/\Gamma^3 \to 0$ as $t\to\infty$ while the proper acceleration stays $a$: the speed asymptotes to $c$ and changes ever more slowly as it nears the ceiling, even though the crew feels constant artificial gravity. $\blacksquare$

---

# Key Takeaways

**Proper acceleration is the four-acceleration norm, computed cleanly at momentary rest where it equals the ordinary acceleration.** The physically meaningful, frame-independent acceleration of a particle — what an accelerometer reads, what the crew of a ship feels as weight — is $\|A\|_g = \sqrt{-A\cdot A}$, a scalar built from the four-vector $A$. The fastest way to compute it is to go to the comoving inertial frame, where, by the momentary-rest identity $A = \boldsymbol\gamma$, it is just the magnitude of the ordinary relative acceleration. The exercise shows the general collinear formula $\|A\|_g = \Gamma^3|\dot V|$ and its reduction to $|\dot V|$ at $V = 0$. The reusable trigger: whenever a problem mentions an accelerometer reading, a felt acceleration, or "proper acceleration", that is $\|A\|_g$, and to compute it you evaluate the four-acceleration in the instantaneous rest frame where it is the Newtonian-looking $\boldsymbol\gamma$. The factor $\Gamma^3$ (collinear) or $\Gamma^2$ (transverse) is the difference between this invariant and the speed-dependent observed acceleration.

**Constant proper acceleration produces hyperbolic motion, not the Newtonian parabola — the factor $\Gamma^3$ caps the velocity.** This is the signature result of relativistic uniform acceleration and the conceptual heart of the exercise. Newtonian constant acceleration gives $V = at$, growing without bound and crossing $c$; relativistic constant *proper* acceleration gives $\Gamma V = at$, so the *proper velocity* grows linearly but the *ordinary velocity* $V = at/\sqrt{1+(at)^2}$ asymptotes to $c$. The worldline is a hyperbola $x^2 - t^2 = \text{const}$, the Lorentzian analogue of a circle (constant curvature), with the light cone as its asymptote — the Rindler horizon. The mechanism is the $\Gamma^3$ in $\|A\|_g = \Gamma^3\dot V$: holding the proper acceleration fixed while $\Gamma$ grows forces the coordinate acceleration $\dot V$ down, so the velocity creeps toward $c$ ever more slowly. The reusable principle: in any constant-proper-acceleration problem, integrate $\Gamma V = at$ (proper velocity linear in time), not $V = at$, and expect a hyperbola.

**The crew feels a steady push while the lab sees the acceleration die away — proper and coordinate acceleration are genuinely different physical quantities.** The exercise makes vivid that "acceleration" is not one thing: the proper acceleration $a$ (what the crew feels, the accelerometer reading, constant) and the relative acceleration $\dot V = a/\Gamma^3$ (what the lab observer measures, falling to zero) diverge dramatically at high speed. The engines work just as hard throughout, the artificial gravity never changes, yet an outside observer sees the ship's velocity change ever more slowly as it nears $c$. This is the reciprocal of the earlier lesson that the *relative* acceleration is observer-dependent while the four-acceleration is invariant: here the invariant ($\|A\|_g = a$) stays fixed while the observer-dependent quantity ($\dot V$) decays. The diagnostic to carry forward: if asked what is felt onboard, it is the proper acceleration $\|A\|_g$; if asked what a distant observer measures, it is the relative acceleration $\boldsymbol\gamma$, smaller by $\Gamma^3$ (collinear). This hyperbolic-motion analysis is the foundation of the accelerated-observer programme, the Rindler horizon, and the Unruh effect, all developed in [[Special Relativity XVI — Accelerated Observers]].
