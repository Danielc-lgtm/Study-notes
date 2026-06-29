---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Relativistic Velocity Addition"
  - "Def - The Lorentz Transformation"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ unless restoring $c$ clarifies a limit. A particle moves at velocity $u'$ in frame $S'$, and $S'$ moves at velocity $v$ relative to $S$ (all collinear).

1. **Derive the law by dividing coordinates.** Starting from the particle's worldline $x' = u't'$ in $S'$, apply the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] to both $x'$ and $t'$ and take the ratio to obtain
$$u = \frac{u' + v}{1 + u'v} \qquad\left(\text{with } c: \ u = \frac{u' + v}{1 + u'v/c^2}\right).$$
2. **Fixed point.** Show that $u' = c$ gives $u = c$ for every $v$, recovering the constancy of the speed of light from the addition law.
3. **Ceiling.** Prove that if $|u'| < c$ and $|v| < c$ then $|u| < c$, by establishing the factorisation
$$c - u = \frac{(c - u')(c - v)\,c}{c^2 + u'v} > 0.$$
Interpret: you cannot reach the speed of light by composing sub-light velocities.
4. **Rapidity route.** Redo the derivation through [[Def - Rapidity|rapidity]] $\varphi = \tanh^{-1}(w/c)$: show that collinear boosts add rapidities, so $u = c\tanh(\varphi_{u'} + \varphi_v)$, and use this to show that $N$ successive boosts of velocity $w$ give net velocity $c\tanh(N\varphi_w) \to c$ as $N\to\infty$ but never equal to $c$.

**Recall:**

![[Thm - Relativistic Velocity Addition#Statement]]

The inverse [[Def - The Lorentz Transformation|Lorentz transformation]] (from $S'$ to $S$, $S'$ moving at $v$) is $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$. The **rapidity** of a velocity $w$ is $\varphi_w = \tanh^{-1}(w/c)$, with $w = c\tanh\varphi_w$; collinear boosts compose by adding rapidities, and a boost has matrix $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\ \sinh\varphi & \cosh\varphi\end{pmatrix}$ acting on $(ct, x)$ ([[Def - Rapidity]]).

---

# Convergent Strategy

**Problem class.** A *derive-and-establish-structural-properties* problem: get the velocity-addition formula two ways and prove its two defining features (fixed point, ceiling). The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] for combining velocities is to switch to rapidity; this exercise builds both the coordinate and rapidity routes.

**Assumption pattern.** The coordinate route leans on "velocity is a ratio $dx/dt$", so the $\gamma$'s cancel and a new denominator survives. The structural properties lean on algebraic identities: the fixed point is a direct substitution, the ceiling a factorisation. The rapidity route leans on boosts being hyperbolic rotations whose angles add.

**Theorem routing.** Part 1 routes through the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] and the ratio. Part 2 substitutes $u' = c$. Part 3 manipulates $c - u$ into the factored form. Part 4 routes through [[Def - Rapidity]] and the $\tanh$ addition formula, then iterates.

**Key decision point.** The crux of part 1 is transforming *both* coordinates and dividing, not transforming $x'$ alone — the cancellation of $\gamma$ and the appearance of the denominator $1 + u'v$ both depend on it. The crux of part 3 is the algebraic insight that $c - u$ *factorises* as $(c-u')(c-v)$ over a positive denominator, which converts a one-off inequality into a structural impossibility (sub-light in $\Rightarrow$ sub-light out, always).

---

# Legal Operations Used

1. **Apply the Lorentz transformation to map events between frames** (operation 1 from the topic page). Part 1 transforms the particle's worldline coordinates from $S'$ to $S$ and divides.

2. **Add velocities relativistically** (operation 6). This exercise *derives* the operation and proves its key properties; the formula $u = (u'+v)/(1+u'v)$ is the operation itself.

3. **Switch to rapidity to make boosts additive** (operation 7). Part 4 replaces velocities by rapidities, turning composition into addition and the $N$-boost iteration into multiplication by $N$.

---

# Hints

> [!note]- Hint 1
> The particle satisfies $x' = u't'$, so $dx' = u'\,dt'$. Transform: $dx = \gamma(dx' + v\,dt')$, $dt = \gamma(dt' + v\,dx')$. Divide: $u = dx/dt$; the $\gamma$'s cancel. Divide top and bottom by $dt'$ and substitute $dx'/dt' = u'$.

> [!note]- Hint 2
> Put $u' = c = 1$ into $u = (u' + v)/(1 + u'v)$: numerator $1 + v$, denominator $1 + v$, ratio $1 = c$. The denominator grows in lockstep with the numerator, pinning light at $c$ in every frame.

> [!note]- Hint 3
> Write $c - u = c - (u'+v)/(1 + u'v/c^2)$ over a common denominator. The numerator is $c(1 + u'v/c^2) - (u' + v) = c + u'v/c - u' - v$. Factor it: group as $(c - u') - \tfrac{v}{c}(c - u') = (c-u')(1 - v/c)$. So $c - u = (c-u')(c-v)/[c(1 + u'v/c^2)]$. Both factors $c - u', c - v > 0$ for sub-light inputs, and the denominator is positive.

> [!note]- Hint 4
> Boost matrices in rapidity form multiply by adding rapidities (use the hyperbolic angle-sum identities). So composing two boosts gives rapidity $\varphi_{u'} + \varphi_v$, and $u = c\tanh(\varphi_{u'} + \varphi_v)$. For $N$ equal boosts of velocity $w$ (rapidity $\varphi_w$), the net rapidity is $N\varphi_w$, so $u_N = c\tanh(N\varphi_w)$. Since $\tanh \to 1$ but never reaches it, $u_N \to c$ without ever equalling $c$.

---

# Solution

Dividing transformed coordinates gives the addition law; light is its fixed point and the speed of light its ceiling, the latter visible through a clean factorisation. The rapidity route reveals the law as hyperbolic-angle addition, making the ceiling the statement that a finite sum of rapidities has $\tanh$ below $1$.

**Step 1: Derivation by dividing coordinates.**

> [!note]- Derivation
> The particle moves at $u'$ in $S'$, so its worldline is $x' = u't'$, i.e. $dx' = u'\,dt'$. Apply the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$ to the differentials:
> $$dx = \gamma(dx' + v\,dt'), \qquad dt = \gamma(dt' + v\,dx').$$
> The particle's velocity in $S$ is the ratio, and the common $\gamma$ cancels (velocity is a ratio):
> $$u = \frac{dx}{dt} = \frac{dx' + v\,dt'}{dt' + v\,dx'} = \frac{dx'/dt' + v}{1 + v\,dx'/dt'} = \frac{u' + v}{1 + u'v}.$$
> Restoring $c$ (the cross term carries $1/c^2$): $u = (u' + v)/(1 + u'v/c^2)$. The numerator is the Galilean sum; the new denominator $1 + u'v/c^2$ — arising because $t$ mixes in some $\Delta x'$, the relativity of simultaneity — is what tames the sum near $c$.

**Step 2: Fixed point — $u' = c \Rightarrow u = c$.**

> [!note]- Derivation
> Substitute $u' = c$:
> $$u = \frac{c + v}{1 + cv/c^2} = \frac{c + v}{1 + v/c} = \frac{c + v}{(c + v)/c} = c,$$
> for **every** $v$ with $|v| < c$. (Symmetrically, $v = c$ gives $u = c$.) So if something moves at $c$ in $S'$, it moves at $c$ in $S$ too: the speed of light is a fixed point of velocity addition. This *recovers the second postulate* — the constancy of light's speed — as a theorem, since the addition law itself follows from the Lorentz transformation, which followed from the postulates. The denominator grows exactly in step with the numerator, which is the algebraic mechanism pinning light at $c$.

**Step 3: Ceiling — sub-light in, sub-light out.**

> [!note]- Derivation
> Compute $c - u$ and factor:
> $$c - u = c - \frac{u' + v}{1 + u'v/c^2} = \frac{c\left(1 + \frac{u'v}{c^2}\right) - (u' + v)}{1 + \frac{u'v}{c^2}} = \frac{c + \frac{u'v}{c} - u' - v}{1 + \frac{u'v}{c^2}}.$$
> Factor the numerator: $c - u' + \tfrac{u'v}{c} - v = (c - u') - \tfrac{v}{c}(c - u') = (c - u')\left(1 - \tfrac{v}{c}\right) = \dfrac{(c-u')(c-v)}{c}$. Hence
> $$c - u = \frac{(c-u')(c-v)/c}{(c^2 + u'v)/c^2} = \frac{(c-u')(c-v)\,c}{c^2 + u'v}.$$
> For $|u'| < c$ and $|v| < c$: the factors $c - u' > 0$ and $c - v > 0$, and the denominator $c^2 + u'v > c^2 - c^2 = 0$, so $c - u > 0$, i.e. $u < c$. The identical computation with $-c$ in place of $c$ gives $u > -c$. Therefore **$|u| < c$**: composing two sub-light velocities yields a sub-light velocity, always. You cannot reach the speed of light by adding sub-light speeds — $c$ is an unreachable **ceiling**, not merely a fixed point. (Iterating, no finite chain of boosts ever attains $c$; see Step 4.)

**Step 4: Rapidity route and the $N$-boost limit.**

> [!note]- Derivation
> Introduce [[Def - Rapidity|rapidity]] $\varphi_w = \tanh^{-1}(w/c)$, so $w = c\tanh\varphi_w$. A collinear boost of velocity $w$ acts on $(ct, x)$ by $B(\varphi_w) = \begin{pmatrix}\cosh\varphi_w & \sinh\varphi_w\\ \sinh\varphi_w & \cosh\varphi_w\end{pmatrix}$. Composing the boost $S\to S'$ (rapidity $\varphi_v$) with $S'\to$ particle (rapidity $\varphi_{u'}$) multiplies the matrices, and the hyperbolic angle-sum identities give
> $$B(\varphi_{u'})\,B(\varphi_v) = B(\varphi_{u'} + \varphi_v),$$
> so the net boost has rapidity $\varphi_u = \varphi_{u'} + \varphi_v$ — **rapidities add**. Converting back,
> $$u = c\tanh(\varphi_{u'} + \varphi_v) = c\,\frac{\tanh\varphi_{u'} + \tanh\varphi_v}{1 + \tanh\varphi_{u'}\tanh\varphi_v} = \frac{u' + v}{1 + u'v/c^2},$$
> the same law, now revealed as the $\tanh$ addition formula.
>
> *The $N$-boost limit.* Apply $N$ successive collinear boosts each of velocity $w$ (rapidity $\varphi_w$). The rapidities add to $N\varphi_w$, so the net velocity is
> $$u_N = c\tanh(N\varphi_w).$$
> Since $\varphi_w > 0$ is fixed and $\tanh$ is strictly increasing with $\tanh(x) \to 1$ as $x\to\infty$ but $\tanh(x) < 1$ for all finite $x$, we have $u_N \to c$ as $N\to\infty$ but $u_N < c$ for every finite $N$. Boosting forever approaches the speed of light **asymptotically and never reaches it** — the ceiling, seen as the fact that a finite sum of finite rapidities is finite, so its $\tanh$ stays below $1$. Light is rapidity infinity.

> [!note]- Complete formal solution
> From the worldline $x' = u't'$, the inverse Lorentz transformation gives $dx = \gamma(dx' + v\,dt')$, $dt = \gamma(dt' + v\,dx')$, so $u = dx/dt = (u' + v)/(1 + u'v/c^2)$, the $\gamma$'s cancelling. Setting $u' = c$ gives $u = (c+v)/(1 + v/c) = c$ for all $v$: light is a fixed point. The identity $c - u = (c-u')(c-v)c/(c^2 + u'v)$ is a ratio of positives for $|u'|, |v| < c$, so $u < c$ (and symmetrically $u > -c$): $c$ is an unreachable ceiling. In rapidity, $w = c\tanh\varphi_w$ and boosts $B(\varphi)$ multiply to add rapidities, $\varphi_u = \varphi_{u'} + \varphi_v$, reproducing the law via the $\tanh$ sum; $N$ equal boosts give $u_N = c\tanh(N\varphi_w) \to c$ without ever reaching it. $\blacksquare$

---

# Key Takeaways

**Velocity addition is the Lorentz transformation applied to a ratio, and the new denominator is the relativity of simultaneity.** The whole law falls out of one move — transform both $dx'$ and $dt'$ and divide — and the only structural difference from Galileo is the denominator $1 + u'v/c^2$. That denominator is not arbitrary: it is there because the transformed time $dt$ mixes in a piece of $dx'$, which is the relativity of simultaneity expressed in differentials. Recognising this connects velocity addition to the rest of the chapter: it is the same simultaneity-tilt that shortens rods and dilates clocks, now acting on the ratio that defines velocity. The transferable technique is that *any* relativistic transformation of a derived quantity (velocity, acceleration, a field) is obtained by transforming the pieces and recombining — never by transforming the numerator alone — and the corrections that appear are always traceable to the mixing of time and space.

**The factorisation $c - u = (c-u')(c-v)\cdot c/(c^2 + u'v)$ turns a one-off inequality into a structural law.** Proving $u < c$ for one pair of inputs would be a calculation; proving it *factorises* is an insight, because the factored form shows the result is not a coincidence of particular numbers but a feature of the algebra — sub-light times sub-light, over a positive quantity, is positive. This is the difference between verifying and understanding: the factorisation makes the speed-of-light ceiling *manifest*, the way $\cos^2 + \sin^2 = 1$ makes the invariance of Euclidean distance manifest. Whenever you want to show a bound is *always* respected rather than merely respected in examples, look for an algebraic identity that exhibits the bounded quantity as a product or ratio of sign-definite pieces. Here that identity is also what proves no chain of boosts reaches $c$: each composition keeps the output strictly below the ceiling, so iterating never breaks through.

**Rapidity is the right coordinate because it linearises the group, and the ceiling becomes obvious in it.** The velocity-addition law looks complicated only because velocity is the wrong variable; rapidity is the additive coordinate on the boost group, and in it the law is just "$\varphi$'s add". This is the exact analogue of preferring angle to slope for rotations, and it pays off threefold: composing many boosts becomes summing numbers, the $N$-boost limit becomes $\tanh(N\varphi_w) \to 1$, and the speed limit becomes the transparent fact that $|\tanh|$ of any finite number is below $1$, so $c$ (rapidity infinity) is approached but never reached. The general lesson — one of the most reusable in the subject — is that when a group's composition law is ugly in one parameter, there is often a "logarithmic" coordinate in which it becomes addition; finding it (rapidity here, the exponential map in Lie theory generally) trivialises iteration and exposes the asymptotic structure. Carry rapidity into any problem that composes, inverts, or iterates boosts; see [[Ex - Two spaceships and the relativistic closing speed]] for a closing-speed problem where the same law governs the approach velocity of two objects.
