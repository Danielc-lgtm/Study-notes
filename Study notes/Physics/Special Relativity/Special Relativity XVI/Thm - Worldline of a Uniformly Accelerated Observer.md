---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Boosts as Hyperbolic Rotations"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathcal{O}$ is a [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] of proper acceleration $a = \|A\|$, four-velocity $U$, four-acceleration $A$, proper time $t$. The reference inertial observer $\mathcal{O}_*$ has orthonormal frame $(e_0^*, e_1^*, e_2^*, e_3^*)$ and inertial coordinates $(ct_*, x_*, y_*, z_*)$, chosen tangent to $\mathcal{O}$ at $t = 0$, so $U(0) = e_0^*$ and $A(0) = a\,e_1^*$. The worldline plane is $\Pi = \mathrm{Span}(e_0^*, e_1^*)$. Components in this frame are written $U^\alpha$, etc. Full registry on [[Special Relativity XVI — Accelerated Observers]].

---

# Statement

> **Theorem (hyperbolic worldline).** A [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] $\mathcal{O}$ of proper acceleration $a$, with reference inertial observer $\mathcal{O}_*$ tangent at $t = 0$, has four-velocity and four-acceleration
> $$
> U(t) = \cosh(act)\,e_0^* + \sinh(act)\,e_1^*, \qquad A(t) = a\big[\sinh(act)\,e_0^* + \cosh(act)\,e_1^*\big],
> $$
> and worldline, in the inertial coordinates of $\mathcal{O}_*$,
> $$
> ct_* = a^{-1}\sinh(act), \quad x_* = a^{-1}\big[\cosh(act) - 1\big], \quad y_* = z_* = 0,
> $$
> which is the branch of an equilateral hyperbola,
> $$
> (ax_* + 1)^2 - (act_*)^2 = 1,
> $$
> with centre $A_{\mathrm{c}} = (ct_*, x_*) = (0, -a^{-1})$ and asymptotes $\Delta_{1,2}: ct_* = \pm(x_* + a^{-1})$.

> **Corollary (motion relative to $\mathcal{O}_*$).** The velocity of $\mathcal{O}$ relative to $\mathcal{O}_*$ is $V = c\,(act_*)/\sqrt{1 + (act_*)^2}$, tending to $\pm c$ as $t_*\to\pm\infty$ but never reaching $c$; the relative (coordinate) acceleration is $\gamma_{\mathrm{coord}} = ac^2/[1 + (act_*)^2]^{3/2}$, which is *not* constant and tends to $0$. The proper acceleration $a$ is the same in every inertial frame.

---

# Motivation

The definition of a uniformly accelerated observer is implicit — it states three conditions ($\|A\| = a$ constant, planar worldline, $\vec\omega = 0$) but does not exhibit the worldline. This theorem makes it explicit, and the explicit form is the workhorse of the entire chapter: every result in §16.1 and §16.2 is read off the hyperbola.

The role of the theorem is to convert a felt acceleration into a trajectory. An observer knows their proper acceleration $a$ — it is what their accelerometer reads — and wants to know where they are, how fast they are going, and how much proper time has elapsed, all as functions of the inertial-frame time $t_*$. The theorem answers all three at once by integrating the defining condition, and the answer is the relativistic replacement for the Newtonian $x = \tfrac12 a t^2$: a hyperbola in place of a parabola, the difference being exactly the requirement that the speed never exceed $c$.

The deeper importance is structural. The worldline being a hyperbola — the curve of constant Lorentzian curvature — is what justifies the names "hyperbolic motion" and "Rindler observer", and the hyperbola's geometry (its asymptotes, its centre, its symmetry under boosts) directly produces the Rindler horizon, the stationarity of the observer, and the exact coincidence of rest spaces with simultaneity hypersurfaces. The theorem is not just a computation; it is the geometric fact from which the chapter's surprises follow.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{O}$ is uniformly accelerated with proper acceleration $a$". The point of input broadening is to recognise the situations that secretly meet it.

The first disguised source is **"a charged particle moves in a uniform electric field"**. The Lorentz four-force $qF\cdot U$ on a charge in a constant field $\mathbf{E}$ produces a four-acceleration of constant norm $a = |q|E/(mc^2)$, confined to the time–field plane, with no rotation — exactly the three conditions. The bridge is the computation of the four-acceleration from the field (Chapter XXI). So any constant-field problem is a hyperbolic-motion problem in disguise. *Example problem:* find the trajectory of an electron entering a parallel-plate capacitor, relativistically.

