---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
  - "Thm - Uniqueness of the Lorentz Transformation from the Postulates"
tags: [physics, special-relativity]
---

# Problem Statement

Derive the Lorentz boost along the $x$-axis from first principles, assuming only that $S$ and $S'$ are inertial frames with $S'$ moving at velocity $v$, origins coinciding at $t = t' = 0$, and the two [[Def - Inertial Frame and the Postulates of Special Relativity|postulates of special relativity]]. Carry out every step explicitly (work with $c$ general):

1. Argue that the transformation $x' = f(x,t)$, $t' = g(x,t)$ must be **linear**, and write $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.
2. Use the requirement that the spatial origin of $S'$ moves at $v$ in $S$ to reduce the spatial equation to $x' = \gamma(x - vt)$.
3. State (citing isotropy/reciprocity) that $\gamma_v = \gamma_{-v}$, so the inverse is $x = \gamma(x' + vt')$ with the *same* $\gamma$.
4. Impose the constancy of light — a ray $x = ct$ in $S$ is $x' = ct'$ in $S'$ — and solve for $\gamma = (1 - v^2/c^2)^{-1/2}$.
5. Recover the time equation $t' = \gamma(t - vx/c^2)$ by substituting the spatial equation into its inverse.
6. Verify the result independently: check that a light ray maps to a light ray, and that $v \ll c$ gives the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]].

**Recall:**

