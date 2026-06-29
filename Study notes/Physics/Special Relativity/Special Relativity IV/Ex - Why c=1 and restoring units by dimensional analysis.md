---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Spacetime Interval"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

Throughout these notes we set $c = 1$. This problem makes the convention precise and gives the mechanical recipe for restoring $c$ in any formula.

1. Explain, following Tong, why setting $c = 1$ is not a numerical trick but a choice of units that reflects a physical fact — that space and time are measured in the same units once you know the relationship between them. Give the analogy of measuring $x$ in centimetres and $y$ in inches.
2. State the conversion factor: in units where $c = 1$, one second of time equals one *light-second* of distance. Write $c$ in such units.
3. Give the dimensional-analysis recipe: starting from a $c = 1$ formula, how do you reinsert the factors of $c$ to obtain the standard-units formula? Apply it to (a) the [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$, (b) the [[Def - The Lorentz Transformation|Lorentz factor]] $\gamma = (1 - v^2)^{-1/2}$, (c) the boost $t' = \gamma(t - vx)$, and (d) the [[Def - Rapidity|rapidity]] relation $v = \tanh\varphi$.
4. Identify which quantities become dimensionless when $c = 1$ and explain why that is the point.

**Recall:**

In an inertial frame an event has coordinates $(t, x, y, z)$. With $c$ restored, the [[Def - The Spacetime Interval|spacetime interval]] is $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ and the [[Def - The Lorentz Transformation|Lorentz transformation]] for a boost along $x$ is $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$, with $\gamma = (1 - v^2/c^2)^{-1/2}$. The [[Def - Rapidity|rapidity]] is defined by $v/c = \tanh\varphi$, $\gamma = \cosh\varphi$. The dimensionless velocity is $\beta = v/c$.

---

# Convergent Strategy

**Problem class.** A *units / book-keeping* problem — not a computation of a physical effect but a meta-skill: translating between the $c = 1$ convention used for clean algebra and the standard SI form needed for a numerical answer. The [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]] flags that $c = 1$ is a standing convention and that $c$ is restored by dimensional analysis.

**Assumption pattern.** The only "assumption" is the convention $c = 1$ together with the dimensional fact $[c] = \text{length}/\text{time}$. Recognising that $c$ is a *conversion factor between length and time units* — the way $2.54\,\mathrm{cm/inch}$ converts between two length units — is the entire conceptual content.

**Theorem routing.** No theorem; the route is dimensional homogeneity. Every physical equation must be dimensionally consistent, so reinserting $c$ is uniquely determined by demanding that each term carry the same dimension once the artificial $c = 1$ is undone.

**Key decision point.** The one judgement is *where* the factors of $c$ go. The rule is mechanical: replace $t \to ct$ (so time-as-length), or equivalently $v \to v/c$ (velocity-as-dimensionless), and insert the minimum powers of $c$ to make every term have matching dimension. The non-obvious part is realising the answer is *unique* — there is exactly one way to restore $c$ consistently — which is why the recipe always works.

---

# Legal Operations Used

1. **Restore $c$ by dimensional analysis (a standing-convention operation).** Begin from the $c = 1$ formula and insert powers of $c$ so that, with $[t] = \text{time}$, $[x] = \text{length}$, $[v] = \text{length}/\text{time}$, every additive term and every argument of a transcendental function is dimensionally homogeneous.

2. **Work in the rest/natural units, then convert out (operation 2 from the topic page, applied to units rather than frames).** The clean derivation is done at $c = 1$; the final answer is converted to SI by the recipe, exactly as a physical computation is done in the convenient frame and transported out.

---

# Hints

> [!note]- Hint 1
> Two terms can only be added if they have the same dimension. In $\Delta s^2 = \Delta t^2 - \Delta x^2$ with $c = 1$, the terms $\Delta t^2$ (time$^2$) and $\Delta x^2$ (length$^2$) are being subtracted — which is only legal if time and length are the *same* unit. What conversion factor makes them the same?

> [!note]- Hint 2
> $c \approx 3\times 10^8\,\mathrm{m/s}$. Setting $c = 1$ means $3\times 10^8\,\mathrm{m} = 1\,\mathrm{s}$, i.e. one second "is" $3\times 10^8$ metres of distance (a light-second). The number $1$ has units of light-seconds per second.

> [!note]- Hint 3
> To restore $c$: wherever a time $t$ appears that is being compared to a length, write $ct$; wherever a velocity $v$ appears, it is really $v/c$ (dimensionless). Then check each term's dimension and insert the unique power of $c$ that fixes it.

> [!note]- Hint 4
> A transcendental function like $\tanh$, $\cosh$, $\exp$ can only take a *dimensionless* argument. So the rapidity $\varphi$ must be dimensionless, which forces $v/c$ (not $v$) to be the natural velocity variable.

---

# Solution

