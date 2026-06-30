---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Rindler Horizon"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

A uniformly accelerated observer $\mathcal{O}$ of proper acceleration $a$ has worldline the hyperbola $(ax_* + 1)^2 - (act_*)^2 = 1$ in the inertial coordinates $(ct_*, x_*, y_*, z_*)$ of the reference inertial observer $\mathcal{O}_*$, with centre $A = (ct_*, x_*) = (0, -a^{-1})$ and asymptotes $\Delta_{1,2}: ct_* = \pm(x_* + a^{-1})$. Working with $c = 1$:

1. A light flash is emitted at the event $(ct_*, x_*) = (0, b)$ on the $x_*$-axis, travelling toward $\mathcal{O}$ (in the $+x_*$ direction is "away"; toward $\mathcal{O}$ means appropriate sign). Show by drawing the $45^\circ$ light ray and the hyperbola that, for $b > a^{-1}$, the flash *never reaches* $\mathcal{O}$; for $b < a^{-1}$ (and on the accessible side) it does.
2. Generalise: for an emitter at an arbitrary event $(ct_*^{\mathrm{em}}, x_*^{\mathrm{em}})$, derive the condition under which a light ray from it reaches $\mathcal{O}$. Show the boundary is the hyperplane $\mathcal{H}: ct_* = x_* + a^{-1}$ — the **Rindler horizon**.
3. Prove that $\mathcal{H}$ is a *null hyperplane*: find a normal vector and show it is also tangent to $\mathcal{H}$, hence null.
4. Interpret the result as the flat-spacetime model of a causal horizon, and explain Tong's remark that "if an accelerated observer wants to see behind the horizon, he just stops accelerating."

**Recall:**

