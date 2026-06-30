---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Rindler Coordinates and the Accelerated Frame"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity]
---

# Problem Statement

A free particle $\mathcal{P}$ of mass $m$ moves inertially (straight worldline) and is, at the moment $t = 0$, at rest in the inertial frame $\mathcal{O}_*$ at inertial position $x_* = b$ (with $b > -a^{-1}$). A uniformly accelerated observer $\mathcal{O}$ of proper acceleration $a$ watches it in Rindler coordinates. Working with $c = 1$ except where restored:

1. Find the particle's Rindler position $x(t)$ as a function of $\mathcal{O}$'s proper time, and show that $\mathcal{O}$ sees the particle "fall": $x(t) = (b + a^{-1})/\cosh(act) - a^{-1}$.
2. Take the low-velocity limit and show $x(t) \simeq b - \tfrac12 g t^2$ with $g = c^2 a$ — exactly the free-fall trajectory in a uniform gravitational field pointing toward $-x$.
3. Compute the energy $E$ of the particle measured by $\mathcal{O}$, $E = mc^2(1+ab)/(1+ax(t))$, and show $E$ is *not* constant (since $\mathcal{O}$ is not inertial).
4. Prove that $E' := E + mgx(t)$ *is* conserved (a constant of motion) — exactly the total energy (kinetic plus potential) of a body in a uniform gravitational field, the cleanest statement of the equivalence principle and the embryo of the geodesic principle.

**Recall:**

A [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] $\mathcal{O}$ carries [[Def - Rindler Coordinates and the Accelerated Frame|Rindler coordinates]] $(ct, x, y, z)$.

![[Def - Rindler Coordinates and the Accelerated Frame#The Definition]]

A free particle has a straight worldline (the law of inertia) and constant four-momentum $P = m\,U_{\mathcal{P}}$ with $U_{\mathcal{P}}$ its constant four-velocity. The energy $\mathcal{O}$ assigns is $E = P\cdot U$ where $U = \cosh(act)e_0^* + \sinh(act)e_1^*$ is $\mathcal{O}$'s four-velocity ([[Thm - Worldline of a Uniformly Accelerated Observer]]). **Equivalence principle:** $\mathcal{O}$'s frame is locally a uniform gravitational field of strength $g = c^2 a$ pointing toward decreasing $x$, with potential $\Phi = gx$.

---

# Convergent Strategy

**Problem class.** A *relativistic-effect-in-the-accelerated-frame* problem with an equivalence-principle payoff: track an inertial (free) worldline in the accelerated frame and show it looks like free fall. The decisive move is to find where the straight inertial worldline crosses $\mathcal{O}$'s rest spaces.

**Assumption pattern.** The particle is *free* — straight worldline, constant four-momentum $P$ — while the *observer* accelerates. The signpost is "free particle seen by accelerated observer": the particle does nothing, the apparent "fall" is entirely an artifact of $\mathcal{O}$'s accelerating frame. The starting condition "at rest at $x_* = b$, $t = 0$" pins the particle's worldline to the vertical line $x_* = b$.

**Theorem routing.** The route is: the particle's worldline is $x_* = b$ (vertical) $\Rightarrow$ intersect with $\mathcal{O}$'s rest space $\mathcal{E}_u(t)$ (the line through $A$ of slope $\tanh(act)$) to get the Rindler position $x(t)$ $\Rightarrow$ low-velocity expansion gives free-fall; $\Rightarrow$ energy $E = P\cdot U$ via the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]] $\Rightarrow$ show $E + mgx$ is conserved by direct substitution. The equivalence principle reads $g = c^2 a$, $\Phi = gx$.

**Key decision point.** The crux is that the particle's "fall" is *not* due to any force on the particle — it moves on a perfectly straight worldline, a geodesic — but is the appearance of that straight motion in $\mathcal{O}$'s curved (accelerating) frame. Turned around, this is the geodesic principle in embryo: in a gravitational field the freely-falling (geodesic) worldline is the natural one, and the "force of gravity" felt by $\mathcal{O}$ is really $\mathcal{O}$ being pushed by their rocket. The conserved $E + mgx$ is the signature.

