---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Rindler Coordinates and the Accelerated Frame"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector $X$ has $X\cdot X > 0$. $\mathcal{O}$ is the fiducial [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] of proper acceleration $a$, proper time $t$, carrying [[Def - Rindler Coordinates and the Accelerated Frame|Rindler coordinates]] $(ct, x, y, z)$. A second observer $\mathcal{O}'$ is **comoving** with $\mathcal{O}$ — fixed at constant Rindler coordinate $(x, y, z) = (x_0, y_0, z_0)$ — with proper time $t'$ and proper acceleration $a'$. $\Gamma$ is the Lorentz factor of $\mathcal{O}'$ relative to $\mathcal{O}$ at the events that are simultaneous for both. The reference inertial observer $\mathcal{O}_*$ has frame $(e_0^*, e_1^*, e_2^*, e_3^*)$ and inertial coordinates $(ct_*, x_*, y_*, z_*)$; $A = (0, -a^{-1})$ is the centre of $\mathcal{O}$'s hyperbola. Full registry on [[Special Relativity XVI — Accelerated Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (§12.4.1–12.4.2) uses mostly-plus; his $\Gamma = \mathrm{d}t/\mathrm{d}t'$ and the relations $t' = (1+ax_0)t$, $a' = a/(1+ax_0)$ are scalar and unchanged by the signature flip. Only intermediate scalar products (e.g. $\vec a(t)\cdot\overrightarrow{O(t)O'(t')} = ax_0$) carry a sign; the final formulas transcribed here are signature-independent.

---

# Statement