The whole exercise is the single principle that $c$ is a unit conversion, not a physical constant to be respected. Step 1 gives the conceptual analogy (cm vs inches), Step 2 fixes the conversion factor (the light-second), Step 3 turns it into a mechanical recipe and applies it to four formulas, and Step 4 records which quantities go dimensionless. The recipe is forced by dimensional homogeneity and is therefore unique.

**Step 1: $c = 1$ is a choice of units, and it encodes that space and time are alike.**

> [!note]- Derivation
> Tong's analogy: imagine you measured $x$-distances in centimetres and $y$-distances in inches. You would then find a "fundamental constant of nature" $\lambda \approx 2.54\,\mathrm{cm/inch}$ relating the two, and Pythagoras would read $d^2 = x^2 + (\lambda y)^2$. This would be a *dumb* thing to do, because the rotational symmetry of space tells you $x$ and $y$ are the same kind of thing and should be measured in the same unit; $\lambda$ is then just $1$ and disappears.
>
> The speed of light plays exactly the role of $\lambda$, but between space and time. The existence of a universal speed $c$ is "Nature's way of telling us that space and time are more similar than our ancestors realised". We labelled them with different units (seconds, metres) only because we did not know they were related; once the boost symmetry between space and time is recognised, measuring them in the same unit is natural, and the conversion factor $c$ becomes $1$ and disappears. Insisting on keeping $c$ in the fundamental equations is "no more sensible than retaining $\lambda$".

**Step 2: the conversion factor is the light-second.**

> [!note]- Derivation
> Choose the unit of length to be the light-second — the distance light travels in one second, $\approx 3\times 10^8\,\mathrm{m}$. Then
> $$c = 1\ \frac{\text{light-second}}{\text{second}} = 1.$$
> In these units time (in seconds) and distance (in light-seconds) are numerically interchangeable: a distance of "$5$" means five light-seconds, a time of "$5$" means five seconds, and light moves one unit of distance per unit of time. Equivalently one may keep metres and measure time in metres of light-travel ($1\,\mathrm{m}$ of time $= 1\,\mathrm{m}/c \approx 3.3\,\mathrm{ns}$). Either way $c = 1$ and time and length share a unit.

**Step 3: the dimensional-analysis recipe, applied.**

> [!note]- Derivation
> **Recipe.** In a $c = 1$ formula, restore $c$ by: (i) replacing every velocity $v$ by $v/c$ so it becomes dimensionless, *or* equivalently by treating each bare time $t$ that is added to or subtracted from a length as $ct$; then (ii) inserting the unique power of $c$ in each term that makes all additive terms — and all arguments of transcendental functions — dimensionally homogeneous. Uniqueness is guaranteed because $c$ is the only quantity with dimension $\text{length}/\text{time}$ available.
>
> **(a) Interval.** $c=1$: $\Delta s^2 = \Delta t^2 - \Delta x^2$. The term $\Delta t^2$ has dimension time$^2$, $\Delta x^2$ has dimension length$^2$; to subtract them, multiply $\Delta t$ by $c$:
> $$\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2.$$
> Now both terms have dimension length$^2$ (and $\Delta s$ has units of length).
>
> **(b) Lorentz factor.** $c=1$: $\gamma = (1 - v^2)^{-1/2}$. The argument $v^2$ has dimension velocity$^2$ but is subtracted from the pure number $1$ — illegal unless $v$ is made dimensionless. Replace $v \to v/c$:
> $$\gamma = \left(1 - \frac{v^2}{c^2}\right)^{-1/2}.$$
> Now $v^2/c^2$ is dimensionless and $\gamma$ is dimensionless, as it must be (it multiplies times and lengths without changing their units).
>
> **(c) Boost.** $c=1$: $t' = \gamma(t - vx)$. Here $t'$ and $t$ are times, but $vx$ has dimension velocity $\times$ length $=$ length$^2$/time — not a time. Insert $c^{-2}$:
> $$t' = \gamma\left(t - \frac{vx}{c^2}\right),\qquad x' = \gamma(x - vt).$$
> Check: $vx/c^2$ has dimension $(\text{length}/\text{time})(\text{length})/(\text{length}/\text{time})^2 = \text{time}$, matching $t$. In the space equation $vt$ is already a length, so no $c$ is needed there.
>
> **(d) Rapidity.** $c=1$: $v = \tanh\varphi$. The function $\tanh$ requires a dimensionless argument, so $\varphi$ is dimensionless; but then its $\tanh$ is dimensionless and cannot equal a velocity. Divide by $c$:
> $$\frac{v}{c} = \tanh\varphi,\qquad \gamma = \cosh\varphi,\qquad \frac{v\gamma}{c} = \sinh\varphi.$$
> Now both sides of $v/c = \tanh\varphi$ are dimensionless.

**Step 4: what goes dimensionless, and why that is the point.**