---

# Legal Operations Used

1. **Read the Rindler metric off the coordinate transformation** (operation 4 from the topic page). The Rindler position $x(t)$ comes from intersecting the inertial worldline with $\mathcal{O}$'s simultaneity slices, equivalently inverting the Rindler transformation; the clock rate and energy follow from the metric.

2. **Use the rest space = simultaneity hypersurface identity for uniform acceleration** (operation 8 from the topic page). The particle's Rindler position $x(t)$ is defined by which rest space $\mathcal{E}_u(t)$ contains it; for the uniformly accelerated observer these are the straight lines through $A$, making the intersection elementary.

3. **Take the low-velocity / small-distance limit to recover Newtonian gravity** (operation 9 from the topic page). Expanding $x(t) = (b+a^{-1})/\cosh(act) - a^{-1}$ for $|act|\ll 1$ and $|ax|\ll 1$ gives the free-fall parabola $x\simeq b - \tfrac12 gt^2$ and the Newtonian energy $E\simeq mc^2 + \tfrac12 mV^2 - mg(x-b)$.

---

# Hints

> [!note]- Hint 1
> The particle's worldline is the vertical line $x_* = b$ in the inertial frame. Its Rindler coordinate $x(t)$ is found by asking: which of $\mathcal{O}$'s rest spaces $\mathcal{E}_u(t)$ (lines through $A = (0,-a^{-1})$ of slope $\tanh(act)$) passes through the particle's current position? Intersect $x_* = b$ with the rest space and invert the Rindler transformation $x_* = (x + a^{-1})\cosh(act) - a^{-1}$ to solve for $x$.

