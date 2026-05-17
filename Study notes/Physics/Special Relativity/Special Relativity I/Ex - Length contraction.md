---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, special-relativity]
---

# Problem Statement

A rigid rod of length $L_0$ lies at rest along the $x'$-axis of frame $S'$, with its ends at $x' = 0$ and $x' = L_0$. Frame $S'$ moves at velocity $v$ along the $x$-axis of frame $S$. Working with $c = 1$:

1. Write the worldlines of the two ends of the rod in $S$.
2. Show that, when its length is measured in $S$ — meaning the positions of *both ends* are taken at the same time $t$ — the rod has length $L = L_0/\gamma = L_0\sqrt{1-v^2}$.
3. **The ladder-and-barn "paradox":** a ladder of rest length $2L$ is run at high speed through a barn of rest length $L$. The barn frame says the ladder is contracted and fits inside; the ladder frame says the barn is contracted and the ladder cannot possibly fit. Resolve the contradiction.

**Recall:**

The computation rests on the Lorentz transformation.

![[Def - The Lorentz Transformation#The Definition]]

The **proper length** $L_0$ of a rod is its length in its own rest frame — the frame in which the rod is not moving. A length measurement in any frame means: record the positions of the two ends *simultaneously in that frame*, and take the difference. The word "simultaneously" is the crux, because by [[Def - Inertial Frame and the Postulates of Special Relativity|the relativity of simultaneity]] it means different things in different frames.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-relativistic-effect* problem, and parts 2–3 are also a *resolve-a-paradox* problem. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] says: start in the rest frame, boost out, and watch the word "simultaneously".

**Assumption pattern.** A rod of known *rest* length is given — the signpost to begin in its rest frame $S'$, where its ends sit at fixed coordinates. The measurement is then demanded in the moving frame $S$.

**Theorem routing.** Write the ends' worldlines in $S'$ (constant $x'$), Lorentz-transform them into $S$, then impose the *$S$-simultaneity* condition $t = \text{const}$ on both worldlines and subtract. The factor $\gamma$ drops out of the algebra.

**Key decision point.** The non-obvious step is recognising that "measure the length in $S$" forces $t$ equal for both ends *in $S$*, which is **not** $t'$ equal in $S'$. The two ends, taken at equal $t$, are *not* simultaneous in $S'$. Contraction is entirely a consequence of this mismatch of simultaneity — that is also the key to the paradox.

---

# Legal Operations Used

1. **Work in the rest frame, then boost out.** In $S'$ the rod's ends are simply $x' = 0$ and $x' = L_0$ for all $t'$; this is the easy description to start from.

2. **Apply the Lorentz transformation** to carry the ends' worldlines from $S'$ to $S$.

3. **Use length contraction** — but here we *derive* it rather than quote it, by imposing the $S$-simultaneity condition.

4. **Track which frame's simultaneity is in play.** Resolving the paradox is entirely the operation of asking, for each frame, "the two ends — at the same time *in which frame*?"

---

# Hints

> [!note]- Hint 1
> In $S'$ the rod is at rest, so its ends have worldlines $x' = 0$ and $x' = L_0$, valid for every $t'$. Lorentz-transform each worldline into $S$ using $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$.

> [!note]- Hint 2
> To measure the rod in $S$, you need both ends at the *same* $S$-time $t$. Pick $t = 0$. The end at $x'=0$ is then at $x = 0$. For the other end, you must find which event on its worldline has $t = 0$ — that means a particular value of $t'$, which is *not* zero. Solve $t = \gamma(t' + vL_0) = 0$ for $t'$, then substitute into $x = \gamma(L_0 + vt')$.

> [!note]- Hint 3
> For the paradox: "the ladder fits in the barn" means "both ends of the ladder are inside the barn *at the same time*". In the barn frame, that simultaneity makes the (contracted) ladder fit. In the ladder frame, the front of the ladder hits the far wall *before* — in that frame's time-ordering — the back of the ladder clears the door. Both frames are right; they disagree about *simultaneity*, not about any single event.

---

# Solution

The rod is shortest in any frame where it moves, and the entire effect comes from the relativity of simultaneity: measuring "both ends at once" in $S$ catches the rod's ends at two events that are *not* simultaneous in the rod's own frame $S'$.

**Step 1: The worldlines of the ends, in $S$.**

> [!note]- Derivation
> In $S'$ the rod is at rest with ends at $x' = 0$ (the "back") and $x' = L_0$ (the "front"), for all $t'$. Apply the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$.
>
> *Back end* ($x' = 0$): $\;x = \gamma v t'$, $\;t = \gamma t'$. Eliminating $t'$: $x = vt$. The back end moves at velocity $v$ in $S$, as expected.
>
> *Front end* ($x' = L_0$): $\;x = \gamma(L_0 + vt')$, $\;t = \gamma(t' + vL_0)$. Eliminating $t'$: from the second equation $t' = t/\gamma - vL_0$, and substituting, $x = \gamma L_0 + \gamma v(t/\gamma - vL_0) = \gamma L_0 - \gamma v^2 L_0 + vt = \gamma L_0(1-v^2) + vt = L_0/\gamma + vt$.
>
> So in $S$ the two worldlines are
> $$\text{back: } x = vt, \qquad \text{front: } x = \frac{L_0}{\gamma} + vt.$$

**Step 2: The measured length is $L = L_0/\gamma$.**

> [!note]- Derivation
> To measure the rod in $S$ we record the positions of *both ends at the same $S$-time*. Take $t = 0$ (any $t$ gives the same answer, since both worldlines move at $v$). From Step 1:
> $$x_{\text{back}}(0) = 0, \qquad x_{\text{front}}(0) = \frac{L_0}{\gamma}.$$
> The length measured in $S$ is the difference:
> $$L = x_{\text{front}}(0) - x_{\text{back}}(0) = \frac{L_0}{\gamma} = L_0\sqrt{1 - v^2}.$$
> Since $\gamma \ge 1$, we have $L \le L_0$: **the moving rod is shorter than its rest length**, contracted by the factor $\gamma$.
>
> The crucial subtlety: the two measurement events — back end at $(t,x)=(0,0)$ and front end at $(t,x)=(0, L_0/\gamma)$ — are simultaneous in $S$ but *not* in $S'$. The front-end event has $t' = t/\gamma - vL_0 = -vL_0 \ne 0$, while the back-end event has $t' = 0$. Measured "all at once" in $S$, the rod's ends are caught at two different $S'$-times. Contraction is the visible consequence of this mismatch — it is not a physical squashing of the rod.

**Step 3: The ladder-and-barn paradox resolved.**

> [!note]- Derivation
> A ladder of rest length $2L$ moves at speed $v$ (with $\gamma > 2$) through a barn of rest length $L$.
>
> *Barn frame.* The ladder moves, so it is contracted to $2L/\gamma < L$. There is an instant — in barn-frame time — at which the back of the ladder is inside the door and the front has not yet reached the far wall. At that instant the whole ladder is inside the barn. The barn frame says: it fits.
>
> *Ladder frame.* The barn moves, so it is contracted to $L/\gamma$, while the ladder has its full rest length $2L$. There is no instant — in ladder-frame time — at which both ends of the ladder are within the barn. The ladder frame says: it does not fit.
>
> *The resolution.* "Fits inside the barn" means "the back end is in the door **at the same time as** the front end is short of the far wall". The phrase "at the same time" is frame-dependent. Consider the two events:
> - $A$: the front of the ladder reaches the far wall;
> - $B$: the back of the ladder enters the door.
>
> In the barn frame, $B$ happens *before* $A$ (back is in before front hits) — so there is a moment with the whole ladder enclosed. In the ladder frame, $A$ happens *before* $B$ (front hits the wall before the back clears the door) — so there is never a moment with the whole ladder enclosed. Events $A$ and $B$ are **spacelike separated** (compute: their interval is negative), and the time-ordering of spacelike-separated events is frame-dependent ([[Def - Classification of Four-Vectors]]). Neither frame is wrong. They are not disagreeing about any physical event — both agree the front reaches the wall, both agree the back enters the door — they disagree only about the *order*, hence about the meaning of "fits". The paradox was manufactured by assuming "fits" has a frame-independent meaning. It does not.

> [!note]- Complete formal solution
> In $S'$ the rod's ends are $x' = 0$ and $x' = L_0$. Transforming to $S$ via $x = \gamma(x'+vt')$, $t = \gamma(t'+vx')$: the back end ($x'=0$) has worldline $x = vt$; the front end ($x'=L_0$) has worldline $x = L_0/\gamma + vt$ (eliminate $t'$ using $\gamma^2(1-v^2)=1$). Measuring in $S$ means taking both ends at one $S$-time, say $t=0$: the ends are at $x=0$ and $x = L_0/\gamma$, so $L = L_0/\gamma = L_0\sqrt{1-v^2} \le L_0$. The two measurement events have $S'$-times $t' = 0$ and $t' = -vL_0$ respectively — not simultaneous in $S'$ — which is the origin of the contraction. For the ladder and barn: each frame contracts the *other* object; "the ladder fits" requires the events "front reaches wall" and "back enters door" to be ordered a particular way, but these events are spacelike separated and their order is frame-dependent, so the two frames consistently disagree about whether the ladder fits. $\blacksquare$

---

# Key Takeaways

**Length contraction is a statement about simultaneity, not about forces.** Nothing pushes on the rod; no stress squashes it. The rod is contracted in $S$ purely because measuring "the length" requires locating both ends *at the same time*, and "the same time" in $S$ catches the rod's ends at two events that the rod's own frame $S'$ regards as occurring at *different* times. Run the rod's worldlines forward and the front end is always $L_0/\gamma$ ahead of the back in $S$-simultaneity but $L_0$ ahead in $S'$-simultaneity. The lesson generalises to every relativistic effect: before you can say what "length" or "duration" or "now" means, you must name the frame, because the simultaneity slicing is part of the measurement. Whenever a relativity problem produces a paradox, the first suspect is an unstated, frame-independent reading of one of these words.

**Each frame contracts the *other* object — and that is consistent, not contradictory.** In the barn problem the barn frame contracts the ladder and the ladder frame contracts the barn. A first reaction is that this cannot both be true. But it is: each frame sees the *other* one moving, and a moving object is the one that contracts. There is no frame that sees both contracted, and no frame that sees neither. The apparent contradiction dissolves once you see that "fits inside" is not a property of the configuration but a property *relative to a simultaneity slicing* — it asks about the time-order of two spacelike-separated events, and that order is frame-dependent. The reusable pattern: when two frames seem to assert opposite physical facts, check whether the "fact" is secretly a statement about the order or simultaneity of spacelike-separated events. If so, both frames are right and the contradiction is an artefact of language.

**The proper length is the maximum, and the rest frame is where measurement is easy.** The rest frame $S'$ is special: there the rod is not moving, so its two ends can be located at *any* times whatsoever and still give the correct length $L_0$ — simultaneity does not matter for a stationary object. This is why the proper length is well-defined and frame-independent, and why it is the largest length any frame assigns. The strategy "describe the object in its rest frame, then boost out" works because the rest frame removes the simultaneity subtlety; you reintroduce it, in controlled form, with a single Lorentz transformation. This is the exact analogue of the time-dilation strategy ([[Ex - Time dilation]]), where the rest frame of the *clock* is where the proper time lives.
