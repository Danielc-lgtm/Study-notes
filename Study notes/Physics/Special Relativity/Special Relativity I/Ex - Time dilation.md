---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

A clock sits at rest at the spatial origin of frame $S'$, which moves at velocity $v$ along the $x$-axis of frame $S$. The clock ticks at intervals of $T_0$ in its own frame: consecutive ticks are the events $(t', x') = (0, 0)$ and $(T_0, 0)$. Working with $c = 1$:

1. Use the Lorentz transformation to find the time interval $T$ between the two ticks as measured in $S$, and show $T = \gamma T_0 \ge T_0$ — the moving clock runs slow.
2. Confirm the same result by computing the **invariant interval** between the two ticks in each frame.
3. **The muon puzzle.** Muons created high in the atmosphere have a rest-frame half-life of about $\tau_0 = 2.2\,\mu\mathrm{s}$ and travel at $v \approx 0.99c$ ($\gamma \approx 7$). The descent to sea level takes about $7\,\mu\mathrm{s}$ as measured from the ground — several half-lives. Explain why muons nonetheless reach the ground in abundance, and check that the muon's-eye-view and the ground's-eye-view agree.

**Recall:**

The computation uses the Lorentz transformation and the interval.

![[Def - The Lorentz Transformation#The Definition]]

The **proper time** between two events on a clock's worldline is the time the clock itself reads — the interval measured in the frame where the clock is at rest, and both events happen at the *same place*. The [[Def - The Spacetime Interval|spacetime interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ is the same in every frame; for two events at the same place in some frame, $\Delta s^2 = \Delta t^2$ there, so $\Delta s$ equals the proper time.

---

# Convergent Strategy

**Problem class.** A *compute-a-relativistic-effect* problem, with part 3 a small *resolve-an-apparent-puzzle* problem. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] prescribes: identify which frame holds the clock, that frame measures the proper time, every other frame dilates it.

**Assumption pattern.** A clock with a known *rest-frame* tick interval is given — the signpost to start in the clock's rest frame $S'$, where the two ticks sit at the same place ($x' = 0$).

**Theorem routing.** Part 1: Lorentz-transform the two tick events from $S'$ to $S$ and read off $\Delta t$. Part 2: evaluate $\Delta s^2$ in each frame — in $S'$ it is $T_0^2$ (same place), in $S$ it is $T^2 - (v T)^2$ (the clock moved) — and equate by [[Thm - Invariance of the Spacetime Interval]].

**Key decision point.** The non-obvious point is recognising that the two ticks happen at the *same place in $S'$* ($x'=0$), so $S'$ measures the proper time $T_0$, and that $S$ — where the clock has moved between ticks — measures the *longer* time $T = \gamma T_0$. Getting the direction of the inequality right depends entirely on identifying which frame has a single clock present at both events.

---

# Legal Operations Used

1. **Work in the rest frame, then boost out.** The two ticks are simplest in $S'$: same place, separated by $T_0$.

2. **Apply the Lorentz transformation** to carry the tick events into $S$.

3. **Use time dilation** — derived here, not quoted: $T = \gamma T_0$.

4. **Compute an invariant in the most convenient frame.** Part 2 evaluates $\Delta s^2$ in $S'$ (trivial: $T_0^2$) and in $S$, and equates.

---

# Hints

> [!note]- Hint 1
> The two ticks are the events $(t',x') = (0,0)$ and $(T_0, 0)$ in $S'$. Use the inverse Lorentz transformation $t = \gamma(t' + vx')$ to find the $S$-time of each. Since $x' = 0$ for both, the spatial term drops out and you get $t$ directly.

> [!note]- Hint 2
> The interval between the ticks. In $S'$: $\Delta t' = T_0$, $\Delta x' = 0$, so $\Delta s^2 = T_0^2$. In $S$: $\Delta t = T$ and the clock has moved, so $\Delta x = vT$, giving $\Delta s^2 = T^2 - v^2 T^2 = T^2(1-v^2)$. Set the two equal.

> [!note]- Hint 3
> For the muons: in the *ground* frame, the muon's internal clock (its decay clock) runs slow by $\gamma \approx 7$, so its effective lifetime is $\gamma\tau_0 \approx 15\,\mu\mathrm{s}$ — long enough to survive the $7\,\mu\mathrm{s}$ descent. In the *muon's* frame, the muon's clock runs normally but the atmosphere is length-contracted, so the distance to the ground is only $(7\,\mu\mathrm{s})\cdot v/\gamma$ of light-travel — covered well within $\tau_0$. The two viewpoints must agree on the one physical fact: does the muon reach the ground?

---

# Solution

A clock measures the shortest time between two events on its own worldline — its proper time — and any frame in which the clock moves assigns a longer time. The effect is symmetric and consistent: each observer correctly sees the *other's* clock run slow, because they compare different pairs of events.

**Step 1: The moving clock runs slow, $T = \gamma T_0$.**

> [!note]- Derivation
> The two ticks are events $E_1 = (t',x') = (0,0)$ and $E_2 = (T_0, 0)$ in $S'$. Apply the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] $t = \gamma(t' + vx')$.
>
> For $E_1$: $t = \gamma(0 + v\cdot 0) = 0$.
> For $E_2$: $t = \gamma(T_0 + v\cdot 0) = \gamma T_0$.
>
> So in $S$ the interval between the ticks is
> $$T = \gamma T_0 - 0 = \gamma T_0 = \frac{T_0}{\sqrt{1-v^2}}.$$
> Since $\gamma \ge 1$, we have $T \ge T_0$: **in $S$, the moving clock's ticks are further apart than $T_0$ — the clock runs slow.** The interval $T_0$ measured in the clock's own frame is the **proper time**: it is the shortest, because there the two ticks happen at the same place and a single clock is present at both.

**Step 2: Confirmation by the invariant interval.**

> [!note]- Derivation
> The [[Def - The Spacetime Interval|spacetime interval]] between the two ticks is, by [[Thm - Invariance of the Spacetime Interval]], the same in every frame.
>
> *In $S'$:* the ticks have $\Delta t' = T_0$, $\Delta x' = 0$ (same place — the clock is at rest). So
> $$\Delta s^2 = \Delta t'^2 - \Delta x'^2 = T_0^2.$$
>
> *In $S$:* the ticks have $\Delta t = T$, and the clock has moved at velocity $v$ during time $T$, so $\Delta x = vT$. Thus
> $$\Delta s^2 = \Delta t^2 - \Delta x^2 = T^2 - v^2 T^2 = T^2(1 - v^2).$$
>
> Equating the two expressions for the one invariant:
> $$T_0^2 = T^2(1-v^2) \;\Longrightarrow\; T = \frac{T_0}{\sqrt{1-v^2}} = \gamma T_0,$$
> in agreement with Step 1. This is the cleaner derivation: it never touches the transformation matrix, only the invariance of the interval. It also exhibits *why* the moving clock runs slow — in $S$ part of the interval is "spent" on the spatial displacement $\Delta x = vT$, so the temporal part $T$ must be larger to keep $\Delta s^2$ fixed at $T_0^2$.

**Step 3: Why the muons reach the ground.**

> [!note]- Derivation
> A muon has rest-frame half-life $\tau_0 \approx 2.2\,\mu\mathrm{s}$ and speed $v \approx 0.99c$, so $\gamma \approx 7$. The descent takes $t_{\text{ground}} \approx 7\,\mu\mathrm{s}$ as measured from the ground — more than three half-lives, which would naively leave almost no surviving muons.
>
> *Ground frame.* The muon's decay is governed by its internal clock, and that clock is *moving* at $0.99c$, so by Step 1 it runs slow by $\gamma \approx 7$. Two events — "muon created" and "muon decays" — happen at the same place *in the muon's frame* (the muon's own location), so the muon frame measures the proper time, $\tau_0$, and the ground frame measures the dilated time $\gamma\tau_0 \approx 15\,\mu\mathrm{s}$. The effective lifetime in the ground frame comfortably exceeds the $7\,\mu\mathrm{s}$ descent, so most muons survive.
>
> *Muon frame.* In the muon's own frame its clock ticks normally — half-life $\tau_0 \approx 2.2\,\mu\mathrm{s}$, no dilation. But now the *atmosphere* is moving, at $0.99c$, so the height of the atmospheric column is length-contracted by $\gamma$. The ground-frame descent distance is $d = v\,t_{\text{ground}}$; in the muon frame it is $d/\gamma$, traversed at speed $v$ in time $d/(\gamma v) = t_{\text{ground}}/\gamma \approx 1\,\mu\mathrm{s}$ — well under one half-life. Most muons survive.
>
> *Agreement.* Both frames predict the same physical fact — the muon reaches the ground — but they attribute it to different effects: the ground frame to time dilation of the muon's clock, the muon frame to length contraction of the atmosphere. This is the hallmark of a correct relativistic analysis: the *invariant* outcome (does the muon arrive?) is frame-independent, while the *explanation* in terms of frame-dependent quantities differs. The two stories are linked by the relativity of simultaneity, and the muon's proper lifetime — the interval along its worldline — is the one invariant both frames agree on.

> [!note]- Complete formal solution
> The ticks are $(t',x') = (0,0)$ and $(T_0,0)$ in $S'$. By $t = \gamma(t'+vx')$, their $S$-times are $0$ and $\gamma T_0$, so $T = \gamma T_0 \ge T_0$: the moving clock runs slow. Equivalently, by interval invariance, in $S'$ the ticks have $\Delta s^2 = T_0^2$ (same place), and in $S$ the clock moves a distance $vT$ so $\Delta s^2 = T^2 - v^2T^2$; equating gives $T_0^2 = T^2(1-v^2)$, hence $T = \gamma T_0$. For the muons ($\gamma \approx 7$): the ground frame sees the muon's decay clock dilated to $\gamma\tau_0 \approx 15\,\mu\mathrm{s} > 7\,\mu\mathrm{s}$, so it survives the descent; the muon frame sees the atmosphere contracted, so the descent takes only $t_{\text{ground}}/\gamma \approx 1\,\mu\mathrm{s} < \tau_0$. Both frames agree the muon reaches the ground. $\blacksquare$

---

# Key Takeaways

**Proper time is the time on the clock, and it is the shortest — identify which frame holds the clock before using $T = \gamma T_0$.** The interval $T_0$ is the proper time: the elapsed time read by the single clock that is present at *both* events. It is the smallest time any frame assigns to that pair of events, because in any other frame the clock has moved, and part of the spacetime interval is then "spent" on spatial displacement, forcing the temporal part to grow. The formula $T = \gamma T_0$ is *not* symmetric in $T$ and $T_0$: $T_0$ is always the rest-frame, single-clock reading. The most common error in the whole subject is to plug in the wrong one and invert the effect. The diagnostic question, asked before any calculation: "the two events — is there a frame with a single clock present at both?" That frame, and only that frame, measures $T_0$.

**Time dilation is symmetric, and the symmetry is not a contradiction.** Each of two observers in relative motion correctly judges the *other's* clock to run slow. This sounds paradoxical until you notice that the two judgements compare *different pairs of events*. When $S$ says "$S'$'s clock is slow", it compares two ticks of $S'$'s clock against $S$'s own clocks at two different places; when $S'$ says the same of $S$, it compares two ticks of $S$'s clock against $S'$'s clocks at two different places. Different pairs, no contradiction. A genuine contradiction would require comparing the *same* pair of events twice and getting two answers — and that never happens. The twin paradox ([[Ex - The twin paradox]]) is precisely the case where the symmetry is broken (one twin accelerates), and only then does a real asymmetry of ageing appear.

**A correct relativistic analysis gives a frame-independent answer to a frame-independent question, even when the explanations differ.** "Does the muon reach the ground?" is a question about a single physical fact — it cannot depend on the observer. And it does not: the ground frame and the muon frame both say yes. But they get there by different routes — time dilation of the muon's clock versus length contraction of the atmosphere — because they decompose the situation into frame-dependent pieces in different ways. This is the deepest methodological lesson of the topic: always check that your invariant conclusion is frame-independent, and do not be alarmed that the *story* changes between frames. The interval along the muon's worldline — its proper lifetime — is the invariant both frames are really computing, dressed up two different ways. When two frames seem to tell incompatible stories, find the invariant question underneath and confirm they agree on *that*.