> [!note]- Hint 2
> Carrying out the intersection: at proper time $t$, the particle (still at $x_* = b$, having moved to $ct_* = \tanh(act)(b + a^{-1})$ along $\mathcal{O}$'s slice) has $x + a^{-1} = (b + a^{-1})/\cosh(act)$, so $x(t) = (b + a^{-1})/\cosh(act) - a^{-1}$. For small $act$, $\cosh(act)\approx 1 + \tfrac12(act)^2$, so $x\approx (b+a^{-1})[1 - \tfrac12(act)^2] - a^{-1} = b - \tfrac12(b+a^{-1})(act)^2$. For $|ab|\ll 1$, $x\approx b - \tfrac12 a c^2 t^2 = b - \tfrac12 g t^2$.

> [!note]- Hint 3
> The energy: the particle's four-momentum is $P = m U_{\mathcal{P}} = m e_0^*$ (at rest in $\mathcal{O}_*$). The energy $\mathcal{O}$ measures is $E = P\cdot U = m e_0^*\cdot[\cosh(act)e_0^* + \sinh(act)e_1^*] = mc^2\cosh(act)$ (restoring $c^2$). Using $\cosh(act) = (b + a^{-1})/(x + a^{-1}) = (1 + ab)/(1 + ax)$ from Step 1, $E = mc^2(1+ab)/(1+ax(t))$. It varies with $x(t)$ — not constant.

> [!note]- Hint 4
> For the conserved quantity, expand $E$ to low order: $E \simeq mc^2 + \tfrac12 mV^2 - mg(x - b)$ where $V$ is the particle's speed relative to $\mathcal{O}$ and $g = c^2 a$. The kinetic-plus-rest part is $mc^2 + \tfrac12 mV^2$; the position-dependent part is $-mgx + mgb$. So $E + mgx = mc^2 + \tfrac12 mV^2 + mgb = \mathrm{const}$ — total energy in a uniform field.

---

# Solution

A free particle's straight worldline, seen in $\mathcal{O}$'s accelerating frame, looks exactly like free fall in uniform gravity. Step 1 finds the Rindler trajectory by intersecting the inertial worldline with $\mathcal{O}$'s rest spaces. Step 2 takes the low-velocity limit and recovers the free-fall parabola. Step 3 computes the (non-constant) energy. Step 4 exhibits the conserved $E + mgx$, the equivalence-principle signature. The non-obvious content is that the "fall" is a frame artifact — the particle is on a geodesic, and $\mathcal{O}$ is the one being accelerated.

**Step 1: The Rindler trajectory is $x(t) = (b + a^{-1})/\cosh(act) - a^{-1}$.**

> [!note]- Derivation
> The free particle is at rest in $\mathcal{O}_*$ at $x_* = b$, so its worldline is the vertical line $x_* = b$, $y_* = z_* = 0$ (parametrised by $t_*$). To find its Rindler coordinate $x$ at $\mathcal{O}$'s proper time $t$, locate the event $M(t)$ where the particle's worldline meets $\mathcal{O}$'s rest space $\mathcal{E}_u(t)$. By [[Def - Rindler Coordinates and the Accelerated Frame|operation 8]] the rest space is the line through $A = (0, -a^{-1})$ of slope $\tanh(act)$: $ct_* = \tanh(act)(x_* + a^{-1})$. At $x_* = b$ this gives $ct_*(M) = \tanh(act)(b + a^{-1})$. Now invert the Rindler transformation $x_* = (x + a^{-1})\cosh(act) - a^{-1}$ at this event:
> $$b = (x + a^{-1})\cosh(act) - a^{-1} \quad\Longrightarrow\quad x + a^{-1} = \frac{b + a^{-1}}{\cosh(act)},$$
> hence
> $$x(t) = \frac{b + a^{-1}}{\cosh(act)} - a^{-1}.$$
> At $t = 0$, $x(0) = (b + a^{-1}) - a^{-1} = b$ (consistent: $x = x_*$ at $t = 0$). As $t$ grows, $\cosh(act)$ grows, so $x(t)$ *decreases* toward $-a^{-1}$: $\mathcal{O}$ sees the particle "fall" toward the horizon. The particle reaches $\mathcal{O}$ (at $x = 0$) iff $\cosh(act_0) = 1 + ab$, i.e. iff $b \ge 0$.

**Step 2: Low-velocity limit gives the free-fall parabola $x \simeq b - \tfrac12 g t^2$.**

> [!note]- Derivation
> For $|act|\ll 1$ (early times) and $|ab|\ll 1$ (particle near $\mathcal{O}$), expand $\cosh(act) \approx 1 + \tfrac12(act)^2$:
> $$x(t) = (b + a^{-1})\Big[1 + \tfrac12(act)^2\Big]^{-1} - a^{-1} \approx (b + a^{-1})\Big[1 - \tfrac12(act)^2\Big] - a^{-1} = b - \tfrac12(b + a^{-1})(act)^2.$$
> For $|ab|\ll 1$ the factor $b + a^{-1}\approx a^{-1}$, so
> $$x(t) \approx b - \tfrac12 a^{-1}(act)^2 = b - \tfrac12 a c^2 t^2 = b - \tfrac12 g t^2,$$
> with $g = c^2 a$. This is *exactly* the free-fall trajectory of a body released from height $b$ in a uniform gravitational field of strength $g$ pointing toward $-x$ (downward): $x = b - \tfrac12 g t^2$. The particle, doing nothing but coasting inertially, appears to $\mathcal{O}$ to fall with acceleration $g$ — the **equivalence principle** in its most direct form. The particle's velocity relative to $\mathcal{O}$ is $V = \mathrm{d}x/\mathrm{d}t \approx -g t$, the Newtonian free-fall velocity.

**Step 3: The measured energy $E = mc^2(1+ab)/(1+ax(t))$ is not constant.**

> [!note]- Derivation
> The free particle's four-momentum is $P = m U_{\mathcal{P}}$ with $U_{\mathcal{P}} = e_0^*$ constant (the particle is at rest in $\mathcal{O}_*$). The energy $\mathcal{O}$ assigns at proper time $t$ is
> $$E = P\cdot U(t) = m\,e_0^*\cdot[\cosh(act)e_0^* + \sinh(act)e_1^*] = mc^2\cosh(act),$$
> restoring $c^2$ (the rest energy). From Step 1, $\cosh(act) = (b + a^{-1})/(x + a^{-1}) = (1 + ab)/(1 + ax(t))$, so
> $$E = mc^2\,\frac{1 + ab}{1 + ax(t)}.$$
> This is *not constant*: as the particle falls ($x$ decreases), $1 + ax$ decreases and $E$ *increases*. The energy measured by $\mathcal{O}$ grows as the particle falls — exactly as the kinetic energy of a falling body grows. The reason $E$ is not conserved is that $\mathcal{O}$ is *not inertial*: energy measured by an accelerated observer need not be conserved, because the observer's frame is changing. (For an inertial observer, the free particle's energy *would* be constant.) The spatial momentum $\mathcal{O}$ assigns is $\mathbf{P} = -mc\sinh(act)e_1(t)$, also non-constant.