The second disguised source is **"a rocket maintains constant thrust per unit mass"**. If a rocket's engine is throttled to keep the accelerometer reading fixed at $g$, the rocket is uniformly accelerated with $a = g/c^2$ for the duration of the burn, regardless of how its launch-frame acceleration decays. The bridge is that "constant felt acceleration" *is* "constant proper acceleration". *Example problem:* compute the proper time for a constant-$g$ interstellar voyage ([[Ex - The relativistic rocket and a constant-g voyage]]).

The third disguised source is **"the late-time behaviour of any bounded, eventually-constant acceleration"**. Any worldline whose proper acceleration settles to a constant value $a$ and whose motion is planar and non-rotating is asymptotically a hyperbola, so the theorem's conclusions hold in the limit. The bridge is that the hyperbola is an *attractor* for such motions. *Example problem:* the terminal trajectory of a particle whose thrust ramps up to a steady value.

**Targets (Output Amplification)**

The conclusion is the explicit worldline and its hyperbola.

Combine the conclusion with **the asymptote $\Delta_1$**. The hyperbola hugs the null line $ct_* = x_* + a^{-1}$ without crossing it, and this asymptote, promoted to a hyperplane, is the [[Def - Rindler Horizon|Rindler horizon]] — the boundary of the region the observer can never see. The further result is the existence of a causal horizon in flat spacetime. The combination is nonobvious because the horizon is a feature of the *limit* of the worldline, not of any finite part of it.

Combine the conclusion with **the boost symmetry of the hyperbola**. A time translation $t\to t + t_0$ along the worldline acts on the inertial coordinates as a Lorentz boost of rapidity $act_0$, so all events on the hyperbola are equivalent. The further result is that the observer is *stationary*: their local physics is time-independent, and any instantaneous computation may be done at $t = 0$. The combination is the engine of the chapter's labour-saving, used to transport every instantaneous result along the worldline.

Combine the conclusion with **the proper-time relation $act = \sinh^{-1}(act_*)$**. The proper time $t$ grows only logarithmically with the inertial time $t_*$ at late times, so the observer ages ever more slowly relative to $\mathcal{O}_*$. The further result is the twin-paradox-like asymmetry of a constant-$g$ voyage: the traveller's clock runs slow without bound. The combination is useful because it quantifies exactly how much proper time a long acceleration costs.

---

# Why Is It True

The deep reason is that **a boost is a hyperbolic rotation, and uniform acceleration sweeps a fixed amount of hyperbolic angle per unit proper time** — exactly as uniform circular motion sweeps a fixed angle per unit arc length.

Picture the Euclidean analogue first. A point moving on a circle of radius $r$ at unit speed has position $(r\cos\theta, r\sin\theta)$ with $\theta$ the arc length divided by $r$; its velocity $(-\sin\theta, \cos\theta)$ rotates at a constant rate, and the (centripetal) acceleration has constant magnitude $1/r$. "Constant curvature $1/r$" is what makes the curve a circle, and the trigonometric functions are the bookkeeping that keeps the point on the circle while the velocity rotates.

Now the Minkowski version. The four-velocity $U$ is a unit timelike vector, so it lives on the hyperboloid $U\cdot U = 1$ — the Lorentzian "unit circle". Constant proper acceleration means $U$ moves along this hyperboloid at a constant rate, sweeping a fixed amount of *hyperbolic* angle (rapidity) per unit proper time. The motion of a unit vector on the hyperboloid at constant rate is parametrised by hyperbolic functions, $U = \cosh(\psi)e_0^* + \sinh(\psi)e_1^*$ with $\psi$ proportional to proper time — this is the boost, the hyperbolic rotation. Integrating $U$ to get the position introduces a second pair of hyperbolic functions, and $\cosh^2 - \sinh^2 = 1$ forces the position onto the hyperbola, just as $\cos^2 + \sin^2 = 1$ forces the circular point onto the circle.