![[Def - Rindler Horizon#The Definition]]

The worldline of $\mathcal{O}$ is the hyperbola of [[Thm - Worldline of a Uniformly Accelerated Observer|the worldline theorem]], hugging its asymptote $\Delta_1: ct_* = x_* + a^{-1}$ in the infinite future as $\mathcal{O}$'s speed tends to $c$. Light rays are null geodesics — straight $45^\circ$ lines in the inertial coordinates, $ct_* = \pm(x_* - b) + \mathrm{const}$. A vector $N$ is [[Def - Classification of Four-Vectors|null]] if $N\cdot N = 0$; a hyperplane is *null* if the metric induced on it is degenerate, equivalently if its normal is also tangent to it.

---

# Convergent Strategy

**Problem class.** A *causal-verdict* problem, the second class in the [[Special Relativity XVI — Accelerated Observers#Problem-Solving Strategy|topic strategy]]: decide whether an event can send a signal to the accelerated observer, and locate the horizon. The decisive tool is the light cone read in the inertial frame, where photon worldlines are straight $45^\circ$ lines.

**Assumption pattern.** The hyperbola $\mathcal{L}_0$ hugs its asymptote $\Delta_1$ without crossing it. The signpost is that a light ray running *parallel to or below* $\Delta_1$ can never catch a curve that stays forever above $\Delta_1$. The assumption "constant proper acceleration" enters only through the shape of the hyperbola — specifically through its asymptote, the limiting $45^\circ$ line.

**Theorem routing.** The route is: write the emission event in inertial coordinates $\Rightarrow$ write the null line from it $\Rightarrow$ impose that the null line meets the hyperbola (solve for the proper time of the meeting) $\Rightarrow$ find the locus where solutions cease to exist. That locus is the [[Def - Rindler Horizon|Rindler horizon]]. The intersection condition reduces, via $\cosh \ge 1$, to a sign condition on $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} + a^{-1}$.

**Key decision point.** The crux is realising that a horizon is *not* a place where light is physically blocked. Nothing stops the light; it travels at $c$ in a straight line forever, but the accelerating observer's worldline simply outruns it, because the gap measured along $\mathcal{O}$'s ever-tilting rest spaces never closes. The horizon is a feature of the *limit* of $\mathcal{O}$'s worldline (its asymptote), not of any finite part of it — and it dissolves the instant $\mathcal{O}$ stops accelerating.

---

# Legal Operations Used

1. **Integrate constant proper acceleration into a hyperbola** (operation 1 from the topic page). The hyperbola and its asymptote $\Delta_1$ are taken from the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]]; the asymptote, promoted to a hyperplane, is the horizon.

2. **Choose the tangent inertial observer and compute there** (operation 2 from the topic page). Working in the inertial coordinates of $\mathcal{O}_*$ makes light rays straight $45^\circ$ lines, so the intersection condition is elementary algebra. By stationarity, taking the emission at $t = 0$ (equivalently $M \in \mathcal{E}_u(0)$) loses no generality.

3. **Classify a separation or a four-vector by the sign of its norm** (operation 9 from the topic page). To show $\mathcal{H}$ is null, compute the norm of its normal vector $e_0^* + e_1^*$ and find it zero — the [[Def - Classification of Four-Vectors|null]] case.

---

# Hints

> [!note]- Hint 1
> Draw the inertial diagram: the hyperbola opening rightward, its asymptote $\Delta_1: ct_* = x_* + a^{-1}$ running at $45^\circ$ up and to the right. A light flash from $(0, b)$ travelling toward $\mathcal{O}$ is a $45^\circ$ line. Compare its line to $\Delta_1$: if the flash starts to the left of where $\Delta_1$ crosses the $x_*$-axis (i.e. $b < a^{-1}$... careful with the geometry), the ray crosses into the region the hyperbola sweeps; if it starts to the right, it stays below the hyperbola forever.

> [!note]- Hint 2
> For a general emitter $M$, write $M \in \mathcal{E}_u(0)$ (using stationarity, so $ct_*^{\mathrm{em}} = 0$ first), with inertial coordinates $(0, x_*^{\mathrm{em}}, y_*^{\mathrm{em}}, z_*^{\mathrm{em}})$. A photon reaches $\mathcal{O}$ iff the vector $\overrightarrow{MO(t)}$ is null for some proper time $t$. Compute $\overrightarrow{MO(t)}$ using the worldline $O(t) = (a^{-1}\sinh(act), a^{-1}[\cosh(act)-1], 0, 0)$ and set its norm to zero.

> [!note]- Hint 3
> The null condition $\overrightarrow{MO(t)}\cdot\overrightarrow{MO(t)} = 0$ simplifies to $2(ax_*^{\mathrm{em}} + 1)\cosh(act) = 1 + a^2[(x_*^{\mathrm{em}} + a^{-1})^2 + (y_*^{\mathrm{em}})^2 + (z_*^{\mathrm{em}})^2]$. Since $\cosh(act) \ge 1$, a solution $t$ exists iff the right side is at least $2(ax_*^{\mathrm{em}}+1)$ AND $ax_*^{\mathrm{em}} + 1 > 0$. The decisive factor is the sign of $ax_*^{\mathrm{em}} + 1$: if $x_*^{\mathrm{em}} \le -a^{-1}$, no solution.

> [!note]- Hint 4
> Restoring the time of emission (the general $ct_*^{\mathrm{em}} \neq 0$ case follows by boosting along the worldline), the condition $x_*^{\mathrm{em}} > -a^{-1}$ generalises to $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$. The boundary is $ct_* = x_* + a^{-1}$, which is $\Delta_1$ promoted to a hyperplane. For the null character: the gradient of $x_* - ct_* + a^{-1}$ gives a normal $\propto e_0^* + e_1^*$; compute its norm.

---

# Solution

The horizon is the asymptote of the worldline, promoted to a hyperplane. Step 1 settles the special case $ct_*^{\mathrm{em}} = 0$ by drawing the light ray against the hyperbola. Step 2 does the general computation: the condition for a null ray from $M$ to meet the hyperbola reduces, because $\cosh \ge 1$, to a sign condition that places the boundary at $\mathcal{H}: ct_* = x_* + a^{-1}$. Step 3 shows $\mathcal{H}$ is null by exhibiting a normal that is also tangent. Step 4 draws the conceptual moral. The non-obvious step is in Step 2, where the $\cosh \ge 1$ bound converts "a solution exists" into a clean inequality.

**Step 1: A flash from $(0, b)$ reaches $\mathcal{O}$ iff $b > -a^{-1}$ (accessible side); for the original framing, the boundary is at $b = -a^{-1}$.**

> [!note]- Derivation
> Place the emission at $(ct_*, x_*) = (0, b)$. The observer's worldline passes through its "top" $O(0) = (0, 0)$ and curves up and to the right toward $\Delta_1$. A light ray from $(0, b)$ that can reach $\mathcal{O}$ must travel in the $+x_*$ direction if $b < 0$ (the emitter is behind $\mathcal{O}$) — the ray is $ct_* = x_* - b$. This ray is *parallel* to the asymptote $\Delta_1: ct_* = x_* + a^{-1}$, offset by $b + a^{-1}$. If $b > -a^{-1}$, the ray lies *below and to the right* of $\Delta_1$ (closer to the hyperbola), and since the hyperbola descends from $\Delta_1$ to its top and back, the ray crosses it: the flash reaches $\mathcal{O}$. If $b < -a^{-1}$, the ray lies *above* $\Delta_1$, on the far side from the hyperbola, which forever stays below $\Delta_1$ on that side — the ray never meets it, and the flash never reaches $\mathcal{O}$. The boundary case $b = -a^{-1}$ is the asymptote itself. (For an emitter ahead of $\mathcal{O}$, $b > 0$, the relevant ray travels in $-x_*$ and always reaches $\mathcal{O}$, who is heading toward larger $x_*$.) So in the plane, the dividing point on the $x_*$-axis is $x_* = -a^{-1}$, the foot of the asymptote.

**Step 2: A general emitter reaches $\mathcal{O}$ iff $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$; the boundary is $\mathcal{H}: ct_* = x_* + a^{-1}$.**

> [!note]- Derivation
> By stationarity, take the emission event $M$ on $\mathcal{E}_u(0)$, so $ct_*^{\mathrm{em}} = 0$ and $M = (0, x_*^{\mathrm{em}}, y_*^{\mathrm{em}}, z_*^{\mathrm{em}})$. A photon reaches $\mathcal{O}$ iff there is a future-directed null geodesic from $M$ to some $O(t)$ on the worldline, i.e. iff $\overrightarrow{MO(t)}$ is null for some $t \ge 0$. With $O(t) = (a^{-1}\sinh(act), a^{-1}[\cosh(act) - 1], 0, 0)$,
> $$\overrightarrow{MO(t)} = a^{-1}\sinh(act)\,e_0^* + [a^{-1}\cosh(act) - a^{-1} - x_*^{\mathrm{em}}]\,e_1^* - y_*^{\mathrm{em}}e_2^* - z_*^{\mathrm{em}}e_3^*.$$
> Setting the norm to zero (mostly-minus: $+(\cdot)^2$ for the $e_0^*$ component, $-(\cdot)^2$ for the spatial ones) and simplifying with $\cosh^2 - \sinh^2 = 1$:
> $$2(ax_*^{\mathrm{em}} + 1)\cosh(act) = 1 + a^2\big[(x_*^{\mathrm{em}} + a^{-1})^2 + (y_*^{\mathrm{em}})^2 + (z_*^{\mathrm{em}})^2\big].$$
> The right side is $\ge 1 > 0$. Two cases:
> - If $ax_*^{\mathrm{em}} + 1 \le 0$ (i.e. $x_*^{\mathrm{em}} \le -a^{-1}$): the left side is $\le 0$ while the right is $> 0$, so there is *no solution* — the light ray never reaches $\mathcal{O}$.
> - If $ax_*^{\mathrm{em}} + 1 > 0$: the equation reads $\cosh(act) = [1 + a^2(\cdots)]/[2(ax_*^{\mathrm{em}}+1)] \ge 1$ (the right side exceeds $1$ since the numerator minus denominator is a sum of squares), so a *unique* $t \ge 0$ exists — the ray reaches $\mathcal{O}$.
>
> Hence the condition is $x_*^{\mathrm{em}} > -a^{-1}$ for emission at $t = 0$. Restoring a general emission time: reasoning on the intersection of light cones with the slices $t_* = \alpha \neq 0$ (or boosting along the worldline, which maps the condition covariantly), the condition becomes $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$. The boundary — the events that can *just barely* fail to reach $\mathcal{O}$ — is the hyperplane
> $$\mathcal{H}:\qquad ct_* = x_* + a^{-1},$$
> which is $\Delta_1$ extended over all $y_*, z_*$. This is the **Rindler horizon**.

**Step 3: $\mathcal{H}$ is a null hyperplane: its normal $e_0^* + e_1^*$ is itself tangent to $\mathcal{H}$, hence null.**

> [!note]- Derivation
> Write $\mathcal{H}$ as the level set $f = 0$ of $f(ct_*, x_*) = x_* - ct_* + a^{-1}$. A normal to $\mathcal{H}$ is the metric-raised gradient of $f$. The gradient components are $\partial_\mu f = (-1, 1, 0, 0)$ (with $x^0 = ct_*$); raising with $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$ gives the normal vector $N$ with components $N^\mu = \eta^{\mu\nu}\partial_\nu f = (-1, -1, 0, 0)$, i.e. $N = -(e_0^* + e_1^*)$, so up to sign the normal is $N = e_0^* + e_1^*$. Its norm is
> $$N\cdot N = (e_0^* + e_1^*)\cdot(e_0^* + e_1^*) = e_0^*\cdot e_0^* + 2e_0^*\cdot e_1^* + e_1^*\cdot e_1^* = 1 + 0 - 1 = 0.$$
> So $N$ is **null**. A null normal is orthogonal to itself, hence *tangent* to the hyperplane it is normal to: $\mathcal{H}$ contains its own normal direction $e_0^* + e_1^*$ (indeed $e_0^* + e_1^*$ points along $\Delta_1$, which lies in $\mathcal{H}$). Therefore the metric induced on $\mathcal{H}$ is *degenerate* — the vector $N$ in $\mathcal{H}$ is orthogonal to all of $\mathcal{H}$ including itself — which is the definition of a **null hyperplane**, the three-dimensional analogue of a null line. This is exactly the structure of a black-hole horizon, which is also a null hypersurface.

**Step 4: The horizon is a causal boundary, observer-dependent, dissolving if $\mathcal{O}$ coasts.**

> [!note]- Derivation
> Nothing physical blocks the hidden light. There is no obstacle, no absorber, no curvature — Minkowski space is perfectly flat and smooth across $\mathcal{H}$. The light is emitted, travels at $c$ in a straight line, and simply never arrives, purely because $\mathcal{O}$ keeps accelerating away: $\mathcal{O}$'s worldline asymptotes to $\Delta_1$, so a ray running parallel to or above $\Delta_1$ is forever outrun. The hidden region — events with $x_* - ct_* \le -a^{-1}$, beyond $\mathcal{H}$ — is the flat-spacetime model of the interior of a black hole, and $\mathcal{H}$ is the model of the event horizon.
>
> The decisive *disanalogy* is observer-dependence. The horizon exists only because $\mathcal{O}$ accelerates eternally. The instant $\mathcal{O}$ stops accelerating — levels off to constant velocity — the worldline becomes a straight line that the previously-hidden light immediately catches, and the hidden region becomes visible. This is Tong's gloss: *if an accelerated observer wants to see behind the horizon, he just stops accelerating; an observer who wants to see behind a black hole's horizon must be considerably braver.* The Rindler horizon is the toy model — the same null-surface geometry, the same hidden region — but it is a property of the *observer's choice*, whereas a black-hole event horizon is intrinsic to the spacetime, the same for everyone. The proper acceleration $a$ that locates $\mathcal{H}$ (a distance $a^{-1}$ behind $\mathcal{O}$) corresponds to the surface gravity of the black hole.

> [!note]- Complete formal solution
> A photon from emission event $M$ reaches $\mathcal{O}$ iff $\overrightarrow{MO(t)}$ is null for some $t \ge 0$. Taking $M \in \mathcal{E}_u(0)$ (stationarity, so $ct_*^{\mathrm{em}} = 0$) and $O(t) = (a^{-1}\sinh act, a^{-1}[\cosh act - 1], 0, 0)$, the null condition reduces to $2(ax_*^{\mathrm{em}}+1)\cosh(act) = 1 + a^2[(x_*^{\mathrm{em}}+a^{-1})^2 + (y_*^{\mathrm{em}})^2 + (z_*^{\mathrm{em}})^2]$. The right side is $\ge 1$; since $\cosh \ge 1$, a solution exists iff $ax_*^{\mathrm{em}} + 1 > 0$, i.e. $x_*^{\mathrm{em}} > -a^{-1}$. Generalising the emission time gives $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$; the boundary is the hyperplane $\mathcal{H}: ct_* = x_* + a^{-1}$, the asymptote $\Delta_1$ extended over $y_*, z_*$ — the Rindler horizon. The gradient of $x_* - ct_* + a^{-1}$ raises to the normal $N = e_0^* + e_1^*$, with $N\cdot N = 1 - 1 = 0$: $N$ is null and lies in $\mathcal{H}$, so $\mathcal{H}$ is a null hyperplane. Physically, no obstacle blocks the hidden light; $\mathcal{O}$'s eternal acceleration outruns it, and the horizon — observer-dependent, dissolving if $\mathcal{O}$ coasts — is the flat-spacetime model of a black-hole event horizon, with $a$ playing the role of surface gravity. $\blacksquare$

---

# Key Takeaways

**A horizon is where geometry outruns light, not where light is blocked.** The single most important conceptual takeaway is that the Rindler horizon involves no physical barrier whatsoever: the hidden light travels freely at $c$ through perfectly flat, smooth spacetime, and is simply never overtaken by the accelerating observer. This reframes "horizon" from a wall to a *causal boundary* — the limit of the region from which signals can ever arrive. The trigger to recognise the structure elsewhere: whenever a worldline asymptotes to a null line (its speed tending to $c$), there is a region of spacetime it can never see, bounded by that asymptote promoted to a hyperplane. The same logic, applied to light trying to *escape* a black hole rather than *reach* an accelerated observer, gives the event horizon. The defining test is always the same — solve for whether a null ray can connect the two worldlines, and find the locus where solutions cease to exist.

**Work in the inertial frame, where light is straight and the algebra is trivial.** The whole computation is easy because in $\mathcal{O}_*$'s inertial coordinates, photon worldlines are straight $45^\circ$ lines and the hyperbola is explicit. The reusable principle — operation 2 of the topic page — is that an accelerated-frame causal question becomes elementary the moment you express it in a global inertial frame: the curved Rindler grid is for *interpreting* the answer, not for *computing* it. The diagnostic: any "can $A$ reach $B$" question in an accelerated frame should be translated to inertial coordinates, where it becomes "does this $45^\circ$ line meet that curve". The $\cosh(act) \ge 1$ bound that converts "a solution exists" into a sharp inequality is the recurring trick — the range of the hyperbolic cosine is what draws the boundary.

**The null character of the horizon is what makes it a horizon.** Showing $\mathcal{H}$ is a null hyperplane — normal $e_0^* + e_1^*$ equal to its own tangent, norm zero — is not a technicality but the structural heart of the matter. A null hypersurface is one whose induced metric is degenerate, and this is precisely the property shared by every causal horizon in physics: the Rindler horizon, the black-hole event horizon, the cosmological horizon. The reusable diagnostic: to test whether a candidate boundary is a genuine horizon, compute the norm of its normal — if the normal is null (and tangent), the surface is null and a horizon; if the normal is timelike or spacelike, it is an ordinary spacelike or timelike slice. This single computation, $N\cdot N = 0$, certifies the horizon, and it is the flat-spacetime rehearsal for the same check on the Schwarzschild metric at $r = 2GM/c^2$.

**Observer-dependence distinguishes the toy from the real thing.** The Rindler horizon dissolves the instant $\mathcal{O}$ stops accelerating, which is the crucial difference from a black-hole event horizon that no choice can remove. Holding this distinction prevents the standard error of treating the Rindler horizon as a real, intrinsic feature of spacetime: it is a feature of *one observer's eternal acceleration*. Yet the analogy is precise enough to be the standard pedagogical and computational bridge to black holes — the near-horizon geometry of Schwarzschild *is* Rindler, the proper acceleration corresponds to surface gravity, and the [[Def - Rindler Horizon|Unruh effect]] derived on the Rindler horizon is the template for Hawking radiation. The lesson generalises: a horizon's *local* physics (its null geometry, its temperature) can be universal even when its *global* status (observer-dependent versus intrinsic) is not.

This exercise builds on [[Ex - Hyperbolic motion under constant proper acceleration]] (the hyperbola and its asymptote) and connects to [[Ex - The relativistic rocket and a constant-g voyage]] (Tong's "doesn't think he's got far" remark is the horizon's signature on the perceived distance).