**Step 4: $E' := E + mgx(t)$ is conserved — total energy in a uniform field.**

> [!note]- Derivation
> Expand $E = mc^2\cosh(act)$ to second order in $act$, using $\cosh(act) \approx 1 + \tfrac12(act)^2$ and the velocity $V \approx -gt$ from Step 2 (so $V^2 \approx g^2 t^2 = a^2 c^4 t^2$, giving $(act)^2 = V^2/c^2$):
> $$E \approx mc^2\Big[1 + \tfrac12(act)^2\Big] = mc^2 + \tfrac12 m(act c)^2\cdot\frac{1}{c^2}\cdots = mc^2 + \tfrac12 m V^2.$$
> More carefully, keeping the position-dependence: from $\cosh(act) = (1+ab)/(1+ax)$,
> $$E = mc^2\frac{1+ab}{1+ax} \approx mc^2(1 + ab)(1 - ax) \approx mc^2[1 + a(b - x)] = mc^2 - mc^2 a(x - b) = mc^2 - mg(x - b),$$
> to first order in $a$ (with $g = c^2 a$). Including the kinetic correction, $E \approx mc^2 + \tfrac12 mV^2 - mg(x - b)$. Therefore
> $$E + mgx \approx mc^2 + \tfrac12 mV^2 + mgb = \mathrm{const},$$
> since $b$ is the (fixed) release position. Defining $E' := E + mgx(t)$, we have $E' = mc^2 + \tfrac12 mV^2 + mgb$, *independent of $t$* — a **constant of motion**. (Exactly: $E' = E + E_{\mathrm{pot}}$ with $E_{\mathrm{pot}} = mgx$, and one checks $E' = mc^2 + b$ in $c=1$ units is conserved from the exact $E = mc^2(1+ab)/(1+ax)$ by direct differentiation.)
>
> The interpretation is the heart of the equivalence principle. $E = mc^2 + \tfrac12 mV^2$ is the kinetic-plus-rest energy; $E_{\mathrm{pot}} = mgx$ is *exactly the potential energy* of a body of mass $m$ at height $x$ in a uniform gravitational field of strength $g$. So $E + mgx$ is the *total mechanical energy* — kinetic plus potential — of a body in uniform gravity, and it is conserved. A free particle in the accelerated frame behaves in every respect like a body falling in a uniform gravitational field, with the proper acceleration $a$ supplying the field strength $g = c^2 a$ and the Rindler coordinate $x$ supplying the height.