![[Def - Inertial Frame and the Postulates of Special Relativity#The Definition]]

The target is the [[Def - The Lorentz Transformation|Lorentz boost]]:

![[Def - The Lorentz Transformation#The Definition]]

The full uniqueness statement (this exercise is its hands-on execution) is [[Thm - Uniqueness of the Lorentz Transformation from the Postulates]].

---

# Convergent Strategy

**Problem class.** This is a *derivation-from-axioms* problem, the load-bearing one of the chapter: produce a specific formula as the forced consequence of stated principles. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] for such problems is to apply each physical demand in sequence, watching it remove one degree of freedom, until nothing is left undetermined.

**Assumption pattern.** Four assumptions, applied in a fixed order: inertia (giving linearity), the moving-origin condition (giving the spatial form), isotropy/reciprocity (giving evenness of $\gamma$), and the constancy of light (giving $\gamma$'s value). Each is a distinct physical input and each is *necessary* — dropping any one leaves the transformation underdetermined or wrong. Recognising which assumption does which job is the skill the exercise drills.

**Theorem routing.** The route is exactly the lemma chain of [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|the uniqueness theorem]]: Lemma 1 (linearity) → Lemma 2 (spatial form) → Lemma 3 (evenness) → Lemma 4 (light fixes $\gamma$) → Lemma 5 (clock equation) → Lemma 6 (transverse). The evenness step may be cited from [[Ex - Reciprocity and the evenness of the Lorentz factor|the reciprocity exercise]] rather than re-derived.

**Key decision point.** The crux — where most attempts stall — is the light step (4). The trap is to substitute $x = ct$ into the spatial equation alone, obtaining one equation for the single unknown ratio $t'/t$ but *not* for $\gamma$; one must *also* impose $x' = ct'$ and use the inverse relation, yielding a *second* equation, and then *multiply* the two so the times cancel and $\gamma$ falls out. Recognising that two light conditions (forward and backward) are needed, and that multiplying them is the move, is the decisive insight.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the transformation and its inverse).** The whole derivation manipulates the forward map $x' = \gamma(x - vt)$ and the inverse $x = \gamma(x' + vt')$, related by $v \to -v$.

2. **Operation 7 from the topic page (use a symmetry to constrain the form).** Isotropy is invoked in step 3 to force $\gamma_v = \gamma_{-v}$, ensuring forward and inverse carry the same $\gamma$.

3. **Operation 4 from the topic page (take the low-speed / $c \to \infty$ limit as a check).** Step 6 confirms the Galilean limit, the standard correctness test.

---

# Hints

> [!note]- Hint 1
> Linearity comes from the law of inertia: straight worldlines (free particles) must map to straight worldlines because both frames are inertial. A line-preserving map fixing the origin is linear.

> [!note]- Hint 2
> The $S'$ spatial origin is the set $x' = 0$; in $S$ it is the worldline $x = vt$. So the linear function $x'$ vanishes exactly on the line $x - vt = 0$, forcing $x' = \gamma(x - vt)$.

> [!note]- Hint 3
> Do not assume the time equation. Get $\gamma$ first from light, *then* derive the time equation by substitution. For the light step, you need *two* conditions: $x = ct \Rightarrow x' = ct'$ (forward) and the same ray through the inverse. Multiply the two resulting scalar equations.

> [!note]- Hint 4
> The two light equations are $t' = \gamma(1 - v/c)\,t$ (from forward) and $t = \gamma(1 + v/c)\,t'$ (from inverse). Their product gives $1 = \gamma^2(1 - v^2/c^2)$.

> [!note]- Hint 5
> For the time equation: substitute $x' = \gamma(x - vt)$ into $x = \gamma(x' + vt')$ and solve for $t'$. Use $1 - \gamma^2 = -\gamma^2 v^2/c^2$ to simplify.

---

# Solution

The derivation removes one degree of freedom per physical demand. Inertia forces linearity (Step 1); the moving origin forces the spatial form (Step 2); isotropy forces $\gamma$ even, so forward and inverse share $\gamma$ (Step 3); the constancy of light fixes $\gamma$ (Step 4); the clock equation then falls out by substitution (Step 5); and a light-ray check plus the Galilean limit confirm the result (Step 6).

**Step 1: Linearity — $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.**

> [!note]- Derivation
> A free particle moves at constant velocity in $S$ (law of inertia), so its worldline is a straight line in the $(t,x)$ plane. Since $S'$ is *also* inertial, the same particle moves at constant velocity in $S'$, so the image worldline is straight in $(t', x')$. Hence the coordinate map carries every straight line to a straight line. A bijection of the plane carrying lines to lines, and fixing the origin (the frames coincide at $t = t' = 0$), is linear. Therefore
> $$x' = \alpha_1 x + \alpha_2 t, \qquad t' = \alpha_3 x + \alpha_4 t,$$
> with constants $\alpha_i = \alpha_i(v)$. (Nonlinearity would make free particles curve in $S'$, contradicting that $S'$ is inertial.)

**Step 2: Spatial form — $x' = \gamma(x - vt)$.**

> [!note]- Derivation
> The spatial origin of $S'$ is the locus $x' = 0$. By hypothesis $S'$ moves at $v$, so this locus is the worldline $x = vt$ in $S$. Thus the linear function $x' = \alpha_1 x + \alpha_2 t$ vanishes whenever $x = vt$, i.e. on the line $x - vt = 0$. A linear function vanishing on that line is a multiple of $(x - vt)$:
> $$x' = \gamma\,(x - vt), \qquad \gamma := \alpha_1, \quad \alpha_2 = -\gamma v.$$
> This spends both spatial coefficients in favour of the single unknown scale $\gamma = \gamma_v$.

**Step 3: Evenness — $\gamma_v = \gamma_{-v}$, so the inverse is $x = \gamma(x' + vt')$.**

> [!note]- Derivation
> By isotropy, $\gamma$ can depend on the velocity only through $v^2$ (no spatial direction is preferred), so $\gamma_v = \gamma_{-v}$; the independent reflected-frame argument gives the same, worked out fully in [[Ex - Reciprocity and the evenness of the Lorentz factor]]. Now view the transformation from $S'$: relative to $S'$, frame $S$ moves at $-v$, so the same structural argument (Steps 1–2 with $v \to -v$) gives $x = \gamma_{-v}(x' + vt')$. Evenness makes $\gamma_{-v} = \gamma_v = \gamma$, so the inverse is
> $$x = \gamma(x' + vt')$$
> with the *same* $\gamma$. This is the principle of relativity made quantitative: the two frames are symmetric.

**Step 4: Light fixes $\gamma = (1 - v^2/c^2)^{-1/2}$.**

> [!note]- Derivation
> A light ray in $S$ has $x = ct$. By the second postulate the *same* ray has $x' = ct'$ in $S'$. Substitute $x = ct$ into the forward spatial equation:
> $$x' = \gamma(ct - vt) = \gamma(c - v)\,t.$$
> Since $x' = ct'$, divide by $c$: $\ t' = \gamma\!\left(1 - \dfrac{v}{c}\right)t$. (Equation A.)
>
> Now the same ray through the inverse $x = \gamma(x' + vt')$, with $x' = ct'$:
> $$x = \gamma(ct' + vt') = \gamma(c + v)\,t', \quad\text{and } x = ct, \text{ so } ct = \gamma(c + v)t' \Rightarrow t = \gamma\!\left(1 + \frac{v}{c}\right)t'. \quad\text{(Equation B.)}$$
> Multiply Equation A by Equation B:
> $$t'\,t = \gamma^2\!\left(1 - \frac{v}{c}\right)\!\left(1 + \frac{v}{c}\right)t\,t' = \gamma^2\!\left(1 - \frac{v^2}{c^2}\right)t\,t'.$$
> Cancel $t\,t' \ne 0$:
> $$1 = \gamma^2\!\left(1 - \frac{v^2}{c^2}\right) \quad\Longrightarrow\quad \boxed{\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}}$$
> (positive root, since $\gamma \to 1$ as $v \to 0$). This is the only step using the second postulate; it supplies the single number $\gamma$.

**Step 5: Clock equation — $t' = \gamma(t - vx/c^2)$.**

> [!note]- Derivation
> Substitute the forward spatial equation $x' = \gamma(x - vt)$ into the inverse $x = \gamma(x' + vt')$:
> $$x = \gamma\big[\gamma(x - vt) + vt'\big] = \gamma^2(x - vt) + \gamma v t'.$$
> Solve for $\gamma v t'$:
> $$\gamma v t' = x - \gamma^2 x + \gamma^2 v t = x(1 - \gamma^2) + \gamma^2 v t.$$
> Now $1 - \gamma^2 = 1 - \dfrac{1}{1 - v^2/c^2} = \dfrac{-v^2/c^2}{1 - v^2/c^2} = -\gamma^2\dfrac{v^2}{c^2}$. Hence
> $$\gamma v t' = -\gamma^2\frac{v^2}{c^2}x + \gamma^2 v t = \gamma^2 v\left(t - \frac{v}{c^2}x\right).$$
> Divide by $\gamma v$ ($v \ne 0$):
> $$\boxed{t' = \gamma\!\left(t - \frac{v}{c^2}x\right)}.$$
> Appending the transverse equations $y' = y$, $z' = z$ (isotropy about the $x$-axis, [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|Lemma 6]]) completes the boost.

**Step 6: Independent checks — light maps to light; Galilean limit.**

> [!note]- Derivation
> *Light check.* Take $x = ct$. Then $x' = \gamma(ct - vt) = \gamma t(c - v)$ and $t' = \gamma(t - v t/c) = \gamma t(1 - v/c) = \gamma t (c-v)/c$. So $x'/t' = \dfrac{\gamma t(c-v)}{\gamma t (c-v)/c} = c$. The ray travels at $c$ in $S'$ too — the second postulate is reproduced, confirming the derivation is consistent.
>
> *Galilean limit.* As $v/c \to 0$, $\gamma \to 1$ and $v x/c^2 \to 0$ (for fixed $x, v$). Then $x' \to x - vt$ and $t' \to t$ — the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]]. The new physics (the term $-vx/c^2$ in the clock equation) vanishes at low speed, as it must (see [[Ex - Recovering the Galilean transformation in the low-speed limit]]).

> [!note]- Complete formal solution
> *Linearity.* Both frames inertial ⇒ free worldlines (straight lines) map to straight lines ⇒ the origin-fixing map is linear: $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.
> *Spatial form.* The $S'$ origin $x' = 0$ is $x = vt$, so $x'$ vanishes on $x - vt = 0$ ⇒ $x' = \gamma(x - vt)$.
> *Evenness.* Isotropy ⇒ $\gamma_v = \gamma_{-v}$ ⇒ inverse $x = \gamma(x' + vt')$ with the same $\gamma$.
> *Determine $\gamma$.* Light $x = ct \Rightarrow x' = ct'$: forward gives $t' = \gamma(1 - v/c)t$; inverse gives $t = \gamma(1 + v/c)t'$; product gives $1 = \gamma^2(1 - v^2/c^2)$, so $\gamma = (1 - v^2/c^2)^{-1/2}$.
> *Clock equation.* Substituting $x' = \gamma(x - vt)$ into $x = \gamma(x' + vt')$ and using $1 - \gamma^2 = -\gamma^2 v^2/c^2$ gives $t' = \gamma(t - vx/c^2)$.
> *Transverse.* $y' = y$, $z' = z$. The complete boost is
> $$x' = \gamma(x - vt),\quad t' = \gamma\!\left(t - \tfrac{v}{c^2}x\right),\quad y'=y,\quad z'=z,\quad \gamma = (1 - v^2/c^2)^{-1/2}.$$
> *Checks.* $x = ct \Rightarrow x'/t' = c$ (light maps to light); $v/c \to 0 \Rightarrow$ Galilean transformation. $\blacksquare$

> [!warning] Illegal but tempting: positing the time equation
> A common shortcut writes down $t' = \gamma(t - vx/c^2)$ as a *second assumption* alongside $x' = \gamma(x - vt)$, then "checks" the light condition. This begs the question: the symmetric appearance of the two equations is a *consequence* of the postulates, not an input. If you assume both equations you have assumed the answer. The honest derivation assumes only the spatial form and the constancy of light, *solves* for $\gamma$, and then *derives* the clock equation by substitution — which is the whole content of Step 5 and the reason the time equation's position-dependent term is forced rather than chosen.

---

# Key Takeaways

**Each physical postulate removes exactly one degree of freedom, and tracking that bookkeeping is how axiomatic derivations are organised.** The transformation begins with infinitely many degrees of freedom (arbitrary functions $f, g$) and ends fully determined, and the discipline is to watch each demand spend its share: inertia collapses functions to four numbers, the moving origin spends two, isotropy ties the rest to one unknown $\gamma$, and the constancy of light spends the last. The transferable habit — useful in deriving the rotation group, the Galilean group, the form of a propagator, or any structure pinned by symmetry — is to *count* the degrees of freedom before and after each assumption and confirm the final count is zero. If you finish with freedom left over, you are missing a physical input; if you finish over-determined, you have imposed a contradiction or assumed the answer. Counting is the skeleton on which the whole derivation hangs.

**The constancy of light is the single numerical input, and it enters by multiplying the forward and backward light conditions.** Everything before Step 4 is structure (linearity, the moving origin, symmetry); only the second postulate carries a *number*, and it enters through a specific algebraic move — write the light condition forward ($t' = \gamma(1 - v/c)t$) and backward ($t = \gamma(1 + v/c)t'$), then *multiply* so the times cancel and $\gamma^2(1 - v^2/c^2) = 1$ pops out. The factors $(1 - v/c)$ and $(1 + v/c)$ are the relativistic Doppler factors, and their geometric mean being $\gamma^{-1}$ is the same fact that makes the [[Ex - The k-calculus (Bondi) derivation|Bondi k-factor]] $k = \sqrt{(c+v)/(c-v)}$ central. The recognition that *two* light conditions are needed (one per direction) and that *multiplying* them is the key step is the one piece of cleverness in the derivation; a reader who sees only one light condition gets stuck with one equation and two unknowns.

**The clock equation is derived, never assumed, and its position-dependent term is the death of absolute time.** The deepest point of the exercise is methodological: the time transformation $t' = \gamma(t - vx/c^2)$ must *emerge* from substituting the spatial equation into its inverse, not be written down by hand. This matters because the term $-\gamma vx/c^2$ — the relativity of simultaneity — is precisely the new physics, and seeing it *forced* by consistency (rather than chosen) is seeing *why* absolute time had to go. Whenever you derive a transformation or a constraint, be suspicious of any step that "assumes" the part carrying the novel physics; the rigorous derivation extracts that part from the parts you are entitled to assume. Here, assuming the symmetric two-equation form would have hidden the entire lesson, which is that the constancy of light *plus consistency* leaves no choice but a position-dependent clock — and that is the discovery special relativity is.
