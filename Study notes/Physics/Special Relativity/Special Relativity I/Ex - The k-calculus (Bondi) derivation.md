---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
  - "Def - Spacetime Diagram"
tags: [physics, special-relativity]
---

# Problem Statement

Bondi's **$k$-calculus** derives the Lorentz transformation using only light signals, clock readings, and elementary algebra — no postulate of linearity, no isotropy argument, no $\gamma$ pulled from a quadratic. Two inertial observers $O$ and $O'$ pass at event $E$, set their clocks to zero there, and move apart along a line at relative speed $v$. (Work with $c$ explicit.)

1. **The $k$-factor.** $O$ emits a light signal towards $O'$ at $O$-clock-reading $T$; it arrives at $O'$ at $O'$-clock-reading $T' = kT$. Argue that $k$ is a constant depending only on the relative velocity (not on $T$), so $k$ is well-defined.
2. **The reflected signal and the radar coordinates.** $O'$ immediately reflects the signal back to $O$, where it arrives at $O$-clock-reading $k^2 T$ (apply the $k$-factor again, now $O' \to O$). Using the [[Def - Spacetime Diagram|radar method]], assign to the reflection event $B$ the coordinates $O$ measures: time $t = \tfrac12(k^2 + 1)T$ and position $x = \tfrac12 c(k^2 - 1)T$.
3. **$k$ in terms of $v$.** From $v = x/t$ for the reflection event (which lies on $O'$'s worldline), show
$$
v = \frac{c(k^2 - 1)}{k^2 + 1}, \qquad\text{equivalently}\qquad k = \sqrt{\frac{c + v}{c - v}}.
$$
4. **Recover the Lorentz transformation.** Let $B$ be a general event; $O$ assigns it $(t, x)$ via signals sent at $O$-time $T_e$ and received at $O$-time $T_r$, and $O'$ assigns it $(t', x')$ via the analogous $O'$-times. Using $t = \tfrac12(T_r + T_e)$, $x = \tfrac12 c(T_r - T_e)$ and the $k$-relations between the $O$- and $O'$-signal-times, derive the Lorentz boost $t' = \gamma(t - vx/c^2)$, $x' = \gamma(x - vt)$, identifying $\gamma = \tfrac12(k + k^{-1})$.
5. **Relate $k$ to rapidity and to the Doppler shift.** Show $k = e^{\varphi}$ where $\varphi$ is the [[Def - Rapidity|rapidity]] ($\tanh\varphi = v/c$), so that $k$ is the relativistic **Doppler factor** and composing two collinear boosts multiplies their $k$-factors.

**Recall:**

