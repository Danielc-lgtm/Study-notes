---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Thm - Inertial Worldlines Maximise Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

An astronaut travels to the centre of the Galaxy in a spaceship that maintains a constant proper acceleration $\gamma_{\!a}$ (chosen equal to Earth's gravity $g = 9.81\,\mathrm{m\,s^{-2}}$, so the crew feels normal weight throughout). The trip is the Langevin "tri-hyperbolic" journey: accelerate, reverse thrust at the quarter and three-quarter points, decelerate to rest, so the ship departs Earth and returns. Working with $c$ restored where instructive:

1. Define the natural timescale $T_* = 4c/\gamma_{\!a}$ built from $c$ and the acceleration, and compute it for $\gamma_{\!a} = g$. Express the relation between the round-trip proper time $T'$ measured aboard ship and the coordinate time $T$ measured on Earth as $T = T_*\sinh(T'/T_*)$, and the maximal distance reached as $d = \tfrac12 c T_*[\cosh(T'/T_*) - 1]$.
2. Examine the non-relativistic limit $T' \ll T_*$ and the ultra-relativistic limit $T' \gg T_*$, interpreting each.
3. The galactic centre lies about $26{,}000$ light-years away. Show that a round trip can be completed in a ship-time $T'$ of only about $40$ years (so the centre is *reached* in about $20$ years of ship-time), while roughly $52{,}000$ years elapse on Earth. Comment on a round trip to the Andromeda galaxy ($\sim 2$ million light-years).
4. Reconcile this with the speed limit: the ship never travels faster than light, yet it crosses $26{,}000$ light-years in $20$ years of its own time. How?

**Recall:**

![[Def - Proper Time#The Definition]]

A clock of constant proper acceleration $\gamma_{\!a}$ follows an arc of hyperbola; its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is $U = (\cosh\gamma_{\!a}\tau, \sinh\gamma_{\!a}\tau, 0, 0)$ (with $c=1$), and its [[Def - Proper Time|proper time]] is the metric arc length of its worldline. That a bent worldline carries *less* proper time than the straight one is [[Thm - Inertial Worldlines Maximise Proper Time|the geodesic principle]]. The deficit between ship-time $T'$ and Earth-time $T$ is the quantitative twin paradox.

---

# Convergent Strategy

**Problem class.** An *applied proper-time / twin-paradox* problem at astronomical scale. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: compute proper time along the worldline as $\int dt/\gamma$, and exploit that a constant-proper-acceleration worldline is a hyperbola whose proper-time relations are hyperbolic functions of the single scale $T_*$.

**Assumption pattern.** "Constant proper acceleration $g$" fixes everything: it sets the hyperbolic worldline, and the only free parameter is the dimensionless $T'/T_*$ (ship-time in units of the acceleration timescale). The single number $T_* = 4c/g = 3.87$ years governs the whole problem — below it, the trip is Newtonian; above it, exponentially relativistic.

**Theorem routing.** Part 1 is the [[Ex - Proper time along an accelerated worldline|accelerated-proper-time]] machinery, re-expressed through $T_*$. Part 2 Taylor-expands ($T' \ll T_*$) and exponentially approximates ($T' \gg T_*$). Part 3 plugs $d = 26{,}000$ ly into $d = \tfrac12 cT_*[\cosh(T'/T_*) - 1]$ and solves for $T'$, then reads off $T = T_*\sinh(T'/T_*)$. Part 4 invokes the resolution: the *ship-frame* distance is length-contracted, so the ship crosses a contracted gap, while remaining sub-light.

**Key decision point.** The crux is realising that the enormous Earth-versus-ship time gap and the apparent "faster than light" paradox are two faces of the same fact: in the ultra-relativistic regime $T' \gg T_*$, both $T$ and $d$ grow *exponentially* in $T'$, so a linear increase in ship-time buys an exponential increase in distance and Earth-time. The ship moves at less than $c$ in *every* frame; the exponential payoff comes from proper time being the (short) arc length of a worldline hugging the light cone.

---

# Legal Operations Used

1. **Switch to rapidity / hyperbolic parametrisation** (operation 6 from the topic page). Constant proper acceleration gives hyperbolic functions of proper time; the relations $T = T_*\sinh(T'/T_*)$ and $d = \tfrac12 cT_*[\cosh(T'/T_*) - 1]$ are pure hyperbolic identities.

2. **Compute proper time along the worldline** (proper-time operation). Ship-time $T'$ is the metric arc length of the bent worldline; Earth-time $T$ is the (longer) arc length of the straight one.

3. **Use a Lorentz invariant / length contraction to switch frames** (operation related to invariants). Part 4 resolves the speed-limit puzzle by passing to the ship frame, where the galactic-centre distance is contracted.

---

# Hints

> [!note]- Hint 1
> Build on the [[Ex - Proper time along an accelerated worldline|constant-proper-acceleration]] result. With $T_* = 4c/\gamma_{\!a}$, the round-trip relations are $T = T_*\sinh(T'/T_*)$ and $d = \tfrac12 cT_*[\cosh(T'/T_*) - 1]$. For $\gamma_{\!a} = g = 9.81\,\mathrm{m\,s^{-2}}$, compute $T_* = 4c/g$ in seconds, then convert to years ($\approx 3.87$ yr).

> [!note]- Hint 2
> For $T' \ll T_*$: $\sinh x \approx x$ and $\cosh x - 1 \approx x^2/2$, giving $T \approx T'$ (no differential ageing) and $d \approx$ the Newtonian $\tfrac12 (\gamma_{\!a}/4)(T'/4)^2$ per quarter-leg. For $T' \gg T_*$: $\sinh x \approx \cosh x \approx \tfrac12 e^x$, so $T \approx \tfrac12 T_* e^{T'/T_*}$ and $d \approx \tfrac12 cT_*\cdot\tfrac12 e^{T'/T_*} = \tfrac12 cT$ — distance grows as half the Earth-time, exponentially in ship-time.

> [!note]- Hint 3
> Set $d = 26{,}000$ ly. Since $T' \gg T_*$ (anticipate), use $d \approx \tfrac14 cT_* e^{T'/T_*}$, solve $e^{T'/T_*} = 4d/(cT_*)$, so $T'/T_* = \ln[4d/(cT_*)]$. With $cT_* = 4c^2/g \approx 3.87$ ly, get $T'/T_* \approx \ln(4\cdot 26000/3.87)$. Multiply by $T_* = 3.87$ yr to get $T' \approx 40$ yr; then $T = T_*\sinh(T'/T_*) \approx \tfrac12 T_* e^{T'/T_*} \approx 52{,}000$ yr.

> [!note]- Hint 4
> In the ship's instantaneous frame the distance to the galactic centre is *length-contracted* by the (huge, peak) Lorentz factor, so the ship crosses a much shorter gap. The ship's speed is always below $c$ in every frame; it covers $26{,}000$ ly of *Earth-frame* distance in $20$ yr of *ship-time* because those are measured in different frames.

---

# Solution

This is the twin paradox pushed to its spectacular conclusion: relativity permits a human to visit the galactic centre within a working lifetime, at the price of returning to an Earth aged by fifty millennia. The plan: Step 1 sets up the hyperbolic relations through the single scale $T_*$; Step 2 reads the two limits; Step 3 plugs in the galactic-centre distance; Step 4 dissolves the speed-limit puzzle.

**Step 1: The acceleration timescale and the hyperbolic relations.**

> [!note]- Derivation
> A ship of constant proper acceleration $\gamma_{\!a}$ traces arcs of hyperbola. From the [[Ex - Proper time along an accelerated worldline|accelerated-worldline]] analysis, the natural timescale built from $c$ and $\gamma_{\!a}$ is
> $$T_* := \frac{4c}{\gamma_{\!a}},$$
> which in Newtonian terms is four times the time to reach light speed from rest at acceleration $\gamma_{\!a}$. For Earth's gravity $\gamma_{\!a} = g = 9.81\,\mathrm{m\,s^{-2}}$,
> $$T_* = \frac{4 \times 2.998\times 10^8\,\mathrm{m\,s^{-1}}}{9.81\,\mathrm{m\,s^{-2}}} = 1.22\times 10^8\,\mathrm{s} \approx 3.87\ \text{years}.$$
> For the full tri-hyperbolic round trip (four quarter-arcs), the relation between the ship's total proper time $T'$ and Earth's coordinate time $T$ is (re-expressing the $\operatorname{arsinh}$ formula through $T_*$, using $\sqrt{1 + \sinh^2} = \cosh$):
> $$\boxed{\,T = T_*\sinh\!\Big(\frac{T'}{T_*}\Big)\,}, \qquad \boxed{\,d = \frac{1}{2}cT_*\Big[\cosh\!\Big(\frac{T'}{T_*}\Big) - 1\Big]\,},$$
> where $d$ is the maximal distance from Earth (reached at the half-way point). These are exact hyperbolic identities; everything follows from them.

**Step 2: The two limits.**

> [!note]- Derivation
> *Non-relativistic, $T' \ll T_*$.* Using $\sinh x \approx x$ and $\cosh x - 1 \approx x^2/2$,
> $$T \approx T', \qquad d \approx \frac{1}{2}cT_*\cdot\frac12\Big(\frac{T'}{T_*}\Big)^2 = \frac{c}{4T_*}T'^2 = 2 \times \frac{1}{2}\gamma_{\!a}\Big(\frac{T'}{4}\Big)^2.$$
> The ship never reaches relativistic speed; there is no differential ageing ($T \approx T'$), and the distance is the Newtonian $\tfrac12\gamma_{\!a}(\text{time})^2$ for each accelerating leg. This is the expected non-relativistic result.
>
> *Ultra-relativistic, $T' \gg T_*$.* Using $\sinh x \approx \cosh x \approx \tfrac12 e^x$,
> $$T \approx \frac{T_*}{2}\,e^{T'/T_*}, \qquad d \approx \frac{cT_*}{4}\,e^{T'/T_*} = \frac{1}{2}cT.$$
> Now both Earth-time and distance grow *exponentially* in the ship's proper time, while the distance settles to half the Earth-time (the ship spends most of the trip at nearly $c$, covering $\approx cT/2$ out and back). A linear investment of ship-years buys an exponential return in distance and Earth-years — the regime in which interstellar travel becomes, in principle, possible.

**Step 3: The galactic centre and beyond.**

> [!note]- Derivation
> The galactic centre is $d \approx 26{,}000$ ly away. Anticipating the ultra-relativistic regime, use $d \approx \tfrac14 cT_* e^{T'/T_*}$, so
> $$e^{T'/T_*} = \frac{4d}{cT_*}, \qquad \frac{T'}{T_*} = \ln\!\frac{4d}{cT_*}.$$
> With $cT_* = 4c^2/\gamma_{\!a} \approx 3.87$ ly (the light-distance corresponding to $T_*$),
> $$\frac{T'}{T_*} = \ln\!\frac{4\times 26{,}000}{3.87} = \ln(2.69\times 10^4) \approx 10.2,$$
> so $T' \approx 10.2 \times 3.87 \approx 39.5$ years for the *round trip*. The centre is therefore *reached* in about half that, $\approx 20$ years of ship-time. Earth-time is
> $$T = T_*\sinh\!\Big(\frac{T'}{T_*}\Big) \approx \frac{T_*}{2}e^{T'/T_*} = \frac{3.87}{2}\times 2.69\times 10^4 \approx 5.2\times 10^4\ \text{years}.$$
> So an astronaut can fly to the centre of the Galaxy and back, ageing under $40$ years, while $52{,}000$ years pass on Earth — long enough that no one who waved goodbye will be there to greet the return; the report can be made only to distant descendants. A round trip to **Andromeda** ($\sim 2$ million ly) takes only $T' \approx 56$ years of ship-time, but the ship returns to an Earth aged by $\sim 3$ million years — at which point, as Gourgoulhon dryly notes, the traveller will at the very least face a language barrier. (Pure kinematics: the energy cost of sustaining $1\,g$ for decades is prohibitive with any foreseeable technology — but relativity does not forbid it.)

**Step 4: Reconciling with the speed limit.**

> [!note]- Derivation
> The puzzle: the ship covers $26{,}000$ ly in $20$ years of its own time, an apparent speed of $1{,}300\,c$ — yet nothing exceeds $c$. The resolution is that *the two numbers are measured in different frames*, and within any single frame the ship is sub-light.
>
> In the *Earth frame*, the ship crosses $26{,}000$ ly in $\approx 26{,}000$ years of Earth-time (it travels at just under $c$), entirely consistent with the speed limit. The "$20$ years" is the ship's *proper time*, the short metric arc length of its nearly-null worldline.
>
> Equivalently, in the *ship's instantaneous rest frame*, the distance to the galactic centre is **length-contracted**: at peak Lorentz factor $\gamma_{\text{peak}} \sim 10^3$, the $26{,}000$ ly contracts to $26{,}000/\gamma_{\text{peak}} \sim 26$ ly, which the ship crosses (at nearly $c$) in $\sim 26$ years of... well, the bookkeeping is subtle because the ship is non-inertial, but the upshot is that the ship sees a *contracted galaxy* and crosses the short gap in a short proper time, always moving at less than $c$ relative to the local stars. There is no frame in which the ship outruns light. The astronaut reaches the centre quickly not by exceeding $c$ but because proper time is the (short) arc length of a worldline that hugs the light cone — exactly the [[Thm - Inertial Worldlines Maximise Proper Time|geodesic principle]] working in the traveller's favour: their bent, near-null worldline is *short* in proper time. This is genuine **time travel to the future** (the traveller arrives in Earth's distant future) — but never to the past, since the worldline stays inside the forward light cone throughout.

> [!note]- Complete formal solution
> A ship at constant proper acceleration $\gamma_{\!a}$ has acceleration timescale $T_* = 4c/\gamma_{\!a}$; for $\gamma_{\!a} = g$, $T_* = 1.22\times 10^8\,\mathrm{s} = 3.87$ yr. The round-trip relations are $T = T_*\sinh(T'/T_*)$ and $d = \tfrac12 cT_*[\cosh(T'/T_*) - 1]$. For $T' \ll T_*$: $T \approx T'$, $d \approx (c/4T_*)T'^2$ (Newtonian). For $T' \gg T_*$: $T \approx \tfrac12 T_* e^{T'/T_*}$, $d \approx \tfrac12 cT$ (exponential). For the galactic centre $d = 26{,}000$ ly, with $cT_* = 3.87$ ly: $T'/T_* = \ln(4d/cT_*) = \ln(2.69\times 10^4) \approx 10.2$, so $T' \approx 39.5$ yr round trip ($\approx 20$ yr to arrive), $T = T_*\sinh(10.2) \approx 5.2\times 10^4$ yr on Earth. Andromeda ($2$ Mly): $T' \approx 56$ yr, $T \approx 3$ Myr. The ship never exceeds $c$ in any frame: $26{,}000$ ly is the Earth-frame distance (crossed in $\sim 26{,}000$ Earth-years), while $20$ yr is the ship's proper time — the short arc length of a near-null worldline, equivalently the time to cross the length-contracted galaxy. This is time travel to the future, the worldline staying inside the forward light cone. $\blacksquare$

> [!warning] Illegal but tempting: concluding the ship "effectively" travels faster than light
> Dividing $26{,}000$ ly by $20$ ship-years gives $1{,}300\,c$, tempting the conclusion that the ship beats light "from its own point of view". This conflates two frames: the *distance* is Earth-frame, the *time* is ship-frame, and a ratio of quantities from different frames is not a speed. In any *single* inertial frame the ship's speed is strictly below $c$ — in the Earth frame it crosses $26{,}000$ ly in $\sim 26{,}000$ years; in the ship's local frame it crosses a length-contracted gap of tens of light-years in a comparable proper time. The correct statement is that proper time is frame-dependent and is the *short* metric length of the worldline; large coordinate distances are crossed in small proper times precisely because the worldline approaches the light cone, where proper time vanishes. The diagnostic: a "speed" must have numerator and denominator measured in the *same* frame, and every such honest speed of the ship is below $c$.

---

# Key Takeaways

**One number, $T_* = 4c/\gamma_{\!a}$, governs the whole relativistic-rocket problem.** The acceleration timescale $T_* = 4c/\gamma_{\!a}$ (about $3.87$ years for $1\,g$) is the watershed: a trip lasting much less than $T_*$ of ship-time is Newtonian (no differential ageing, distance $\sim\tfrac12 g t^2$), while a trip lasting much more than $T_*$ is exponentially relativistic ($T$ and $d$ both $\sim e^{T'/T_*}$). The reusable structure is that constant proper acceleration makes every kinematic relation a hyperbolic function of the single dimensionless ratio $T'/T_*$, so the entire family of journeys — to the nearest star, to the galactic centre, to Andromeda — is read off one pair of formulas. The trigger: any "rocket at constant $g$" or "constant-proper-acceleration journey" problem reduces to evaluating $\sinh, \cosh$ of $T'/T_*$, and the regime is decided by whether $T'$ is below or above $T_*$.

**Proper time is the short arc length of a near-null worldline — which is why the future is reachable but the past is not.** The astronaut reaches the galactic centre in $20$ years of ship-time not by any superluminal trick but because their bent, fast worldline is *short* in proper time, the [[Thm - Inertial Worldlines Maximise Proper Time|geodesic principle]] working for them: the straighter (stay-at-home) worldline is the long one. As the ship hugs the light cone, its proper time per unit Earth-time shrinks toward zero, so an arbitrary coordinate distance can be crossed in a small proper time. This is genuine time travel *to the future* — the traveller arrives in Earth's distant future, having aged little. But the same Minkowski structure forbids travel to the *past*: the worldline stays inside the forward light cone at every instant, so the ship can never reach an event earlier than its departure. The asymmetry between future (reachable) and past (forbidden) is the parallelism of light cones in flat spacetime, broken only when gravity tips them over.

**Apparent superluminal travel is always a frame-mixing illusion — keep numerator and denominator in one frame.** The seductive "$1{,}300\,c$" comes from dividing an Earth-frame distance by a ship-frame time. A genuine speed requires both measured in the same frame, and every such honest speed of the ship is below $c$: in the Earth frame the trip takes $\sim 26{,}000$ years, in the ship frame the galaxy is length-contracted to a crossable size. This frame-mixing trap recurs throughout relativity — in the [[Ex - The twin paradox|twin paradox]], in muon decay, in cosmological "recession faster than light" — and the diagnostic is always the same: identify which frame each quantity belongs to before forming a ratio. The deeper lesson is that proper time and coordinate distance are not commensurable as a velocity; the only frame-independent statement is that the worldline is everywhere timelike, hence everywhere slower than light. See [[Ex - Proper time along an accelerated worldline]] for the derivation of the hyperbolic relations and [[Ex - The Hafele-Keating experiment]] for the experimental confirmation that proper time really does depend on the worldline.