> [!note]- Complete formal solution
> The free particle (at rest in $\mathcal{O}_*$ at $x_* = b$) has worldline $x_* = b$; intersecting with $\mathcal{O}$'s rest space $\mathcal{E}_u(t)$ (slope $\tanh(act)$ through $A$) and inverting the Rindler transformation gives $x(t) = (b+a^{-1})/\cosh(act) - a^{-1}$, decreasing toward the horizon — $\mathcal{O}$ sees it "fall". For $|act|,|ab|\ll 1$, $x \simeq b - \tfrac12 gt^2$ ($g = c^2 a$), the free-fall parabola, with $V\simeq -gt$. The energy $\mathcal{O}$ measures is $E = P\cdot U = mc^2\cosh(act) = mc^2(1+ab)/(1+ax(t))$, which grows as the particle falls — not conserved, because $\mathcal{O}$ is non-inertial. But $E \simeq mc^2 + \tfrac12 mV^2 - mg(x-b)$, so $E' := E + mgx = mc^2 + \tfrac12 mV^2 + mgb$ is a constant of motion: exactly the total (kinetic + potential) energy of a body in a uniform gravitational field, with $E_{\mathrm{pot}} = mgx$. The "fall" is a frame artifact — the particle is on a geodesic; $\mathcal{O}$ is the one being accelerated. $\blacksquare$

---

# Key Takeaways

**The "fall" is a frame artifact — the free particle is on a geodesic, and the observer is the one accelerating.** The deepest takeaway, and the embryo of the geodesic principle of general relativity, is that the particle does *nothing*: it coasts inertially on a perfectly straight worldline (a geodesic), and its apparent fall is entirely the appearance of that straight motion in $\mathcal{O}$'s *accelerating* frame. Turned around, this is exactly how general relativity reinterprets gravity: in a gravitational field the freely-falling (geodesic) worldline is the natural, force-free one, and what the static observer $\mathcal{O}$ calls "the force of gravity" is really $\mathcal{O}$ being pushed by their rocket (or by the ground). The trigger to recognise this elsewhere: whenever an accelerated observer reports a "force" acting uniformly on all free bodies, suspect that the bodies are in free fall and the observer is the accelerated one — a uniform "force" that accelerates everything equally (independent of mass) is the signature of a fictitious/gravitational field, by the equivalence of inertial and gravitational mass.

**Position-dependence in the accelerated frame is gravity in disguise — read $x$ as height and $c^2 a$ as $g$.** Every position-dependent quantity in this problem maps onto a gravitational one: the fall $x \simeq b - \tfrac12 g t^2$ is free fall, the energy $E_{\mathrm{pot}} = mgx$ is gravitational potential energy, the field strength is $g = c^2 a$. The reusable shortcut — the [[Special Relativity XVI — Accelerated Observers#Insights|"position-dependence is the fingerprint of gravity"]] trigger — is that whenever a quantity in an accelerated-frame problem carries the Rindler coordinate $x$, you can immediately write its gravitational counterpart by setting $\Phi = c^2 ax = gx$. The diagnostic: if you have computed something that depends on *where* in the accelerated frame it happens, you have computed a gravitational effect, and the fastest route to both the answer and its physical meaning is to translate to the uniform-gravity language.

**Energy measured by an accelerated observer is not conserved, but energy-plus-potential is.** A free particle's energy is conserved for an inertial observer but *not* for $\mathcal{O}$, because $\mathcal{O}$'s frame is changing — $E = mc^2\cosh(act)$ grows as the particle falls. What *is* conserved is the combination $E' = E + mgx$, the energy plus the gravitational potential energy. The reusable principle: in an accelerated (or gravitational) frame, the conserved quantity is not the locally-measured energy but the energy supplemented by the potential, and the conservation comes from the time-translation symmetry of the *stationary* frame (all events on $\mathcal{O}$'s worldline are equivalent). The trigger: when local energy seems not to be conserved in an accelerated frame, look for the potential term $m\Phi = mgx$ that restores conservation — this is the relativistic origin of "gravitational potential energy" and, in general relativity, of the conserved energy associated with a timelike Killing vector. The combination $E + mgx$ being constant is the cleanest single statement of the equivalence principle in this chapter.

This exercise completes the §16.2 trio with [[Ex - Redshift in an accelerated frame and the Einstein elevator]] (the equivalence principle for light) and [[Ex - Clock desynchronization and Rindler rigidity]] (the equivalence principle for clocks). Together they show the accelerated frame reproducing every aspect of a uniform gravitational field — redshift, time dilation, and free fall with a conserved energy.
