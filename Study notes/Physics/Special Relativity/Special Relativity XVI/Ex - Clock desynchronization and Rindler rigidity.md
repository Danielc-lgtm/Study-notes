---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Clock Synchronization and Desynchronization in an Accelerated Frame"
  - "Def - Rindler Coordinates and the Accelerated Frame"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
tags: [physics, special-relativity]
---

# Problem Statement

A uniformly accelerated observer $\mathcal{O}$ of proper acceleration $a$ carries Rindler coordinates. A second observer $\mathcal{O}'$ is fixed at constant Rindler coordinate $x_0$ relative to $\mathcal{O}$. Working with $c = 1$ except where restored:

1. Show $\mathcal{O}'$ is itself uniformly accelerated, with proper acceleration $a' = a/(1 + ax_0)$, and that its proper time relates to $\mathcal{O}$'s by $t' = (1 + ax_0)t$.
2. Deduce that two ideal clocks fixed in the accelerated frame at $x_0 \neq 0$, synchronized at $t = 0$, *desynchronize* for $t > 0$. Contrast with an inertial frame, where comoving synchronized clocks stay synchronized.
3. Consider a rigid rod with ends at Rindler $x = 0$ and $x = x_0$. Show its rest length is $\ell_0 = |x_0|$ (constant, hence "rigid"), that the trailing end accelerates harder than the leading end, and that the rod cannot extend past $x_0 = -a^{-1}$ (the horizon).
4. Connect to **Bell's spaceship paradox**: two rockets that accelerate *identically* (same $a$, not the position-dependent $a'$) do not keep a fixed proper distance, and a string between them snaps.

**Recall:**

![[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame#Statement]]

A comoving observer fixed at Rindler coordinate $x_0$ has worldline $ct_* = (x_0 + a^{-1})\sinh(act)$, $x_* = (x_0 + a^{-1})\cosh(act) - a^{-1}$, obtained by setting $x = x_0$ in the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler transformation]]. The [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]] gives the proper acceleration of a hyperbola as the reciprocal of its centre-distance. **Born rigidity:** a body is rigid if the proper distance between neighbouring material points, measured in their common rest space, stays constant.

---

# Convergent Strategy

**Problem class.** A *relativistic-effect-in-the-accelerated-frame* problem focused on the position-dependence of clock rates and accelerations — the defining departure of an accelerated frame from an inertial one. The decisive move is to substitute $x = x_0$ into the Rindler transformation and recognise another hyperbola.

**Assumption pattern.** "Fixed in the accelerated frame" means constant Rindler coordinate $x_0$, and the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock-synchronization theorem]] then makes $\mathcal{O}'$ uniformly accelerated with $a' = a/(1+ax_0)$. The signpost for desynchronization is "two clocks at different positions": their rates differ by the lapse ratio $1 + ax_0$. The signpost for rigidity is "constant proper distance": that means constant $x_0$.

**Theorem routing.** The route is: $x = x_0$ in the Rindler transformation $\Rightarrow$ confocal hyperbola of centre-distance $x_0 + a^{-1}$ $\Rightarrow$ proper acceleration $a' = (x_0 + a^{-1})^{-1} = a/(1+ax_0)$ and proper time $t' = (1+ax_0)t$ ([[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock theorem]]); then the rest length $\ell_0 = |x_0|$ follows from the Rindler distance, and Bell's paradox from comparing $a'$ (rigid) with equal $a$ (non-rigid).

**Key decision point.** The crux is that "at rest with respect to each other" does *not* mean "physically equivalent" in an accelerated frame: comoving observers occupy different hyperbolae, feel different accelerations, and tick at different rates. The trap is the inertial intuition that comoving synchronized clocks stay synchronized — false here. For Bell's paradox, the decision is whether the rockets hold $a$ fixed (identical engines, non-rigid, string snaps) or $a'$ fixed (position-dependent, rigid, string survives); these are *different* motions.

---

# Legal Operations Used

1. **Replace a comoving observer by a uniformly accelerated one with $a' = a/(1+ax_0)$** (operation 3 from the topic page). The observer $\mathcal{O}'$ fixed at $x_0$ is itself uniformly accelerated, so every §16.1 result applies to it with $a\to a'$; the same Rindler horizon serves both.

2. **Read the Rindler metric off the coordinate transformation** (operation 4 from the topic page). The clock rate $\mathrm{d}\tau = (1+ax)\mathrm{d}t$, read from the Rindler metric $g_{tt} = (1+ax)^2$, is the position-dependent rate that drives the desynchronization.