> [!note]- Derivation
> Setting $c = 1$ makes the following dimensionless or unit-shared: velocity $\beta = v/c$ (was length/time, now a pure number in $[0,1)$); the [[Def - Rapidity|rapidity]] $\varphi$ (already dimensionless, now equal to $\tanh^{-1}v$ directly); and time and length share one unit so $t$ and $x$ are added and subtracted freely. The Lorentz factor $\gamma$ and the boost matrix entries are dimensionless in either convention.
>
> The *point* is that the dimensionless combination is the physically meaningful one. Velocities only matter relative to $c$ — a speed is "fast" or "slow" only by comparison with light — so $\beta = v/c$ is the true variable, and the factor of $c$ in $v$ is an artefact of measuring length and time in unrelated units. Once $c = 1$, the symmetry between space and time in the [[Thm - Invariance of the Spacetime Interval|interval]] and the boost is *manifest*: $\Delta s^2 = \Delta t^2 - \Delta x^2$ treats $t$ and $x$ on the same footing, which is exactly the structural insight that the boost mixes them like a rotation.

> [!note]- Complete formal solution
> Setting $c = 1$ is the choice of length unit (the light-second) in which time and distance share a unit; it reflects the physical fact, exposed by the existence of a universal speed, that space and time are the same kind of quantity, just as a sensible choice of units would measure $x$ and $y$ in the same length unit rather than introducing a spurious constant $\lambda \approx 2.54\,\mathrm{cm/inch}$. In these units $c = 1\ \text{light-second/second}$. To restore $c$ in any formula, demand dimensional homogeneity, inserting the unique powers of $c$ (the only quantity of dimension length/time): the interval becomes $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$; the Lorentz factor $\gamma = (1 - v^2/c^2)^{-1/2}$; the boost $t' = \gamma(t - vx/c^2)$, $x' = \gamma(x - vt)$; and the rapidity relations $v/c = \tanh\varphi$, $\gamma = \cosh\varphi$. The quantities that become dimensionless are $\beta = v/c$ and the rapidity $\varphi$, and that is the point: only the dimensionless ratio $v/c$ is physically meaningful, and $c = 1$ makes the space–time symmetry of the interval and boost manifest. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might "restore $c$" by simply multiplying the whole formula by some power of $c$ until it "looks right". This fails because different *terms* need different powers — in the boost, $t'$ needs no $c$ but $vx$ needs $c^{-2}$ — and an overall factor cannot fix term-by-term mismatches. The correct recipe restores $c$ *per term* (and per transcendental argument), guided by the requirement that each additive piece carry identical dimension. Always check the argument of every $\sqrt{\,}$, $\tanh$, $\exp$ separately: it must be dimensionless.

---

# Key Takeaways

**A "fundamental constant" that is really a unit conversion can and should be set to one.** The deepest lesson is conceptual: $c$ is not a property of light to be carried reverently through every equation, it is the conversion factor between the units we historically used for time and for space. The existence of a single universal speed is the signal that time and space are the same kind of quantity, and a unit system that respects this (light-seconds, or natural units) sets $c = 1$ and removes the clutter. The same logic later sets $\hbar = 1$ (action is dimensionless), $k_B = 1$ (temperature is energy), and $G = 1$ (Planck units) — each time, a "constant" is revealed as a unit conversion and absorbed. The trigger for recognising such a constant is that it appears *only* in fixed combinations ($v/c$, $E/k_BT$, $S/\hbar$) and never alone in a physically meaningful way.

**Dimensional homogeneity makes the restoration of $c$ unique and mechanical.** Because $c$ is the only available quantity of dimension length/time, there is exactly one way to reinsert it consistently, and the recipe — make every additive term and every transcendental argument dimensionally matched — finds it without guesswork. This is a fully general technique: any natural-units formula can be de-naturalised by the same procedure (restore $\hbar$ by tracking action, $k_B$ by tracking energy-vs-temperature, etc.). The diagnostic to internalise is that *arguments of transcendental functions must be dimensionless* — this single check immediately tells you, for instance, that rapidity is $\tanh^{-1}(v/c)$ and not $\tanh^{-1}(v)$, and it catches the most common unit error in relativistic formulas.

**The dimensionless combination is the physics; the dimensionful split is the accident.** A velocity matters only relative to $c$; an energy only relative to a temperature or a rest mass; an action only relative to $\hbar$. Setting the conversion constant to one isolates the dimensionless ratio that carries the physical content and discards the historical accident of incompatible units. In special relativity this is why $\beta = v/c$ and the rapidity $\varphi$ are the right variables: $\beta \to 1$ is the light-speed limit and $\varphi \to \infty$ is the same limit unfolded onto the line, and both are visible only after $c$ is set to one and the space–time symmetry of the [[Thm - Invariance of the Spacetime Interval|interval]] is laid bare.