![[Def - Inertial Frame and the Postulates of Special Relativity#The Definition]]

The **radar method** (see [[Def - Spacetime Diagram]] and [[Ex - The operational synchronisation of clocks]]) assigns to an event the time $\tfrac12(T_r + T_e)$ and position $\tfrac12 c(T_r - T_e)$ from the emission/reception clock-readings $T_e, T_r$ of a reflected light signal. The target is the [[Def - The Lorentz Transformation|Lorentz boost]]. The [[Def - Rapidity|rapidity]] $\varphi$ satisfies $v = c\tanh\varphi$, $\gamma = \cosh\varphi$.

---

# Convergent Strategy

**Problem class.** This is a *second-independent-derivation* problem — reproduce a known result (the Lorentz transformation) by a logically disjoint route, both to verify it and to expose new structure. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] values such cross-checks: a result reached two ways is trustworthy, and each route illuminates a different facet (here, the Doppler/eigenvalue facet).

**Assumption pattern.** The $k$-calculus assumes far *less* than the [[Ex - Deriving the Lorentz transformation from the postulates|algebraic derivation]]: no linearity postulate (it follows), no isotropy argument, no quadratic for $\gamma$. The only inputs are the constancy of $c$ (so light signals are the universal yardstick), the constancy of $k$ (from "only relative velocity is observable, and $O, O'$ do not accelerate"), and the radar coordinatisation. The recognition is that the single number $k$ — the factor by which received light-signal time-intervals are stretched — encodes the *entire* transformation.

**Theorem routing.** The route is: define $k$ (a Doppler factor) → apply it twice for the round trip → radar-assign coordinates → solve $v = x/t$ for $k(v)$ → feed the $k$-relations into the radar formulas for a general event to get the boost → identify $\gamma = \tfrac12(k + k^{-1})$ and $k = e^\varphi$. It connects to [[Thm - Relativistic Velocity Addition|velocity addition]] (composition multiplies $k$'s) and to [[Def - Rapidity|rapidity]] (additive because $k = e^\varphi$).

**Key decision point.** The decisive idea is to apply the $k$-factor *twice and symmetrically*: once for $O \to O'$ (outbound) and once for $O' \to O$ (the reflected return), using the *same* $k$ because the relative speed is the same and the principle of relativity makes the two directions reciprocal. This symmetric double application is what turns a single Doppler measurement into a full coordinatisation, and getting the *same* $k$ in both directions (rather than $k$ and some other $k'$) is the reciprocity that the principle of relativity supplies — the analogue of the evenness of $\gamma$ in the algebraic route.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the transformation / constancy of $c$).** Light signals at speed $c$ are the sole tool; the radar coordinatisation and the $k$-relations are built from them.

2. **Operation 6 from the topic page (read geometry off a spacetime diagram).** The emission, reflection, and reception events and their $45^\circ$ light rays are best tracked on a [[Def - Spacetime Diagram|spacetime diagram]] (Bondi's "radar diagram").

3. **Operation 5/6 from the topic page (rapidity makes boosts additive).** Step 5 identifies $k = e^\varphi$, so multiplying $k$-factors is adding rapidities — the operation behind [[Thm - Relativistic Velocity Addition|velocity addition]].

---

# Hints

> [!note]- Hint 1
> $k$ is constant because (i) neither observer accelerates, so nothing changes with time, and (ii) only relative velocity is observable, so $k$ can depend only on $v$. Linearity of the relation $T' = kT$ then follows rather than being assumed.

> [!note]- Hint 2
> Apply $k$ *twice*: $O$ sends at $T$, $O'$ receives at $kT$, reflects immediately, and $O$ receives at $k(kT) = k^2 T$. The reflection event $B$ is coordinatised by $O$ via radar: time = midpoint $\tfrac12(k^2 T + T)$, position = half-distance $\tfrac12 c(k^2 T - T)$.

> [!note]- Hint 3
> The reflection event $B$ is *on $O'$'s worldline* (that is where the reflection happens). So $x/t = v$, the speed of $O'$. Substitute the radar coordinates and solve for $k^2$.

> [!note]- Hint 4
> For a general event $B$, let $O$ send at $T_e$ and receive at $T_r$; then $t = \tfrac12(T_r + T_e)$, $x = \tfrac12 c(T_r - T_e)$. The *same* light rays, in $O'$'s coordinatisation, are sent at $T'_e$ and received at $T'_r$, with $t' = \tfrac12(T'_r + T'_e)$, $x' = \tfrac12 c(T'_r - T'_e)$. The $k$-factor relates the outgoing ray ($O \to O'$) and the returning ray ($O' \to O$): $T'_e = k T_e$ (outgoing) and $T_r = k T'_r$ (returning). Eliminate the primed signal-times.

> [!note]- Hint 5
> $k = \sqrt{(c+v)/(c-v)}$. With $v = c\tanh\varphi$, compute $(c+v)/(c-v) = (1 + \tanh\varphi)/(1 - \tanh\varphi) = e^{2\varphi}$, so $k = e^\varphi$. Then $\gamma = \tfrac12(k + 1/k) = \cosh\varphi$. Two boosts: $k_{12} = k_1 k_2 \Rightarrow \varphi_{12} = \varphi_1 + \varphi_2$.

---

# Solution

The single number $k$ — the Doppler stretch of received light-signal intervals — encodes the whole transformation. Defining $k$ (Step 1), applying it twice for a round trip and radar-coordinatising (Step 2), and demanding the reflection lie on $O'$'s worldline (Step 3) gives $k(v)$. Feeding the $k$-relations into the radar formulas for a general event recovers the Lorentz boost with $\gamma = \tfrac12(k + k^{-1})$ (Step 4), and $k = e^\varphi$ exhibits it as the Doppler factor with additive rapidity (Step 5).

**Step 1: $k$ is a well-defined constant, function of $v$ only.**

> [!note]- Derivation
> $O$ emits a light flash towards $O'$ at $O$-clock-reading $T$; $O'$ receives it at $O'$-clock-reading $T' = kT$. Two facts make $k$ a constant:
> - *No acceleration.* Both observers are inertial, so the physical situation is unchanging in time — the factor relating emission and reception times cannot itself depend on *when* the signal is sent. Hence $k$ is independent of $T$, so $T' = kT$ is *linear* (a doubling of $T$ doubles $T'$). Linearity is thus a *consequence* here, not an assumption.
> - *Only relative velocity is observable.* By the [[Def - Inertial Frame and the Postulates of Special Relativity|principle of relativity]], nothing distinguishes the two inertial observers except their relative velocity $v$. So $k = k(v)$, a single function of the relative speed.
>
> $k$ is the **Bondi $k$-factor**: the ratio of received to emitted light-signal time-intervals between two inertial observers. For observers separating ($v > 0$), successive crests arrive more spread out, so $k > 1$ (redshift); for approach, $k < 1$ (blueshift). The reciprocity needed below — that $O' \to O$ uses the *same* $k$ — follows because the principle of relativity makes the two observers interchangeable.

**Step 2: Round-trip and radar coordinates of the reflection event $B$.**

> [!note]- Derivation
> $O$ sends a signal at $O$-time $T$. By Step 1 it reaches $O'$ at $O'$-time $kT$. $O'$ reflects it immediately back towards $O$. Now apply the $k$-factor to the *return* leg ($O' \to O$): the signal was "emitted" by $O'$ at $O'$-time $kT$, so $O$ receives it at $O$-time $k \cdot (kT) = k^2 T$ — using the *same* $k$ by reciprocity.
>
> $O$ now coordinatises the reflection event $B$ by the [[Def - Spacetime Diagram|radar method]]: $B$ is assigned the time halfway between $O$'s emission ($T$) and reception ($k^2 T$), and the distance equal to $c$ times half the round-trip time:
> $$t_B = \frac{T + k^2 T}{2} = \frac{(k^2 + 1)T}{2}, \qquad x_B = \frac{c(k^2 T - T)}{2} = \frac{c(k^2 - 1)T}{2}.$$

**Step 3: $v = c(k^2-1)/(k^2+1)$, hence $k = \sqrt{(c+v)/(c-v)}$.**

> [!note]- Derivation
> The reflection event $B$ lies on $O'$'s worldline (that is where $O'$ was when it reflected the signal). $O'$ moves at speed $v$ through $E$ (the origin), so on its worldline $x_B / t_B = v$. Substitute:
> $$v = \frac{x_B}{t_B} = \frac{\tfrac12 c(k^2 - 1)T}{\tfrac12(k^2 + 1)T} = \frac{c(k^2 - 1)}{k^2 + 1}.$$
> Solve for $k^2$: $v(k^2 + 1) = c(k^2 - 1) \Rightarrow k^2(v - c) = -(c + v) \Rightarrow k^2 = \dfrac{c + v}{c - v}$, so
> $$k = \sqrt{\frac{c + v}{c - v}}.$$
> (Positive root: $k > 0$, and $k \to 1$ as $v \to 0$.) This is the $k$-factor as a function of relative velocity, derived from light signals alone.

**Step 4: Recover the Lorentz boost; $\gamma = \tfrac12(k + k^{-1})$.**

> [!note]- Derivation
> Let $B$ be a *general* event. $O$ assigns it coordinates via a radar signal: $O$ emits at $O$-time $T_e$, receives the reflection at $O$-time $T_r$, so
> $$t = \tfrac12(T_r + T_e), \qquad x = \tfrac12 c(T_r - T_e). \tag{$O$}$$
> $O'$ assigns the *same* event coordinates via *its* radar signal, emitting at $O'$-time $T'_e$ and receiving at $T'_r$:
> $$t' = \tfrac12(T'_r + T'_e), \qquad x' = \tfrac12 c(T'_r - T'_e). \tag{$O'$}$$
> Now relate the signal-times by the $k$-factor. The *outgoing* signal that reaches $B$ travels $O \to B$; trace it back: the part of this light ray on the segment $O \to O'$ links $O$'s emission $T_e$ to $O'$'s "passing" time, and by the $k$-relation the relevant $O'$-emission-time obeys $T'_e = k\,T_e$ (the outgoing radar ray of $O'$ is the same null line, scaled by $k$). The *returning* signal travels $B \to O$; by the same $k$-relation applied to the return direction, $T_r = k\,T'_r$. (These two relations are Bondi's key identities: the forward null ray carries the factor $k$, the backward null ray its reciprocal — see Figure 3 of the Oxford notes, equations 2.18–2.19.)
>
> So $T'_e = k T_e$ and $T'_r = T_r / k$. Substitute into ($O'$):
> $$t' = \tfrac12\!\left(\frac{T_r}{k} + k T_e\right), \qquad x' = \tfrac12 c\!\left(\frac{T_r}{k} - k T_e\right).$$
> Invert ($O$) to write $T_e, T_r$ in terms of $t, x$: $T_e = t - x/c$, $T_r = t + x/c$. Then
> $$t' = \tfrac12\!\left[\frac{1}{k}\Big(t + \frac{x}{c}\Big) + k\Big(t - \frac{x}{c}\Big)\right] = \tfrac12\!\left(k + \frac1k\right)t - \tfrac12\!\left(k - \frac1k\right)\frac{x}{c},$$
> $$x' = \tfrac12 c\!\left[\frac{1}{k}\Big(t + \frac{x}{c}\Big) - k\Big(t - \frac{x}{c}\Big)\right] = -\tfrac12\!\left(k - \frac1k\right)c\,t + \tfrac12\!\left(k + \frac1k\right)x.$$
> Now identify the coefficients. Define $\gamma := \tfrac12(k + k^{-1})$. From Step 3, $k^2 = (c+v)/(c-v)$, so
> $$\tfrac12\!\left(k + \frac1k\right) = \frac{k^2 + 1}{2k} = \frac{\frac{c+v}{c-v} + 1}{2\sqrt{\frac{c+v}{c-v}}} = \frac{\frac{2c}{c-v}}{2\sqrt{\frac{c+v}{c-v}}} = \frac{c}{\sqrt{(c-v)(c+v)}} = \frac{1}{\sqrt{1 - v^2/c^2}} = \gamma. \checkmark$$
> Similarly $\tfrac12(k - k^{-1}) = \dfrac{k^2 - 1}{2k} = \dfrac{\frac{2v}{c-v}}{2\sqrt{\frac{c+v}{c-v}}} = \dfrac{v}{\sqrt{c^2 - v^2}} = \gamma\,\dfrac{v}{c}$. Substituting,
> $$t' = \gamma\,t - \gamma\frac{v}{c}\cdot\frac{x}{c} = \gamma\!\left(t - \frac{v}{c^2}x\right), \qquad x' = -\gamma\frac{v}{c}\cdot c\,t + \gamma\,x = \gamma(x - vt).$$
> This is exactly the [[Def - The Lorentz Transformation|Lorentz boost]], with $\gamma = \tfrac12(k + k^{-1})$. The $k$-calculus has reproduced it from light signals alone.

**Step 5: $k = e^\varphi$ — the Doppler factor, with additive rapidity.**

> [!note]- Derivation
> Write $v = c\tanh\varphi$ ([[Def - Rapidity|rapidity]] $\varphi$). Then
> $$k^2 = \frac{c + v}{c - v} = \frac{1 + \tanh\varphi}{1 - \tanh\varphi} = \frac{\cosh\varphi + \sinh\varphi}{\cosh\varphi - \sinh\varphi} = \frac{e^{\varphi}}{e^{-\varphi}} = e^{2\varphi},$$
> so $\boxed{k = e^{\varphi}}$. Consequently $\gamma = \tfrac12(k + k^{-1}) = \tfrac12(e^\varphi + e^{-\varphi}) = \cosh\varphi$ and $\gamma v/c = \tfrac12(k - k^{-1}) = \sinh\varphi$, recovering the [[Def - Rapidity|hyperbolic parametrisation]] of the boost.
>
> $k$ is precisely the relativistic **Doppler factor**: a periodic signal of $O$-period $\tau$ is received by $O'$ with period $k\tau$, i.e. frequency shifted by $1/k = e^{-\varphi}$. And because $k = e^\varphi$, composing two collinear boosts *multiplies* the $k$-factors, $k_{12} = k_1 k_2$, which is *adding* rapidities $\varphi_{12} = \varphi_1 + \varphi_2$ — the cleanest statement of [[Thm - Relativistic Velocity Addition|relativistic velocity addition]]. Finally, $k$ and $k^{-1}$ are the two *eigenvalues* of the boost matrix (its eigenvectors are the two null directions $x = \pm ct$), so the $k$-factor is the eigenvalue of the Lorentz transformation along the light cone — the structural reason it governs everything.

> [!note]- Complete formal solution
> Define $k$ by $T' = kT$ for a light signal $O \to O'$; inertia makes $k$ constant (so $T' = kT$ linear) and relativity makes $k = k(v)$. A round trip applies $k$ twice: $O$ sends at $T$, $O$ receives at $k^2 T$, and radar-coordinatises the reflection $B$ as $t = \tfrac12(k^2+1)T$, $x = \tfrac12 c(k^2-1)T$. Since $B$ is on $O'$'s worldline, $v = x/t = c(k^2-1)/(k^2+1)$, so $k = \sqrt{(c+v)/(c-v)}$. For a general event, $O$'s radar gives $t = \tfrac12(T_r + T_e)$, $x = \tfrac12 c(T_r - T_e)$ and $O'$'s gives the primed analogues; the $k$-relations $T'_e = kT_e$, $T'_r = T_r/k$ then yield, with $T_e = t - x/c$, $T_r = t + x/c$, the boost $t' = \gamma(t - vx/c^2)$, $x' = \gamma(x - vt)$ where $\gamma = \tfrac12(k + k^{-1}) = (1 - v^2/c^2)^{-1/2}$. Writing $v = c\tanh\varphi$ gives $k = e^\varphi$, so $k$ is the Doppler factor, $\gamma = \cosh\varphi$, and composing boosts multiplies $k$'s (adds rapidities). $\blacksquare$

---

# Key Takeaways

**One physically measurable number — the Doppler factor $k$ — encodes the entire Lorentz transformation, and it is more primitive than $\gamma$.** The $k$-calculus teaches that you do not need to start from linearity, isotropy, and a quadratic; you need only the factor by which received light-signal intervals are stretched, which is directly observable as a Doppler shift. From $k$ alone, linearity *follows* (from no-acceleration), $\gamma = \tfrac12(k + k^{-1})$ *follows*, and the full boost *follows*. The reusable lesson is that the right primitive variable can make a derivation almost trivial: $k$ is multiplicative under composition and exponential in rapidity, so it linearises the boost group in a way velocity never does. The trigger to reach for $k$ (or its logarithm, rapidity): any problem about *composing* boosts, about Doppler shifts, or about the eigenstructure of the Lorentz map — there, $k$ turns nonlinear velocity algebra into multiplication, and rapidity turns it into addition.

**A second, logically independent derivation is the strongest possible confirmation, and each derivation exposes different structure.** Reaching the Lorentz transformation by the $k$-calculus — which assumes *less* than the [[Ex - Deriving the Lorentz transformation from the postulates|algebraic route]] (no linearity postulate, no isotropy step) — both confirms the result and reveals what the algebraic route hides: that $\gamma$ is the average $\tfrac12(k + k^{-1})$ of the two null eigenvalues of the boost, and that the relativistic Doppler effect, velocity addition, and the boost are *one* phenomenon seen through the variable $k$. The general principle: when a result can be derived from a *weaker* set of assumptions, that derivation is more fundamental and more illuminating, and the comparison tells you exactly which of your original assumptions were redundant (here, linearity and isotropy were consequences, not axioms). Whenever you have one derivation of an important result, it is worth hunting for a second from different primitives — the agreement is reassurance, and the contrast is insight.

**The $k$-factor is the eigenvalue of the Lorentz transformation, which is why it governs the boost, the Doppler shift, and velocity composition at once.** The boost matrix has eigenvectors along the two null directions $x = \pm ct$ (the light cone), with eigenvalues $k$ and $k^{-1}$ — light along $+x$ is stretched by $k$, light along $-x$ compressed by $k^{-1}$. This single algebraic fact unifies the chapter's themes: the Doppler shift is the eigenvalue acting on a light signal; $\gamma = \tfrac12(k + k^{-1})$ is the average of the eigenvalues (the matrix trace over 2); $\det = k \cdot k^{-1} = 1$ is the product; and composing boosts multiplies eigenvalues, $k_1 k_2$, which is why rapidities (logarithms of eigenvalues) add. The transferable diagnostic: when a linear transformation has a privileged invariant subspace (here the light cone), diagonalise on it — the eigenvalues are usually the physically meaningful, composition-friendly variables, and expressing everything in terms of them collapses a tangle of formulas into a single clean structure. This is the deep reason rapidity, not velocity, is the natural coordinate on the boost group.