3. **Use the rest space = simultaneity hypersurface identity for uniform acceleration** (operation 8 from the topic page). $\mathcal{O}$ and $\mathcal{O}'$ share the same rest spaces $\mathcal{E}_{u'}(t') = \mathcal{E}_u(t)$ (straight lines through the common centre $A$), which is what makes "the rod at one instant" and "simultaneous" well-defined for both ends.

---

# Hints

> [!note]- Hint 1
> Set $x = x_0$ in the Rindler transformation. The worldline $ct_* = (x_0 + a^{-1})\sinh(act)$, $x_* = (x_0 + a^{-1})\cosh(act) - a^{-1}$ is another hyperbola — confocal with $\mathcal{O}$'s, same centre $A = (0, -a^{-1})$. Its centre-distance is $x_0 + a^{-1}$, so its proper acceleration (the reciprocal) is $a' = 1/(x_0 + a^{-1}) = a/(1 + ax_0)$.

> [!note]- Hint 2
> For the proper time, integrate the line element along the constant-$x_0$ worldline: $c\,\mathrm{d}t' = \sqrt{c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2} = (1+ax_0)c\,\mathrm{d}t$ (the radical collapses by $\cosh^2 - \sinh^2 = 1$). So $t' = (1+ax_0)t$. Two clocks at $x_1\neq x_2$ then read $(1+ax_1)t \neq (1+ax_2)t$ for $t > 0$: they desynchronize.

> [!note]- Hint 3
> The rod's rest length is the proper distance between its ends in their common rest space: $\ell_0 = \|\overrightarrow{O(t)O'(t')}\| = \|x_0\,e_1(t)\| = |x_0|$, constant — hence "rigid". The trailing end ($x_0 < 0$) has the *larger* proper acceleration $a' = a/(1+ax_0) > a$, and $a'\to\infty$ as $x_0\to -a^{-1}$: no material point can sit at the horizon.

> [!note]- Hint 4
> Bell's paradox: if two rockets fire *identical* engines (same proper acceleration $a$ for both, not the position-dependent $a'$), their worldlines are *congruent* hyperbolae (same centre-distance $a^{-1}$, hence same shape but *shifted*), not confocal. The proper distance between them, measured in their instantaneous common rest space, *grows*, so a string tied between them stretches and snaps. Rigidity requires the trailing rocket to accelerate *harder* — exactly the $a'$ profile.

---

# Solution

The position-dependence of clock rate and acceleration is the whole story. Step 1 shows a comoving observer is uniformly accelerated with $a' = a/(1+ax_0)$ and ticks at rate $1+ax_0$. Step 2 reads off the desynchronization. Step 3 builds the rigid rod and finds its rest length, front-back asymmetry, and maximal extent. Step 4 resolves Bell's paradox. The non-obvious content is that comoving observers are *not* equivalent — different hyperbolae, different accelerations, different clock rates.

**Step 1: $\mathcal{O}'$ is uniformly accelerated, $a' = a/(1+ax_0)$, $t' = (1+ax_0)t$.**

> [!note]- Derivation
> Substituting $x = x_0$ (constant) into the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler transformation]] gives $\mathcal{O}'$'s worldline
> $$ct_* = (x_0 + a^{-1})\sinh(act), \qquad x_* = (x_0 + a^{-1})\cosh(act) - a^{-1}.$$
> Writing $a' := a/(1+ax_0)$, so $x_0 + a^{-1} = a'^{-1}$, and $x_*' := x_* - x_0$: then $a'x_*' + 1 = \cosh(act)$ and $a'ct_* = \sinh(act)$, whence $(a'x_*' + 1)^2 - (a'ct_*)^2 = 1$. This is a uniformly accelerated worldline of proper acceleration $a'$, confocal with $\mathcal{O}$'s (same centre $A = (0,-a^{-1})$, same asymptotes). So $\mathcal{O}'$ is itself uniformly accelerated with $a' = a/(1+ax_0)$, and shares $\mathcal{O}$'s [[Def - Rindler Horizon|Rindler horizon]].
>
> The proper time: differentiating the worldline and forming $c\,\mathrm{d}t' = \sqrt{c^2\mathrm{d}t_*^2 - \mathrm{d}x_*^2}$, the factor $(x_0 + a^{-1})ac$ comes out and the radical $\sqrt{\cosh^2 - \sinh^2} = 1$, leaving $c\,\mathrm{d}t' = (1 + ax_0)c\,\mathrm{d}t$. Since $x_0$ is constant, $t' = (1+ax_0)t$ (with $t' = 0$ at $t = 0$). Equivalently, this is the Rindler clock rate $\mathrm{d}\tau = (1+ax)\mathrm{d}t$ at $x = x_0$.

**Step 2: Fixed comoving clocks at $x_0 \neq 0$ desynchronize.**

