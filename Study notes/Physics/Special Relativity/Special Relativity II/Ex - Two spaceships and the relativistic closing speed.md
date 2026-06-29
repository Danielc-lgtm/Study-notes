---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Relativistic Velocity Addition"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

*(A qualifying-exam-style problem.)* Two spaceships, $A$ and $B$, approach each other head-on. In the Earth frame, each moves at the *same* speed $u$ (towards the other). Restore $c$ throughout.

1. **Closing speed reckoned from Earth.** What is the rate at which the gap between the ships shrinks *as measured in the Earth frame* — the "Earth-frame closing speed"? Show it can exceed $c$ (up to $2u$), and explain why this is *not* a violation of relativity.
2. **Closing speed reckoned by a ship.** What is the speed of ship $B$ *as measured in the rest frame of ship $A$* — the physically meaningful relative speed? Use the relativistic velocity-addition law, and show it is always below $c$.
3. **The inverse problem (the exam question).** Suppose ship $A$ measures ship $B$ to approach at $0.70c$. Find the common Earth-frame speed $u$ of each ship. Set up the equation $0.70c = 2u/(1 + u^2/c^2)$, solve the quadratic, and contrast your answer with the naive Galilean halving $u = 0.35c$.
4. Redo part 2 via [[Def - Rapidity|rapidity]]: show the relative rapidity is $2\varphi_u$ and the relative speed $c\tanh(2\varphi_u)$, and confirm it matches.

**Recall:**