**The whole theorem is "uniform circular motion with the metric sign flipped": the proper acceleration is the curvature, the proper time is the hyperbolic arc length, the rapidity $\psi = act$ is the hyperbolic angle, and the velocity rotates hyperbolically — which is why it asymptotes to $c$ (rapidity infinity) instead of wrapping around.** The single difference from the circle is that the hyperbola is unbounded: the hyperbolic angle runs over all of $\mathbb{R}$, the velocity climbs toward but never reaches $c$, and the curve flies off along its asymptotes instead of closing up. Every feature of hyperbolic motion is the circular feature read through the sign flip.

---

# What Makes This Hard

The integration itself is short; the place people stumble is the orthogonality bookkeeping. The four-acceleration must continuously reorient to stay orthogonal to the turning four-velocity, and it is easy to forget this and write a constant $A$ — which (as the definition's motivation shows) forces $A = 0$. The non-obvious step is recognising that the *norm* condition $\|A\| = a$, combined with $A\cdot U = 0$ and $U\cdot U = 1$, determines the components up to a sign that is fixed by continuity. The most common error is a sign slip in the hyperbolic identities (writing $\cosh^2 + \sinh^2$ instead of $\cosh^2 - \sinh^2$), which destroys the hyperbola; and conflating the constant proper acceleration $a$ with the coordinate acceleration $d^2x_*/dt_*^2$, which is *not* constant.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write $U$ and $A$ in components in the plane $\Pi = \mathrm{Span}(e_0^*, e_1^*)$, impose $U\cdot U = 1$, $A\cdot U = 0$, $\|A\| = a$, and $A = c^{-1}dU/dt$. These reduce to a single first-order ordinary differential equation for the spatial velocity component, with hyperbolic-function solution; integrate once more for the position.

**Subgoal decomposition:**

1. **Set up the constraints in the plane.** Write $U(t) = u^0 e_0^* + u^1 e_1^*$ (the $y, z$ components vanish since the motion is planar). Impose $U\cdot U = (u^0)^2 - (u^1)^2 = 1$ and $A\cdot A = -(a^0)^2 + (a^1)^2 = -a^2$ where $A = a^0 e_0^* + a^1 e_1^*$, $a^\alpha = c^{-1}du^\alpha/dt$.
   - *Hint:* Mostly-minus: timelike $U$ has $(u^0)^2 - (u^1)^2 = 1$; spacelike $A$ has $\|A\|^2 = (a^1)^2 - (a^0)^2 = a^2$.
   - *Why needed:* These are the algebraic constraints the dynamics must respect at every instant.

2. **Derive the velocity equation.** From $(u^0)^2 = 1 + (u^1)^2$ and the norm condition, obtain $c^{-1}du^1/dt = ca\sqrt{1 + (u^1)^2}/\sqrt{1+(u^1)^2}$... more directly: differentiating $(u^0)^2 - (u^1)^2 = 1$ gives $u^0 a^0 = u^1 a^1$, and combining with $(a^1)^2 - (a^0)^2 = a^2$ yields $\frac{1}{\sqrt{1+(u^1)^2}}\frac{du^1}{dt} = ca$.
   - *Hint:* Use $a^0 = (u^1/u^0)a^1$ to eliminate $a^0$ from the norm condition.
   - *Why needed:* This is the single ODE whose solution is the velocity.

3. **Integrate to the four-velocity.** With $u^1(0) = 0$ (tangent at $t=0$), integrate $du^1/\sqrt{1+(u^1)^2} = ca\,dt$ to get $u^1(t) = \sinh(act)$, hence $u^0(t) = \cosh(act)$.
   - *Hint:* $\int du/\sqrt{1+u^2} = \sinh^{-1}u$.
   - *Why needed:* This is the four-velocity; $A$ follows by differentiation.

4. **Integrate to the worldline and identify the hyperbola.** Integrate $dX_*^0/dt = c\cosh(act)$, $dX_*^1/dt = c\sinh(act)$ with $X_*^\alpha(0) = 0$ to get $ct_* = a^{-1}\sinh(act)$, $x_* = a^{-1}[\cosh(act)-1]$; eliminate $t$ via $\cosh^2 - \sinh^2 = 1$.
   - *Hint:* $(ax_* + 1) = \cosh(act)$ and $act_* = \sinh(act)$, so $(ax_*+1)^2 - (act_*)^2 = 1$.
   - *Why needed:* This exhibits the worldline as a hyperbola and identifies its centre and asymptotes.

---

# Lemma Decomposition

> [!note]- Lemma 1: The four-velocity is a hyperbolic rotation of $e_0^*$
> **Statement:** With $U(0) = e_0^*$ and constant proper acceleration $a$, the four-velocity is $U(t) = \cosh(act)e_0^* + \sinh(act)e_1^*$.
>
> **Hint:** Reduce the constraints to $\frac{1}{\sqrt{1+(u^1)^2}}\frac{du^1}{dt} = ca$ and integrate.
>
> **Why needed:** It is the core of the theorem; the worldline and four-acceleration both follow from it.
>
> > [!note]- Full proof
> > Write $U = u^0 e_0^* + u^1 e_1^*$ (planar motion, so transverse components vanish). The normalisation $U\cdot U = 1$ reads $(u^0)^2 - (u^1)^2 = 1$, so $u^0 = \sqrt{1 + (u^1)^2}$ (taking $u^0 > 0$, future-directed). The four-acceleration is $A = c^{-1}dU/dt = c^{-1}(\dot u^0 e_0^* + \dot u^1 e_1^*)$ (overdot $= d/dt$). Differentiating the normalisation: $u^0\dot u^0 = u^1\dot u^1$, hence $\dot u^0 = (u^1/u^0)\dot u^1$. The proper-acceleration condition $\|A\|^2 = a^2$ reads $c^{-2}[(\dot u^1)^2 - (\dot u^0)^2] = a^2$, i.e. $(\dot u^1)^2 - (\dot u^0)^2 = c^2 a^2$. Substituting $\dot u^0 = (u^1/u^0)\dot u^1$:
> > $$(\dot u^1)^2\left[1 - \frac{(u^1)^2}{(u^0)^2}\right] = (\dot u^1)^2\,\frac{(u^0)^2 - (u^1)^2}{(u^0)^2} = \frac{(\dot u^1)^2}{(u^0)^2} = c^2 a^2,$$
> > using $(u^0)^2 - (u^1)^2 = 1$. Hence $\dot u^1 = c a\,u^0 = ca\sqrt{1 + (u^1)^2}$ (the $+$ sign fixed by $\dot u^1(0) = ca > 0$, since $A(0) = a e_1^*$). This separates:
> > $$\frac{du^1}{\sqrt{1 + (u^1)^2}} = ca\,dt \ \Longrightarrow\ \sinh^{-1}(u^1) = act,$$
> > using $u^1(0) = 0$. Therefore $u^1(t) = \sinh(act)$ and $u^0(t) = \sqrt{1 + \sinh^2(act)} = \cosh(act)$. $\blacksquare$

> [!note]- Lemma 2: The worldline is the hyperbola $(ax_*+1)^2 - (act_*)^2 = 1$
> **Statement:** Integrating the four-velocity with $O(0)$ at the origin gives $ct_* = a^{-1}\sinh(act)$, $x_* = a^{-1}[\cosh(act)-1]$, satisfying $(ax_*+1)^2 - (act_*)^2 = 1$.
>
> **Hint:** The inertial coordinates of $O(t)$ have $dX_*^\alpha/dt = c\,u^\alpha$; integrate and use $\cosh^2-\sinh^2=1$.
>
> **Why needed:** It exhibits the trajectory as a hyperbola and locates its centre and asymptotes — the geometry the rest of the chapter uses.
>
> > [!note]- Full proof
> > The inertial coordinates $X_*^\alpha(t)$ of the event $O(t)$ satisfy $dX_*^\alpha/dt = c\,u^\alpha(t)$ (the four-velocity is the unit tangent, $U^\alpha = c^{-1}dX_*^\alpha/dt$). Thus
> > $$\frac{d(ct_*)}{dt} = c\cosh(act), \qquad \frac{dx_*}{dt} = c\sinh(act).$$
> > Integrating with $X_*^\alpha(0) = 0$:
> > $$ct_* = \frac{c}{ac}\sinh(act) = a^{-1}\sinh(act), \qquad x_* = a^{-1}[\cosh(act) - 1].$$
> > Then $ax_* + 1 = \cosh(act)$ and $act_* = \sinh(act)$, so
> > $$(ax_* + 1)^2 - (act_*)^2 = \cosh^2(act) - \sinh^2(act) = 1.$$
> > This is an equilateral hyperbola in $(ct_*, x_*)$ centred at $(0, -a^{-1})$ (the point where $ax_*+1 = 0$ and $ct_* = 0$), with asymptotes $ax_* + 1 = \pm act_*$, i.e. $ct_* = \pm(x_* + a^{-1})$. $\blacksquare$

> [!note]- Lemma 3: The relative velocity tends to $c$ but the coordinate acceleration tends to $0$
> **Statement:** $V = c\,(act_*)/\sqrt{1 + (act_*)^2}\to\pm c$ and $\gamma_{\mathrm{coord}} = ac^2/[1+(act_*)^2]^{3/2}\to 0$ as $t_*\to\pm\infty$.
>
> **Hint:** Differentiate $x_*(t_*) = a^{-1}[\sqrt{1+(act_*)^2} - 1]$ once and twice with respect to $t_*$.
>
> **Why needed:** It shows the proper acceleration is constant while the coordinate acceleration is not — the distinction that the warning callouts insist on.
>
> > [!note]- Full proof
> > Eliminating $t$ from Lemma 2: $ct_* = a^{-1}\sinh(act)$ gives $\cosh(act) = \sqrt{1 + (act_*)^2}$, so $x_*(t_*) = a^{-1}[\sqrt{1 + (act_*)^2} - 1]$. Then
> > $$V = \frac{dx_*}{dt_*} = a^{-1}\cdot\frac{a^2 c^2 t_*}{\sqrt{1 + (act_*)^2}} = \frac{ac^2 t_*}{\sqrt{1+(act_*)^2}} = c\,\frac{act_*}{\sqrt{1+(act_*)^2}},$$
> > which $\to\pm c$ as $t_*\to\pm\infty$ (the argument of the square root dominates), never reaching $c$. Differentiating again,
> > $$\gamma_{\mathrm{coord}} = \frac{d^2 x_*}{dt_*^2} = \frac{ac^2}{[1 + (act_*)^2]^{3/2}},$$
> > which equals $ac^2$ at $t_* = 0$ but $\to 0$ as $t_*\to\pm\infty$. So the coordinate acceleration is not constant, even though the proper acceleration $a$ is. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Choose the reference inertial observer $\mathcal{O}_*$ tangent to $\mathcal{O}$ at $t = 0$, so $U(0) = e_0^*$ and (by the definition, up to the sign fixed by orienting $e_1^*$) $A(0) = a\,e_1^*$. Since the worldline is planar, $U$ and $A$ lie in $\Pi = \mathrm{Span}(e_0^*, e_1^*)$ for all $t$.
>
> By **Lemma 1**, the constraints $U\cdot U = 1$, $A\cdot U = 0$, $\|A\| = a$, and $A = c^{-1}dU/dt$ integrate (with $U(0) = e_0^*$) to
> $$U(t) = \cosh(act)\,e_0^* + \sinh(act)\,e_1^*.$$
> Differentiating, $A(t) = c^{-1}dU/dt = a[\sinh(act)e_0^* + \cosh(act)e_1^*]$. One checks $A\cdot U = a[\sinh\cosh - \cosh\sinh] = 0$, $U\cdot U = \cosh^2 - \sinh^2 = 1$, and $A\cdot A = a^2[\sinh^2 - \cosh^2] = -a^2$, so $\|A\| = a$ — all three conditions hold.
>
> By **Lemma 2**, integrating $dX_*^\alpha/dt = c\,U^\alpha$ with $O(0)$ at the origin gives the worldline
> $$ct_* = a^{-1}\sinh(act), \quad x_* = a^{-1}[\cosh(act)-1], \quad y_* = z_* = 0,$$
> which satisfies $(ax_* + 1)^2 - (act_*)^2 = 1$ — an equilateral hyperbola of centre $(0, -a^{-1})$ and asymptotes $ct_* = \pm(x_* + a^{-1})$.
>
> By **Lemma 3**, the relative velocity is $V = c(act_*)/\sqrt{1+(act_*)^2}\to\pm c$ and the coordinate acceleration is $\gamma_{\mathrm{coord}} = ac^2/[1+(act_*)^2]^{3/2}\to 0$, while the proper acceleration $a = \|A\|$ is a Lorentz scalar, the same in every inertial frame. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Catenary and the constant-tension cable (classical mechanics).** The hyperbolic-function solution of a constant-proper-acceleration worldline is structurally identical to the catenary $y = a^{-1}\cosh(ax)$ of a hanging chain, where the "constant" being maintained is the horizontal tension. Both arise from a first-order condition that a fixed quantity (tension; proper acceleration) be maintained, integrated through a $\cosh$. Recognising the shared structure clarifies why hyperbolic functions, not parabolas, are the natural solutions when a *rate* rather than a *force* is held fixed.

**The pseudosphere and surfaces of constant curvature (differential geometry).** The worldline of constant proper acceleration is the timelike curve of constant first curvature; its spacelike analogue, swept out as the acceleration direction is rotated, is a surface of constant curvature, and the velocity hyperboloid on which the four-velocity moves is a model of hyperbolic space. Computing the geodesics and the holonomy on this hyperboloid is the same calculation that gives Thomas precession ([[Def - Thomas Precession]]); the application is nonobvious because a kinematics problem turns out to be a problem in the geometry of $\mathbb{H}^3$.

**Rapidity as a clock for exponential growth (applied mathematics).** Since the rapidity is $\psi = act$ and the energy grows as $\cosh(act)$, a constant-proper-acceleration trajectory is an *exponential* process in disguise: at late times $\cosh(act)\sim\tfrac12 e^{act}$, so the observer's energy, Lorentz factor, and distance all grow exponentially in proper time. This is the same exponential-in-proper-time structure that appears in the Unruh temperature and in inflationary cosmology, where a constant "acceleration" (Hubble rate) drives exponential expansion; the application battle-tests the recognition that "constant proper acceleration" means "exponential in proper time".

---

# Bridges

- **[[Def - Boosts as Hyperbolic Rotations]]** — the four-velocity $U(t) = \cosh(act)e_0^* + \sinh(act)e_1^*$ is literally a one-parameter family of boosts applied to $e_0^*$, with rapidity $\psi = act$ growing linearly in proper time. Uniform acceleration is "uniform rapidity-rate": the boost parameter advances at a constant rate, which is the cleanest possible statement of the motion. The hyperbola is the orbit of $e_0^*$ under the boost subgroup.

- **[[Def - Rindler Horizon]]** — the asymptotes $\Delta_{1,2}$ of the hyperbola produced by this theorem are exactly the Rindler horizon: the worldline approaches $\Delta_1$ without reaching it, so light from beyond $\Delta_1$ never catches the observer. The horizon is a feature of the hyperbola's asymptotic geometry, inseparable from this theorem.

- **[[Thm - Inertial Worldlines Maximise Proper Time]]** — this theorem is the natural foil: an inertial worldline is straight and maximises proper time between two events, whereas the uniformly accelerated worldline is a hyperbola and a *bent* path, accumulating less proper time. The constant-$g$ voyage's twin-paradox asymmetry is the proper-time deficit of the hyperbola relative to the straight line.

- **[[Def - Curvature and Torsions of a Worldline]]** — the proper acceleration $a$ is the *first curvature* of the worldline in the Serret–Frenet sense, and "uniformly accelerated" is "constant first curvature, zero torsions". The hyperbola is the Lorentzian analogue of the circle (the Euclidean curve of constant curvature), with $a^{-1}$ the radius of the osculating hyperbola.

---

# Unlocked by This

> [!tip] The Length Scale of Acceleration and the Unruh Temperature *(from quantum field theory)*
> The centre of the hyperbola sits a distance $a^{-1}$ behind the observer, and this length scale governs everything: the horizon, the redshift, the maximal rigid extent. The same $a$ sets the **Unruh temperature** $T = \hbar a/(2\pi c k_B)$ a uniformly accelerated detector registers in the Minkowski vacuum. That a purely classical kinematic quantity — the curvature of a worldline — fixes a quantum temperature is among the deepest results connecting acceleration, horizons, and thermodynamics, and the hyperbolic worldline of this theorem is the trajectory along which it is derived.

> [!tip] Eternal Acceleration and the Rindler Wedge *(from the study of horizons)*
> The full family of hyperbolae with a common pair of asymptotes fills the **Rindler wedge** $x_* > |ct_*|$, a quarter of Minkowski space. The wedge is the largest region that any uniformly accelerated observer can causally access, and its boundary is the horizon. This decomposition of Minkowski space into the wedge and its hidden complement is the flat-spacetime model of the exterior and interior of a black hole, and the hyperbolae are the worldlines of static observers hovering outside the hole.