> [!note]- Derivation
> Two ideal clocks fixed in $\mathcal{O}$'s accelerated frame at positions $x_1$ and $x_2$ are, by Step 1, uniformly accelerated observers whose proper times relate to $\mathcal{O}$'s by $t'_1 = (1 + ax_1)t$ and $t'_2 = (1+ax_2)t$. Synchronize them at $t = 0$ (all read zero). For $t > 0$,
> $$t'_1 - t'_2 = a(x_1 - x_2)\,t \neq 0 \quad\text{whenever } x_1\neq x_2.$$
> The clocks read *different* proper times even though they are at rest with respect to each other and were synchronized — they **desynchronize**, and the discrepancy grows linearly in $t$. This is the defining failure of an accelerated frame.
>
> Contrast the inertial case: two clocks at rest in an inertial frame, synchronized once, tick at the *same* rate forever ($1 + ax_0\to 1$ as $a\to 0$), so they stay synchronized. The difference is the position-dependent lapse $1 + ax$: in an accelerated frame the clock rate varies across the frame, and "the time now" is not a globally consistent quantity. A clock lower in the frame (smaller $x$, nearer the horizon) runs slow relative to one higher up — the [[Thm - Spectral Shift in an Accelerated Frame|same effect that redshifts light]] climbing through the frame.

**Step 3: Rest length $\ell_0 = |x_0|$, trailing end accelerates harder, no rigid extent past the horizon.**

> [!note]- Derivation
> A rod with ends fixed at Rindler $x = 0$ ($\mathcal{O}$) and $x = x_0$ ($\mathcal{O}'$), coplanar ($y_0 = z_0 = 0$), has, at any instant, both ends in their common rest space $\mathcal{E}_u(t) = \mathcal{E}_{u'}(t')$ (Step 1 gives $\mathcal{E}_{u'} = \mathcal{E}_u$). The rod's **rest length** is the proper distance between the ends in that common rest space:
> $$\ell_0 = \|\overrightarrow{O(t)O'(t')}\| = \|x_0\,e_1(t)\| = |x_0|,$$
> since $e_1(t)$ is a unit spacelike vector. This is *constant* (independent of $t$), which is precisely the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|Born-rigidity]] condition — the rod keeps a constant proper length, so it is **rigid**.
>
> But the two ends accelerate *differently*. The leading end ($\mathcal{O}$, at $x = 0$) has proper acceleration $a$; the trailing end ($\mathcal{O}'$, at $x_0 < 0$ if it trails) has $a' = a/(1 + ax_0) > a$ (since $1 + ax_0 < 1$). The trailing end accelerates *harder*. As $x_0\to -a^{-1}$, $a'\to +\infty$: the trailing end would need infinite proper acceleration. Therefore a Born-rigid rod can extend at most a distance $a^{-1}$ toward the horizon — no material point can be held rigidly at or beyond $x_0 = -a^{-1}$. (For the inertial observer, the rod is seen length-contracted, $\ell(t_*) = \ell_0\cdot(2+ax_0)/[\sqrt{(1+ax_0)^2 + (act_*)^2} + \sqrt{1+(act_*)^2}] \le \ell_0$, but its *rest* length stays $|x_0|$.)

**Step 4: Bell's spaceship paradox — identical accelerations snap a connecting string.**

> [!note]- Derivation
> Bell's paradox: two rockets, initially at rest a proper distance $L$ apart, fire *identical* engines, each maintaining the *same* proper acceleration $a$ (not the position-dependent $a'$). A delicate string is tied between them. Does the string snap?
>
> It does. With both rockets at proper acceleration $a$, their worldlines are *congruent* hyperbolae — same centre-distance $a^{-1}$, hence same shape, but *translated* by $L$ along $x_*$, with *different* centres ($A_1$ and $A_2 = A_1 + L\,e_1^*$). They are *not* confocal. Measured in their instantaneous common rest space, the proper distance between them *grows* with time: in the inertial frame they stay $L$ apart, but the inertial frame sees them length-contracted, so in their own (ever-faster) rest frame the distance is $\gamma L > L$ and increasing. The string, which can hold only its rest length $L$, is stretched beyond breaking and *snaps*.
>
> The resolution is exactly Step 3's front-back asymmetry: to keep a *fixed proper distance* (rigid motion), the trailing rocket must accelerate *harder* than the leading one, by the position-dependent $a' = a/(1+ax_0)$. Identical accelerations do *not* preserve proper distance; they preserve inertial-frame distance, which is a different and non-rigid condition. The paradox is "manufactured" by the inertial intuition that equal accelerations keep things rigid — false in relativity. The string survives only if the rockets follow the $a'$ profile, i.e. only if they are the two ends of a single Born-rigid body.