![[Thm - Relativistic Velocity Addition#Statement]]

To find $B$'s speed in $A$'s rest frame, transform to that frame: $A$ is at rest, the Earth moves at $u$ (in the direction from $A$ towards $B$), and $B$ moves at $u$ relative to Earth in the same direction — so $B$'s speed relative to $A$ is the relativistic combination of $u$ and $u$. The **rapidity** of a velocity $w$ is $\varphi_w = \tanh^{-1}(w/c)$; collinear boosts add rapidities ([[Def - Rapidity]]).

---

# Convergent Strategy

**Problem class.** A *compute-a-combined-velocity plus inverse-problem* — a staple qualifying-exam question testing whether the student distinguishes "closing speed in a third frame" (which can exceed $c$) from "relative speed in one object's frame" (which cannot). The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] says: switch to the rest frame of one object and apply velocity addition.

**Assumption pattern.** The key datum is "each ship at the same speed $u$ in the Earth frame, head-on". The Earth-frame closing speed is a Galilean sum $2u$ (legitimately up to $2c$, since it is not any single object's speed). The relative speed in $A$'s frame is the relativistic combination of $u$ with $u$. The inverse problem inverts this.

**Theorem routing.** Part 1 is the Galilean closing speed $u + u = 2u$ (a coordinate rate, not an object's speed). Part 2 routes through [[Thm - Relativistic Velocity Addition]] with both inputs $u$: $w = 2u/(1 + u^2/c^2)$. Part 3 inverts: solve $0.70c = 2u/(1 + u^2/c^2)$ for $u$. Part 4 routes through [[Def - Rapidity]]: relative rapidity $2\varphi_u$.

**Key decision point.** The crux is distinguishing two different "speeds": the *Earth-frame closing speed* (how fast the Earth-frame coordinate gap shrinks, which is $2u$ and may exceed $c$ — no object moves this fast, so no violation) versus the *relative speed* (how fast $B$ moves in $A$'s rest frame, which is the relativistic combination and is always $< c$). Confusing them is the intended trap. The inverse problem then tests whether the student inverts the *relativistic* formula, not the Galilean one.

---

# Legal Operations Used

1. **Add velocities relativistically** (operation 6 from the topic page). Part 2 combines $u$ and $u$ via $w = (u + u)/(1 + u^2/c^2)$ to get $B$'s speed in $A$'s frame.

2. **Work in the rest frame, then boost out** (operation 2). Part 2 transforms to $A$'s rest frame, where $A$ is at rest and the combination of Earth's and $B$'s motion gives $B$'s relative speed.

3. **Switch to rapidity to make boosts additive** (operation 7). Part 4 computes the relative rapidity as $2\varphi_u$ directly, bypassing the rational formula.

---

# Hints

> [!note]- Hint 1
> Earth-frame closing speed: the gap between the ships is an Earth-frame distance, and each end of it moves at $u$ towards the other, so the gap shrinks at $u + u = 2u$. This can be up to $2c$. It is *not* any object's speed — it is the rate of change of a coordinate separation — so it does not violate the speed limit. Nothing material moves at $2u$; the *gap* does.

> [!note]- Hint 2
> For $B$'s speed in $A$'s frame, sit in $A$'s rest frame. There, the Earth recedes at $u$ and $B$ moves at $u$ relative to the Earth (same direction, towards $A$). Combine relativistically: $w = (u + u)/(1 + u\cdot u/c^2) = 2u/(1 + u^2/c^2)$. Check $w < c$: at $u \to c$, $w \to 2c/2 = c$, approached but not exceeded.

> [!note]- Hint 3
> Set $w = 0.70c$: $0.70c = 2u/(1 + u^2/c^2)$. Let $\beta = u/c$. Then $0.70(1 + \beta^2) = 2\beta$, i.e. $0.70\beta^2 - 2\beta + 0.70 = 0$. Solve the quadratic for $\beta$ and take the physical root ($\beta < 1$). Compare with the Galilean guess $\beta = 0.35$.

> [!note]- Hint 4
> Rapidity: $A$'s rest frame is reached by boosting Earth by rapidity $\varphi_u$, and $B$ moves at rapidity $\varphi_u$ relative to Earth, so $B$'s rapidity relative to $A$ is $\varphi_u + \varphi_u = 2\varphi_u$, and its speed is $c\tanh(2\varphi_u)$. Use $\tanh(2\varphi) = 2\tanh\varphi/(1 + \tanh^2\varphi)$ to confirm this equals $2u/(1 + u^2/c^2)$.

---

# Solution

The Earth-frame closing speed is the Galilean $2u$ and may exceed $c$ without violating relativity, because it is a coordinate rate, not an object's speed. The physically meaningful relative speed — $B$ as seen by $A$ — is the relativistic combination $2u/(1 + u^2/c^2)$, always below $c$. Inverting it for a measured $0.70c$ gives $u \approx 0.41c$, well above the naive $0.35c$.

**Step 1: Earth-frame closing speed is $2u$, and may exceed $c$ harmlessly.**

> [!note]- Derivation
> The "closing speed" in the Earth frame is the rate at which the Earth-frame *gap* between the ships shrinks. Ship $A$ moves towards $B$ at $u$ and ship $B$ towards $A$ at $u$, so the separation decreases at
> $$\text{(Earth-frame closing speed)} = u + u = 2u.$$
> For $u > c/2$ this exceeds $c$, reaching $2c$ as $u \to c$. **This is not a violation of relativity.** The speed limit forbids any *object*, signal, or causal influence from moving faster than $c$ in a given frame — and no object here moves at $2u$. The quantity $2u$ is the time-derivative of a coordinate *difference* between two separately sub-light objects; it is a bookkeeping rate, not the velocity of anything material. Nothing is transported, and no information propagates, at $2u$. (Contrast with part 2, which asks for an actual object's speed in an actual frame, and which therefore *must* be below $c$.)

**Step 2: $B$'s speed in $A$'s frame is $2u/(1 + u^2/c^2) < c$.**

> [!note]- Derivation
> The physically meaningful relative speed is how fast $B$ moves in $A$'s rest frame. Transform to that frame. In $A$'s rest frame, the Earth moves at speed $u$ (in the direction from $A$ to $B$), and $B$ moves at speed $u$ relative to the Earth in the same direction. By [[Thm - Relativistic Velocity Addition]], $B$'s speed relative to $A$ is the relativistic combination of $u$ with $u$:
> $$w = \frac{u + u}{1 + u\cdot u/c^2} = \frac{2u}{1 + u^2/c^2}.$$
> Check the ceiling: as $u \to c$, $w \to 2c/(1 + 1) = c$; and for $u < c$, $w < c$ (by the ceiling property $c - w = (c-u)^2 c/(c^2 + u^2) > 0$). So however close each ship's Earth-frame speed is to $c$, $B$ approaches $A$ at a relative speed strictly below $c$ — the correct, sub-light answer. For example, $u = 0.7c$ gives $w = 1.4c/1.49 \approx 0.94c$, not $1.4c$.

**Step 3: The inverse problem — measured $0.70c$ gives $u \approx 0.41c$.**

> [!note]- Derivation
> Ship $A$ measures $B$ approaching at $w = 0.70c$. Invert the relativistic formula. Let $\beta = u/c$:
> $$0.70 = \frac{2\beta}{1 + \beta^2} \ \Longrightarrow\ 0.70(1 + \beta^2) = 2\beta \ \Longrightarrow\ 0.70\beta^2 - 2\beta + 0.70 = 0.$$
> Solve the quadratic:
> $$\beta = \frac{2 \pm \sqrt{4 - 4(0.70)(0.70)}}{2(0.70)} = \frac{2 \pm \sqrt{4 - 1.96}}{1.4} = \frac{2 \pm \sqrt{2.04}}{1.4} = \frac{2 \pm 1.428}{1.4}.$$
> The two roots are $\beta = (2 + 1.428)/1.4 \approx 2.45$ (unphysical, $> 1$) and
> $$\beta = \frac{2 - 1.428}{1.4} \approx \frac{0.572}{1.4} \approx 0.41.$$
> So each ship moves at $u \approx 0.41c$ in the Earth frame. Contrast with the **naive Galilean halving** $u = w/2 = 0.35c$: the relativistic answer $0.41c$ is substantially larger, because the relativistic combination of two equal speeds is *less* than their Galilean sum, so to *produce* a given relative speed each ship must move *faster* than the naive estimate. The discrepancy ($0.41$ vs $0.35$) is the signature of the denominator $1 + \beta^2$ and grows as the speeds increase. (Sanity check: $2(0.41)/(1 + 0.41^2) = 0.82/1.168 \approx 0.70$. Correct.)

**Step 4: Rapidity route.**

> [!note]- Derivation
> In rapidity, $A$'s rest frame is reached from the Earth frame by a boost of rapidity $\varphi_u = \tanh^{-1}(u/c)$, and $B$ moves at rapidity $\varphi_u$ relative to the Earth (same magnitude, towards $A$). Collinear rapidities add ([[Def - Rapidity]]), so $B$'s rapidity relative to $A$ is
> $$\varphi_{\text{rel}} = \varphi_u + \varphi_u = 2\varphi_u,$$
> and its relative speed is $w = c\tanh(2\varphi_u)$. Using the double-angle identity $\tanh(2\varphi) = \dfrac{2\tanh\varphi}{1 + \tanh^2\varphi}$ with $\tanh\varphi_u = u/c$:
> $$w = c\cdot\frac{2(u/c)}{1 + (u/c)^2} = \frac{2u}{1 + u^2/c^2},$$
> matching Step 2. The inverse problem is even cleaner in rapidity: $\tanh^{-1}(0.70) \approx 0.867 = 2\varphi_u$, so $\varphi_u \approx 0.434$, and $u = c\tanh(0.434) \approx 0.41c$ — the same answer, obtained by halving a rapidity rather than solving a quadratic. This is the rapidity payoff: "half the relative speed" is *not* $w/2$ in velocity, but it *is* $\varphi_{\text{rel}}/2$ in rapidity.

> [!note]- Complete formal solution
> The Earth-frame closing speed is $u + u = 2u$, which may exceed $c$ (up to $2c$) without violating relativity, because it is the rate of change of a coordinate gap between two sub-light objects, not the speed of anything material. The relative speed of $B$ in $A$'s rest frame is the relativistic combination $w = 2u/(1 + u^2/c^2)$, always below $c$ (since $c - w = (c-u)^2 c/(c^2 + u^2) > 0$). Inverting for $w = 0.70c$: with $\beta = u/c$, $0.70\beta^2 - 2\beta + 0.70 = 0$, whose physical root is $\beta \approx 0.41$, so $u \approx 0.41c$ — larger than the naive Galilean $0.35c$. Via rapidity, $\varphi_{\text{rel}} = 2\varphi_u$ and $w = c\tanh(2\varphi_u)$, giving $\varphi_u = \tfrac12\tanh^{-1}(0.70) \approx 0.434$ and $u = c\tanh(0.434) \approx 0.41c$, confirming the quadratic. $\blacksquare$

---

# Key Takeaways

**Distinguish a coordinate closing rate from an object's velocity — only the latter is bounded by $c$.** The single conceptual hinge of this problem is that "the gap shrinks at $2u$" and "$B$ moves at $w$ in $A$'s frame" are *different quantities*, and only the second is a velocity in the sense the speed limit constrains. The Earth-frame closing speed is the time-derivative of a separation between two distinct objects, and it can legitimately reach $2c$ because no single thing moves that fast — there is no object, signal, or influence with that speed, so causality is untouched. The relative speed, by contrast, is an actual object's velocity in an actual inertial frame and *must* be below $c$. Examiners deploy this distinction precisely because the Galilean instinct conflates them; the diagnostic is to ask "is this the speed of *one thing in one frame*, or the rate of change of a *gap between two things*?" — the former obeys the ceiling, the latter need not. (The same point recurs for the phase velocity of a wave, which may exceed $c$ while carrying no information.)

**Invert the relativistic formula, not the Galilean one — the discrepancy is the whole point.** The inverse problem is designed to catch the student who, asked for the Earth-frame speed producing a $0.70c$ relative approach, simply halves to $0.35c$. The correct answer, $0.41c$, is materially larger, and the reason is structural: the relativistic combination of two equal speeds is *less* than their Galilean sum (the denominator $1 + \beta^2 > 1$ shrinks it), so to *achieve* a given relative speed each ship must exceed the naive half. Whenever a problem gives a combined or relative speed and asks for the constituents, set up and invert the *relativistic* law $w = 2u/(1+u^2/c^2)$ — typically a quadratic — and discard the unphysical root $\beta > 1$. The gap between the relativistic and Galilean answers widens as speeds approach $c$, and quoting the Galilean value is the canonical scoring error; the habit to build is to write the relativistic relation first and only then solve, never to reach for $w/2$.

**Rapidity converts "halving a relative speed" into halving an angle, dissolving the quadratic.** The cleanest solution to the inverse problem is not algebraic but a change of variable: because rapidities add, two ships symmetric about the Earth frame have relative rapidity $2\varphi_u$, so the Earth-frame rapidity is *exactly half* the relative rapidity — $\varphi_u = \tfrac12\tanh^{-1}(w/c)$ — and the quadratic never appears. This is the recurring lesson that rapidity is the natural coordinate for any boost composition: symmetric configurations, bisections, and iterations that are awkward in velocity become trivial linear operations in rapidity, exactly as bisecting an angle is trivial while "bisecting a slope" is not. The transferable move: whenever a problem involves *symmetry between two boosted frames* (equal-and-opposite velocities, a midpoint frame, the centre-of-momentum frame), pass to rapidity, exploit the additivity, and convert back at the end — see [[Ex - Addition of velocities and the speed-of-light ceiling]] for the same additivity driving the $N$-boost approach to $c$.