> **Theorem (comoving observers and clock desynchronization).** Let $\mathcal{O}$ be a uniformly accelerated observer of proper acceleration $a$, and let $\mathcal{O}'$ be an observer fixed at constant Rindler coordinate $(x_0, y_0, z_0)$ relative to $\mathcal{O}$. Then:
> 1. $\mathcal{O}'$ is *itself* a uniformly accelerated observer, with proper acceleration
> $$a' = \frac{a}{1 + ax_0}.$$
> 2. The rest spaces of $\mathcal{O}$ and $\mathcal{O}'$ coincide at simultaneous events, $\mathcal{E}_{u'}(t') = \mathcal{E}_u(t)$, and the Lorentz factor of $\mathcal{O}'$ relative to $\mathcal{O}$ is $\Gamma = (1 + ax_0)^{-1}$.
> 3. The proper times of $\mathcal{O}'$ and $\mathcal{O}$ are related by
> $$\mathrm{d}t' = (1 + ax_0)\,\mathrm{d}t, \qquad t' = (1 + ax_0)\,t,$$
> the integration constant fixed so that $t' = 0$ when $t = 0$.

> **Corollary (desynchronization and the rigidity hierarchy).** Two ideal clocks fixed in the accelerated frame at different positions $x_0 \neq 0$ and synchronized at $t = 0$ *desynchronize* for $t > 0$: their proper times $t' = (1+ax_0)t$ differ. The proper acceleration of comoving observers satisfies $a' \le a$ when $x_0 \ge 0$ and $a' \to +\infty$ as $x_0 \to -a^{-1}$ (the Rindler horizon); the bottom of an accelerated rigid body must accelerate harder than the top. All comoving observers share the *same* [[Def - Rindler Horizon|Rindler horizon]].

---

# Motivation

An inertial observer can build a global clock network. Lay out identical clocks at rest throughout the frame, synchronize them once with light signals, and they stay synchronized forever: every clock ticks at the same rate, and "the time now" is a well-defined global quantity. This is so basic to Newtonian and inertial-relativistic physics that one rarely notices it is a theorem rather than an axiom. The question this result answers is what happens to that clock network when the frame accelerates — and the answer is that it falls apart.

The theorem isolates the single deepest difference between an accelerated frame and an inertial one. It is not that clocks run slow (that already happens for moving inertial clocks) but that two clocks *at rest with respect to each other* in the accelerated frame, started together, *drift apart in their readings*. There is no consistent global time in an accelerated frame, and this result quantifies exactly how the inconsistency grows: linearly in $t$, with the rate set by the position-dependent factor $1 + ax_0$.

The role of the theorem in the chapter is to convert the abstract Rindler metric into operational physics. The metric component $g_{tt} = (1 + ax)^2$ says a static clock ticks at rate $\mathrm{d}\tau = (1 + ax)\,\mathrm{d}t$; this theorem reads that off as a desynchronization, derives the position-dependent proper acceleration $a' = a/(1+ax_0)$ that a comoving clock actually feels, and sets up everything in §16.2 that follows — the spectral shift (light exchanged between desynchronized clocks), the rigid ruler (a one-parameter family of comoving observers), and the equivalence-principle reading (the desynchronization *is* gravitational time dilation). It is the statement that an accelerated "rocket" is a genuinely different kind of object from an inertial one, with a built-in front-to-back asymmetry.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{O}'$ is fixed in $\mathcal{O}$'s accelerated frame, i.e. at constant Rindler coordinate". The point of input broadening is to recognise the situations that secretly supply this.

The first disguised source is **"two observers maintain a fixed proper distance from each other while accelerating"**. If two observers want the distance between them — measured in their common rest space — to stay constant, then each sits at a fixed Rindler coordinate of the other, which is exactly the precondition. The bridge is the [[Def - Rindler Coordinates and the Accelerated Frame|rigid ruler]] result $\ell_0 = |x_0|$: constant proper separation means constant $x_0$. So any problem about a *rigid* accelerating body — a rocket of finite length, a Born-rigid ruler — is a comoving-observer problem, with each material point a separate $\mathcal{O}'$. *Example problem:* find the acceleration the tail of a rigid rocket must have if the nose accelerates at $g$.

The second disguised source is **"an observer hovers at fixed altitude in a uniform gravitational field"**. By the equivalence principle a static observer in a uniform field of strength $g = c^2 a$ is, locally, a comoving observer in an accelerated frame, with the altitude playing the role of $x_0$. The bridge is the identification $\Phi = c^2 ax_0 = gx_0$ of the Rindler "potential" with the gravitational potential. So any problem about clocks at different heights in a (locally uniform) gravitational field routes through this theorem. *Example problem:* compare the rates of two clocks at heights differing by $h$ in gravity $g$ — the result $\mathrm{d}t'/\mathrm{d}t = 1 + gh/c^2$ is the gravitational time dilation.

The third disguised source is **"a second uniformly accelerated worldline shares the asymptotes of the first"**. Two hyperbolae in the same plane with the same centre $A = (0, -a^{-1})$ and the same asymptotes are precisely the worldlines of two comoving observers (they differ only in their constant $x_0$). The bridge is that constant-$x_0$ curves are the iso-coordinate lines of the Rindler chart, which are confocal hyperbolae. So recognising "same asymptotes" lets one apply the theorem without ever mentioning Rindler coordinates. *Example problem:* show that two accelerating rockets with a common Rindler horizon keep a fixed proper separation only if their proper accelerations differ by exactly $a' = a/(1+ax_0)$.

**Targets (Output Amplification)**

The conclusions are $a' = a/(1+ax_0)$, $t' = (1+ax_0)t$, and $\mathcal{E}_{u'} = \mathcal{E}_u$.

Combine the proper-time relation with **a second comoving observer at a different position**. Two comoving clocks at $x_1$ and $x_2$ have proper-time rates in the ratio $(1+ax_1)/(1+ax_2)$, so a definite phase difference accumulates: after $\mathcal{O}$'s proper time $t$, clock $1$ reads $(1+ax_1)t$ and clock $2$ reads $(1+ax_2)t$. The further result is the gravitational/Rindler clock comparison used in the GPS-style problem and in the [[Thm - Spectral Shift in an Accelerated Frame|spectral-shift]] derivation. The combination is nonobvious because each clock is, individually, a perfectly good uniformly accelerated observer with its own constant proper acceleration; the drift appears only when their *readings* are compared.

Combine $a' = a/(1+ax_0)$ with **the demand of a finite rigid body extending toward the horizon**. As $x_0 \to -a^{-1}$ the required proper acceleration $a'$ diverges, so no material point can be held rigidly at the horizon: a Born-rigid body can extend at most a distance $a^{-1}$ behind its leading edge. The further result is the maximal rigid extent and the resolution of [[Ex - Clock desynchronization and Rindler rigidity|Bell's spaceship paradox]] — identical accelerations (not the position-dependent $a'$) snap a connecting string. The combination is useful because it converts a kinematic formula into a hard physical limit on rigid structures.

Combine $\mathcal{E}_{u'} = \mathcal{E}_u$ with **the exact rest-space–simultaneity identity for uniform acceleration**. Because every comoving observer is uniformly accelerated, each has $\Sigma_{u'}(t') = \mathcal{E}_{u'}(t')$ exactly, and these all coincide with $\mathcal{O}$'s slices. The further result is that the whole comoving family shares one consistent (if position-dependently-paced) simultaneity foliation of the Rindler wedge — the foliation by straight lines through $A$. The combination is nonobvious because for a *generic* accelerated family the rest spaces would not agree, and the clean Rindler chart would not exist.

---

# Why Is It True

The deep reason is that **a clock fixed at Rindler position $x$ sits on a hyperbola of smaller "radius" the closer it is to the centre $A$, and a smaller hyperbola is traversed faster in proper time per unit of the shared angular parameter $act$.**

Picture the Rindler diagram: the centre $A = (0, -a^{-1})$, the fiducial observer $\mathcal{O}$ on the hyperbola through $x = 0$, and a comoving observer $\mathcal{O}'$ on the confocal hyperbola through $x = x_0$. The straight lines through $A$ of slope $\tanh(act)$ are the common rest spaces: a single such line cuts $\mathcal{O}$ at proper time $t$ and $\mathcal{O}'$ at proper time $t'$, and these are the *simultaneous* events. The geometry is a fan of lines pivoting about $A$, and as the fan sweeps from slope $0$ upward, it carries both observers forward — but it carries the *nearer* observer (smaller $|x_0 + a^{-1}|$, i.e. closer to $A$) through more proper time, because that observer is on a tighter hyperbola and so moves faster along it.

Quantitatively, the hyperbola through $x_0$ has centre-distance $x_0 + a^{-1} = a'^{-1}$, so its proper acceleration is $a' = (x_0 + a^{-1})^{-1} = a/(1 + ax_0)$. This is the whole of part 1: *the proper acceleration of a comoving observer is the reciprocal of its distance from the common centre $A$*, exactly as the curvature of a circle is the reciprocal of its radius. The observer nearer the horizon (smaller distance to $A$) is on a more sharply curved hyperbola and feels a larger acceleration; the observer farther out feels less. The proper-time relation follows by the same scaling: along a hyperbola of centre-distance $r$, the proper time accumulated per unit of the shared rapidity-parameter $act$ is proportional to $r$, giving $t'/t = (x_0 + a^{-1})/a^{-1} = 1 + ax_0$.

**The one-line mechanism: a comoving clock's rate and felt acceleration are both fixed by its distance $x_0 + a^{-1}$ from the common centre $A$ — farther out means slower ticking and gentler acceleration, nearer the horizon means faster ticking and fiercer acceleration, and the proportionality constant is the same factor $1 + ax_0$.** The desynchronization is then automatic: two clocks at different distances from $A$ accumulate proper time at different rates, so once started together they cannot stay together. There is nothing to "fix" — it is the unavoidable price of the rest spaces pivoting about $A$ rather than translating.

---

# What Makes This Hard

The computation is short; the place people stumble is conceptual — believing that $\mathcal{O}'$, which is *at rest with respect to* $\mathcal{O}$, can nonetheless have a *different* proper acceleration and a *different* clock rate. The non-obvious step is that "at rest with respect to" in an accelerated frame does not mean "physically equivalent": the two observers occupy different hyperbolae, and their distance to the common centre $A$ is what breaks the symmetry. The most common error is to assume, by analogy with inertial frames, that comoving clocks stay synchronized (they do not, unless $x_0 = 0$), or to forget the sign of $x_0$ and conclude that the leading rather than the trailing edge of a rigid body accelerates harder.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the worldline of the comoving observer $\mathcal{O}'$ by substituting $x = x_0$ into the Rindler-to-inertial transformation; recognise the result as another hyperbola; read off its proper acceleration from its centre-distance; then compute its proper time by integrating the line element along the constant-$x_0$ worldline.

**Subgoal decomposition:**

1. **Write $\mathcal{O}'$'s worldline in inertial coordinates.** Set $x = x_0$ in $ct_* = (x + a^{-1})\sinh(act)$, $x_* = (x + a^{-1})\cosh(act) - a^{-1}$.
   - *Hint:* This is the constant-$x$ iso-coordinate line of the Rindler chart.
   - *Why needed:* It exhibits $\mathcal{O}'$ as an explicit curve whose nature can be identified.

2. **Identify the curve as a hyperbola and read its proper acceleration.** Eliminate $t$ via $\cosh^2 - \sinh^2 = 1$ to get $(a'x_*' + 1)^2 - (a'ct_*)^2 = 1$ in shifted coordinates, with $a'^{-1} = x_0 + a^{-1}$.
   - *Hint:* The centre-distance of the new hyperbola is $x_0 + a^{-1}$; its proper acceleration is the reciprocal.
   - *Why needed:* It gives part 1, $a' = a/(1+ax_0)$.

3. **Compute the proper time along the constant-$x_0$ worldline.** Differentiate the worldline with respect to $t$, form $\mathrm{d}s^2 = c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2$, and take the square root.
   - *Hint:* $c\,\mathrm{d}t' = \sqrt{c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2} = |1 + ax_0|\,c\,\mathrm{d}t$ since $\cosh^2 - \sinh^2 = 1$.
   - *Why needed:* It gives part 3, $\mathrm{d}t' = (1+ax_0)\mathrm{d}t$, and the desynchronization corollary.

4. **Verify the common rest space.** Show the four-velocities of $\mathcal{O}$ and $\mathcal{O}'$ at simultaneous events are equal, so their orthogonal hyperplanes coincide; deduce $\Gamma = (1+ax_0)^{-1}$.
   - *Hint:* Two proportional unit future timelike vectors are equal, and $\Gamma = \mathrm{d}t/\mathrm{d}t'$.
   - *Why needed:* It gives part 2 and the Lorentz factor.

---

# Lemma Decomposition

> [!note]- Lemma 1: A comoving observer is uniformly accelerated with $a' = a/(1+ax_0)$
> **Statement:** Setting $x = x_0 = \mathrm{const}$ in the Rindler transformation gives a hyperbola of centre-distance $x_0 + a^{-1}$ and proper acceleration $a' = a/(1+ax_0)$.
>
> **Hint:** The constant-$x$ curve is confocal with $\mathcal{O}$'s hyperbola; its proper acceleration is the reciprocal of its distance to the common centre $A$.
>
> **Why needed:** It establishes part 1 and lets every §16.1 result be re-applied to $\mathcal{O}'$ with $a \to a'$.
>
> > [!note]- Full proof
> > The worldline of $\mathcal{O}'$ in the inertial coordinates of $\mathcal{O}_*$ is obtained by fixing $x = x_0$, $y = y_0$, $z = z_0$ in the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler transformation]]:
> > $$ct_* = (x_0 + a^{-1})\sinh(act), \quad x_* = (x_0 + a^{-1})\cosh(act) - a^{-1}, \quad y_* = y_0, \ z_* = z_0.$$
> > Introduce the shifted inertial coordinate $x_*' := x_* - x_0$ and set $a' := a/(1 + ax_0)$, so that $x_0 + a^{-1} = a'^{-1}$ and $x_* + a^{-1} = x_*' + x_0 + a^{-1} = x_*' + a'^{-1}$. Then $a'x_*' + 1 = a'(x_* + a^{-1}) = a'(x_0 + a^{-1})\cosh(act) = \cosh(act)$ and $a'ct_* = a'(x_0 + a^{-1})\sinh(act) = \sinh(act)$, whence
> > $$(a'x_*' + 1)^2 - (a'ct_*)^2 = \cosh^2(act) - \sinh^2(act) = 1.$$
> > This is the equation of a uniformly accelerated worldline of proper acceleration $a'$ (the same form as [[Thm - Worldline of a Uniformly Accelerated Observer|$\mathcal{O}$'s hyperbola]], with $a\to a'$ and shifted spatial origin). Hence $\mathcal{O}'$ is uniformly accelerated with $a' = a/(1+ax_0)$. $\blacksquare$

> [!note]- Lemma 2: The proper time of $\mathcal{O}'$ is $t' = (1+ax_0)t$
> **Statement:** Along $\mathcal{O}'$'s worldline, $c\,\mathrm{d}t' = (1 + ax_0)\,c\,\mathrm{d}t$, integrating to $t' = (1+ax_0)t$.
>
> **Hint:** Differentiate the worldline and form the line element; $\cosh^2 - \sinh^2 = 1$ collapses the radical.
>
> **Why needed:** It is the proper-time relation and the source of clock desynchronization.
>
> > [!note]- Full proof
> > Differentiating the worldline of Lemma 1 with respect to $t$ (at fixed $x_0, y_0, z_0$):
> > $$\frac{\mathrm{d}(ct_*)}{\mathrm{d}t} = (x_0 + a^{-1})\,ac\cosh(act), \qquad \frac{\mathrm{d}x_*}{\mathrm{d}t} = (x_0 + a^{-1})\,ac\sinh(act),$$
> > with $\mathrm{d}y_* = \mathrm{d}z_* = 0$. The proper time of $\mathcal{O}'$ between two events on its worldline is the integrated [[Def - Proper Time|interval]] $\int\sqrt{\mathrm{d}s^2}$ with $\mathrm{d}s^2 = c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2$. Hence
> > $$c\,\mathrm{d}t' = \sqrt{c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2} = (x_0 + a^{-1})\,ac\,\sqrt{\cosh^2(act) - \sinh^2(act)}\;\mathrm{d}t = (1 + ax_0)\,c\,\mathrm{d}t,$$
> > using $x_0 + a^{-1} = (1+ax_0)/a$ and $\cosh^2 - \sinh^2 = 1$ (and $1 + ax_0 > 0$ on the Rindler chart). Since $x_0$ is constant along $\mathcal{L}_0'$, integrating with $t' = 0$ at $t = 0$ gives $t' = (1+ax_0)t$. $\blacksquare$

> [!note]- Lemma 3: The rest spaces coincide and $\Gamma = (1+ax_0)^{-1}$
> **Statement:** At events simultaneous for both, $\mathcal{O}$ and $\mathcal{O}'$ have equal four-velocity, hence $\mathcal{E}_{u'}(t') = \mathcal{E}_u(t)$, and the Lorentz factor of $\mathcal{O}'$ relative to $\mathcal{O}$ is $\Gamma = (1 + ax_0)^{-1}$.
>
> **Hint:** Both four-velocities are unit future timelike and proportional, so equal; $\Gamma = \mathrm{d}t/\mathrm{d}t'$.
>
> **Why needed:** It gives part 2 and shows the comoving family shares one simultaneity foliation.
>
> > [!note]- Full proof
> > The four-velocity of $\mathcal{O}'$ at $O'(t')$ is the unit tangent $U'^\alpha = c^{-1}\mathrm{d}X_*^\alpha/\mathrm{d}t'$. From Lemma 2, $\mathrm{d}t' = (1+ax_0)\mathrm{d}t$, so $U'^\alpha = c^{-1}(\mathrm{d}X_*^\alpha/\mathrm{d}t)/(1+ax_0)$. Using the derivatives from Lemma 2, $\mathrm{d}(ct_*)/\mathrm{d}t = (1+ax_0)\cosh(act)$ and $\mathrm{d}x_*/\mathrm{d}t = (1+ax_0)\sinh(act)$ (in units of $c$), so $U' = \cosh(act)e_0^* + \sinh(act)e_1^*$ — *identical* to $\mathcal{O}$'s four-velocity $U(t)$ at the simultaneous event. Two equal four-velocities have the same orthogonal hyperplane, so $\mathcal{E}_{u'}(t') = \mathcal{E}_u(t)$. Finally the Lorentz factor of $\mathcal{O}'$ relative to $\mathcal{O}$ is $\Gamma = \mathrm{d}t/\mathrm{d}t' = (1+ax_0)^{-1}$. (Equivalently, $\Gamma = [1 + \vec a(t)\cdot\overrightarrow{O(t)O'(t')}]^{-1}$ with $\vec a(t)\cdot\overrightarrow{OO'} = ax_0$.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{O}'$ be fixed at Rindler coordinate $(x_0, y_0, z_0)$ relative to $\mathcal{O}$. Substituting $x = x_0$, $y = y_0$, $z = z_0$ into the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler-to-inertial transformation]] gives the worldline
> $$ct_* = (x_0 + a^{-1})\sinh(act), \quad x_* = (x_0 + a^{-1})\cosh(act) - a^{-1}, \quad y_* = y_0,\ z_* = z_0.$$
>
> By **Lemma 1**, with $a' := a/(1+ax_0)$ and $x_*' := x_* - x_0$, this satisfies $(a'x_*' + 1)^2 - (a'ct_*)^2 = 1$, an equilateral hyperbola of proper acceleration $a'$. Hence $\mathcal{O}'$ is uniformly accelerated with proper acceleration $a' = a/(1+ax_0)$, and its hyperbola is confocal with $\mathcal{O}$'s (common centre $A = (0,-a^{-1})$, common asymptotes), so $\mathcal{O}'$ shares $\mathcal{O}$'s [[Def - Rindler Horizon|Rindler horizon]].
>
> By **Lemma 2**, integrating the line element along the constant-$x_0$ worldline gives $c\,\mathrm{d}t' = (1+ax_0)c\,\mathrm{d}t$, hence $t' = (1+ax_0)t$ with $t' = 0$ at $t = 0$.
>
> By **Lemma 3**, the four-velocity of $\mathcal{O}'$ at $O'(t')$ equals that of $\mathcal{O}$ at the simultaneous event $O(t)$, so $\mathcal{E}_{u'}(t') = \mathcal{E}_u(t)$, and $\Gamma = \mathrm{d}t/\mathrm{d}t' = (1+ax_0)^{-1}$.
>
> *Corollary.* For $x_0 \neq 0$ the factor $1 + ax_0 \neq 1$, so two comoving clocks at different positions, synchronized at $t = 0$, read different proper times $t' = (1+ax_0)t$ for $t > 0$ — they desynchronize. From $a' = a/(1+ax_0)$: $a' \le a \iff x_0 \ge 0$, and $a' \to +\infty$ as $x_0 \to -a^{-1}$ (the trailing edge near the horizon must accelerate without bound). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Gravitational time dilation and GPS (applied physics, general relativity).** Read $1 + ax_0$ as $1 + \Phi/c^2$ with $\Phi = gx_0$ the gravitational potential: the proper-time relation $\mathrm{d}t' = (1 + gh/c^2)\mathrm{d}t$ for clocks at height difference $h$ is exactly the gravitational time dilation that GPS satellites must correct for (the dominant relativistic correction to satellite clocks). The application is nonobvious because the theorem is derived in flat spacetime for an accelerated observer, yet by the equivalence principle it gives the leading-order gravitational effect; the higher-order corrections require the full Schwarzschild metric of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].

**Surface gravity and the redshift hierarchy of a black hole (general relativity).** The divergence $a' \to +\infty$ as $x_0 \to -a^{-1}$ is the flat-spacetime model of the diverging proper acceleration needed to hover ever closer to a black-hole horizon: a static observer at Schwarzschild radius $r$ feels a proper acceleration that blows up as $r \to 2GM/c^2$, while the acceleration *measured at infinity* (the surface gravity $\kappa$) stays finite. The application battle-tests the source by replacing "Rindler horizon" with "event horizon" and $a^{-1}$ with the near-horizon length scale.

**Lattice clocks and relativistic geodesy (precision metrology).** Optical-lattice clocks are now precise enough that two clocks differing in height by a centimetre on Earth desynchronize measurably, $\mathrm{d}t'/\mathrm{d}t - 1 \approx gh/c^2 \approx 10^{-18}$ per centimetre. The theorem, in its equivalence-principle reading, is the basis of *relativistic geodesy*: measuring the gravitational potential difference between two points by comparing clock rates. The application is surprising because a thought experiment about accelerating rockets turns into a working surveying technique.

---

# Bridges

- **[[Thm - Worldline of a Uniformly Accelerated Observer]]** — this theorem is the statement that the worldline theorem applies *to a whole family*: every comoving observer is uniformly accelerated, so the hyperbola, the velocity-tending-to-$c$, and the asymptotes all carry over with $a \to a' = a/(1+ax_0)$. The confocal family of hyperbolae sharing one centre $A$ is the geometric object underlying the Rindler chart, and this theorem is what licenses treating each $x_0$-slice as an independent accelerated observer.

- **[[Thm - Spectral Shift in an Accelerated Frame]]** — the spectral shift is this theorem applied to light rather than to clocks. Two comoving observers exchange a photon; the ratio of emitted to received frequency is exactly the ratio of their clock rates, $(1 + ax_{\mathrm{em}})$, so the redshift $z = 1/(1+ax_{\mathrm{em}}) - 1$ is the desynchronization read off in the frequency domain. The same factor $1 + ax_0$ governs both, which is why the redshift and the clock drift are the same physics.

- **[[Def - Rindler Coordinates and the Accelerated Frame]]** — the position-dependent clock rate $\mathrm{d}\tau = (1 + ax)\,\mathrm{d}t$, read directly off the Rindler metric component $g_{tt} = (1+ax)^2$, *is* this theorem's proper-time relation for the comoving observer at $x_0 = x$. The metric's $x$-dependence and the clock desynchronization are two statements of one fact: the lapse function $1 + ax$ varies across the frame.

- **Bell's spaceship paradox and Born rigidity** — the result $a' = a/(1+ax_0)$ is the resolution of the paradox in which two rockets accelerate *identically* (same $a$): because rigidity requires the *position-dependent* $a'$, identical accelerations do not preserve proper distance, and a string between the rockets stretches and snaps. To keep a finite body rigid, its trailing edge must accelerate harder than its leading edge by exactly this factor — and since $a' \to \infty$ at $x_0 = -a^{-1}$, no rigid body can reach the horizon. This is developed in [[Ex - Clock desynchronization and Rindler rigidity]].

---

# Unlocked by This

> [!tip] Gravitational Time Dilation and the Pound–Rebka Experiment *(from General Relativity)*
> Read through the equivalence principle, the proper-time relation $\mathrm{d}t' = (1 + ax_0)\,\mathrm{d}t$ with $ax_0 = gx_0/c^2 = \Phi/c^2$ is the **gravitational time dilation**: a clock deeper in a gravitational potential (smaller $\Phi$, nearer the horizon) runs slow relative to one higher up. This is the effect that the **Pound–Rebka experiment** measured in $1959$ by comparing the frequencies of photons emitted at the top and bottom of a tower, and it is the first quantitative crack in special relativity, forcing the metric to vary from place to place and hence spacetime to be curved. The desynchronization of clocks at different potentials is incompatible with a global inertial frame, which is the gateway to [[Special Relativity XXV — Toward Relativistic Gravitation|relativistic gravitation]].

> [!tip] Born Rigidity and the Limits of Rigid Bodies *(from relativistic continuum mechanics)*
> The position-dependent acceleration $a' = a/(1+ax_0)$ is the finite-extent form of **Born rigidity** — the relativistic notion of a body whose every material element keeps a constant proper distance from its neighbours. The divergence of $a'$ at the horizon means a Born-rigid body can extend no farther than $a^{-1}$ toward the horizon, and the **Herglotz–Noether theorem** sharpens this: a Born-rigid body in special relativity has only three degrees of freedom (it cannot, for instance, be spun up from rest while staying rigid). The accelerated rigid ruler of §16.2 is the simplest non-trivial Born-rigid motion, and this theorem supplies its acceleration profile.