> [!note]- Complete formal solution
> Setting $x = x_0$ in the Rindler transformation gives $\mathcal{O}'$'s worldline, a confocal hyperbola of centre-distance $x_0 + a^{-1}$, so $\mathcal{O}'$ is uniformly accelerated with $a' = a/(1+ax_0)$, and integrating the line element gives $t' = (1+ax_0)t$. Two fixed comoving clocks at $x_1\neq x_2$ then read $(1+ax_1)t \neq (1+ax_2)t$ for $t>0$ — they desynchronize, unlike inertial comoving clocks which stay synchronized ($a\to 0$). A coplanar rod with ends at $0$ and $x_0$ has rest length $\ell_0 = \|x_0 e_1\| = |x_0|$, constant (rigid), with the trailing end at the larger acceleration $a' > a$ and $a'\to\infty$ as $x_0\to -a^{-1}$: no rigid extent past the horizon. Bell's paradox: two rockets at *equal* proper acceleration $a$ trace congruent (translated, not confocal) hyperbolae; their proper separation grows ($\gamma L$), so a connecting string snaps. Rigidity requires the position-dependent $a'$ — the trailing rocket must accelerate harder. $\blacksquare$

---

# Key Takeaways

**Comoving does not mean equivalent — different hyperbolae feel different accelerations and tick at different rates.** The single most important takeaway is that "at rest with respect to each other" carries none of the equivalence in an accelerated frame that it does in an inertial one. Two comoving observers occupy *different* hyperbolae at different distances from the common centre $A$, so the nearer one (smaller $x_0 + a^{-1}$, toward the horizon) feels a *larger* proper acceleration $a' = a/(1+ax_0)$ and ticks *faster*, while the farther one feels less and ticks slower. The trigger to recognise this: any problem with two objects "fixed in an accelerated frame" — a rocket of finite length, a clock on a shelf, the two ends of a ruler — requires applying the position-dependent $a'$ and clock rate, *not* a single common value. The diagnostic that catches the error is the inertial-intuition test: if your reasoning would give the same answer for two comoving inertial observers, you have probably forgotten the position-dependence.

**Clock desynchronization is the defining failure of an accelerated frame.** Two synchronized clocks at different positions in an accelerated frame drift apart linearly in time, $t'_1 - t'_2 = a(x_1 - x_2)t$, and this is *the* property that distinguishes an accelerated frame from an inertial one, where comoving synchronized clocks stay synchronized forever. The reusable principle: there is no globally consistent "now" in an accelerated frame, because the clock rate $1 + ax$ varies across it. The trigger: whenever you are tempted to speak of "the time" throughout an accelerated frame, stop — specify *which clock*, because they no longer agree. This is the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock-synchronization theorem]] in action, and read through the equivalence principle it is the gravitational time dilation: clocks deeper in a gravitational potential run slow, which is why GPS satellite clocks must be corrected.

**Rigidity requires the trailing edge to accelerate harder, and bounds the body's extent at the horizon.** The rest length $\ell_0 = |x_0|$ being constant is what makes the Rindler ruler rigid, but the price is that its ends accelerate *differently*: the trailing end at $a' = a/(1+ax_0) > a$, diverging as it approaches the horizon. The reusable insight is that a relativistic rigid body has a built-in front-back asymmetry and a *maximal length* — it can extend no farther than $a^{-1}$ toward the horizon, because beyond that the required acceleration is infinite. The trigger: any "rigid accelerating body" problem must use the position-dependent acceleration profile, and any body longer than $\sim a^{-1}$ cannot be held rigid. This is the finite-extent form of [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|Born rigidity]], and the Herglotz–Noether theorem sharpens it: a Born-rigid body in special relativity has very few degrees of freedom.

**Bell's paradox is resolved by distinguishing "equal acceleration" from "rigid".** The paradox — that a string between two identically-accelerating rockets snaps — dissolves once you see that *equal proper acceleration* and *constant proper separation* are different, incompatible conditions. Equal $a$ for both rockets gives congruent, translated hyperbolae whose proper separation grows ($\gamma L$); constant proper separation (rigidity) requires the position-dependent $a'$, with the trailing rocket accelerating harder. The trigger to avoid the trap: when a problem specifies how rockets accelerate, ask whether they hold *acceleration* fixed or *proper distance* fixed — these select different motions, and the string's fate depends on which. The general lesson, recurring throughout the chapter, is that the inertial-frame quantity (here, coordinate separation) and the rest-frame quantity (proper separation) are *different things* in accelerated motion, and conflating them manufactures paradoxes.

This exercise applies the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock-synchronization theorem]] and pairs with [[Ex - Redshift in an accelerated frame and the Einstein elevator]] (the optical readout of the same clock-rate difference).
