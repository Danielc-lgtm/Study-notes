---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Rapidity"
  - "Def - Boosts as Hyperbolic Rotations"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$. The [[Def - Rapidity|rapidity]] is $\varphi$, with $v = \tanh\varphi$, $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$.

1. Starting from $\gamma = \cosh\varphi$ alone, derive the other two relations $\gamma v = \sinh\varphi$ and $v = \tanh\varphi$, using $\gamma^2(1 - v^2) = 1$ and $\cosh^2\varphi - \sinh^2\varphi = 1$.
2. Show that $\varphi = \tanh^{-1}v = \tfrac12\ln\!\big(\tfrac{1+v}{1-v}\big)$ and that this maps the velocity interval $(-1, 1)$ bijectively onto the whole real line $\mathbb{R}$. Sketch (in words) the graph of $\varphi(v)$.
3. Show that the [[Def - Boosts as Hyperbolic Rotations|Doppler]] factor $k = e^{\varphi}$ satisfies $k = \gamma(1 + v) = \sqrt{\tfrac{1+v}{1-v}}$, and that the rapidity is its logarithm, $\varphi = \ln k$.
4. A point on the unit hyperbola $t^2 - x^2 = 1$ (the upper branch) is $(\cosh\varphi, \sinh\varphi)$. Explain why $\varphi$ is the "hyperbolic angle" — the analogue of the circular angle on the unit circle — and what the velocity ceiling $v < 1$ looks like in this picture.

**Recall:**

The [[Def - Rapidity|rapidity]] $\varphi$ parametrises a boost so that boosts compose by adding $\varphi$. The hyperbolic functions satisfy $\cosh^2\varphi - \sinh^2\varphi = 1$, $\cosh\varphi \ge 1$, $\tanh\varphi \in (-1, 1)$, and $\cosh\varphi + \sinh\varphi = e^{\varphi}$. The Lorentz factor is $\gamma = (1 - v^2)^{-1/2}$, so $\gamma^2(1 - v^2) = 1$.

---

# Convergent Strategy

**Problem class.** A *calculation drill* on the rapidity relations, building fluency with the three defining identities and the geometry of the unit hyperbola. It is the routine-application tier: one move (an identity) per part.

**Assumption pattern.** Only the definition $\gamma = \cosh\varphi$ and the two algebraic identities $\gamma^2(1 - v^2) = 1$ and $\cosh^2 - \sinh^2 = 1$. Recognising that these two identities are "the same identity" (both say a quantity and its hyperbolic partner differ by $1$ in squares) is what makes the three rapidity relations equivalent.

**Theorem routing.** Each part is a short manipulation: Part 1 combines the two identities; Part 2 inverts $\tanh$; Part 3 computes $e^{\varphi}$; Part 4 interprets geometrically. No external theorem is invoked; the exercise builds the vocabulary the [[Thm - Boosts Compose by Adding Rapidities|composition theorem]] uses.

**Key decision point.** The only judgement is which identity to start from. Starting from $\gamma = \cosh\varphi$ and matching $\gamma^2(1-v^2) = 1$ against $\cosh^2 - \sinh^2 = 1$ forces $\sinh\varphi = \gamma v$; everything else follows. The geometric interpretation in Part 4 is the conceptual reward: rapidity is arc-length on the hyperbola, exactly as angle is arc-length on the circle.

---

# Legal Operations Used

1. **Switch to rapidity (operation 6 from the topic page).** The exercise is the careful establishment of the rapidity dictionary that operation 6 relies on.

2. **Restore $c$ by dimensional analysis (operation: standing-convention book-keeping).** The $c$-restored forms ($v/c = \tanh\varphi$) are noted; the rapidity is dimensionless because it is the argument of $\tanh$.

---

# Hints

> [!note]- Hint 1
> From $\gamma = \cosh\varphi$ and $\gamma^2(1 - v^2) = 1$, get $\cosh^2\varphi(1 - v^2) = 1$, so $\cosh^2\varphi - \cosh^2\varphi\,v^2 = 1$. Compare with $\cosh^2\varphi - \sinh^2\varphi = 1$ to read off $\sinh^2\varphi = \cosh^2\varphi\,v^2$, i.e. $\sinh\varphi = \gamma v$.

> [!note]- Hint 2
> $v = \tanh\varphi$ inverts to $\varphi = \tanh^{-1}v$. Use the logarithmic form: $\tanh\varphi = \frac{e^{\varphi} - e^{-\varphi}}{e^{\varphi} + e^{-\varphi}} = v$ solves to $e^{2\varphi} = \frac{1+v}{1-v}$.

> [!note]- Hint 3
> $k = e^{\varphi} = \cosh\varphi + \sinh\varphi = \gamma + \gamma v = \gamma(1 + v)$. For the square-root form, use $\gamma = (1-v^2)^{-1/2} = [(1-v)(1+v)]^{-1/2}$.

> [!note]- Hint 4
> On the unit circle $x^2 + y^2 = 1$, a point is $(\cos\theta, \sin\theta)$ and $\theta$ is the arc length / twice the sector area. On the unit hyperbola $t^2 - x^2 = 1$, a point is $(\cosh\varphi, \sinh\varphi)$ and $\varphi$ is twice the hyperbolic sector area. The velocity is the slope $x/t = \tanh\varphi$, which approaches the asymptote $t = x$ (slope $1$) as $\varphi \to \infty$.

---

# Solution

The exercise drills the rapidity dictionary. Step 1 derives all three relations from one. Step 2 inverts to get the logarithmic form and the bijection onto $\mathbb{R}$. Step 3 connects to the Doppler factor. Step 4 gives the hyperbolic-geometry picture in which rapidity is an angle. Each step is one identity.

**Step 1: the three relations from $\gamma = \cosh\varphi$.**

> [!note]- Derivation
> Given $\gamma = \cosh\varphi$. Substitute into $\gamma^2(1 - v^2) = 1$:
> $$\cosh^2\varphi\,(1 - v^2) = 1 \quad\Longrightarrow\quad \cosh^2\varphi - \cosh^2\varphi\,v^2 = 1.$$
> Compare with the hyperbolic identity $\cosh^2\varphi - \sinh^2\varphi = 1$. The two right-hand sides are both $1$, so $\cosh^2\varphi\,v^2 = \sinh^2\varphi$, giving (taking positive roots for $\varphi, v > 0$)
> $$\sinh\varphi = \cosh\varphi\cdot v = \gamma v.$$
> Then
> $$\tanh\varphi = \frac{\sinh\varphi}{\cosh\varphi} = \frac{\gamma v}{\gamma} = v.$$
> All three relations $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$, $v = \tanh\varphi$ are thus equivalent, any one implying the other two.

**Step 2: the logarithmic form and the bijection.**

> [!note]- Derivation
> From $v = \tanh\varphi = \frac{e^{\varphi} - e^{-\varphi}}{e^{\varphi} + e^{-\varphi}}$, cross-multiply: $v(e^{\varphi} + e^{-\varphi}) = e^{\varphi} - e^{-\varphi}$, so $e^{\varphi}(1 - v) = e^{-\varphi}(1 + v)$, giving
> $$e^{2\varphi} = \frac{1 + v}{1 - v}, \qquad \varphi = \tfrac12\ln\!\left(\frac{1 + v}{1 - v}\right) = \tanh^{-1}v.$$
> As $v$ ranges over $(-1, 1)$: at $v \to -1^+$, $\frac{1+v}{1-v} \to 0^+$ so $\varphi \to -\infty$; at $v = 0$, $\varphi = 0$; at $v \to 1^-$, $\frac{1+v}{1-v} \to +\infty$ so $\varphi \to +\infty$. The map $v \mapsto \varphi$ is strictly increasing and continuous, hence a bijection $(-1, 1) \to \mathbb{R}$.
>
> *Graph in words:* $\varphi(v)$ passes through the origin with slope $1$ (since $\tanh^{-1}v \approx v$ for small $v$), is odd, and has vertical asymptotes at $v = \pm 1$ — it rises gently near the origin and shoots to $\pm\infty$ as $v$ approaches $\pm 1$. The bounded velocity interval is unfolded onto the entire line.

**Step 3: the Doppler factor.**

> [!note]- Derivation
> The Doppler factor is the eigenvalue of the boost on the forward null direction,
> $$k = e^{\varphi} = \cosh\varphi + \sinh\varphi = \gamma + \gamma v = \gamma(1 + v).$$
> Using $\gamma = [(1-v)(1+v)]^{-1/2}$,
> $$k = \gamma(1 + v) = \frac{1 + v}{\sqrt{(1-v)(1+v)}} = \sqrt{\frac{1 + v}{1 - v}}.$$
> (This is consistent with $e^{2\varphi} = \frac{1+v}{1-v}$ from Step 2, so $k = e^{\varphi} = \sqrt{e^{2\varphi}} = \sqrt{\frac{1+v}{1-v}}$.) Hence the rapidity is the logarithm of the Doppler factor,
> $$\varphi = \ln k.$$
> A quantity that *multiplies* under composition (the Doppler factor) has the additive group coordinate (rapidity) as its logarithm.

**Step 4: the hyperbolic-angle picture.**

> [!note]- Derivation
> On the unit circle $x^2 + y^2 = 1$, a point is $(\cos\theta, \sin\theta)$, and the parameter $\theta$ is the arc length from $(1, 0)$, equivalently twice the area of the circular sector swept out. On the unit hyperbola $t^2 - x^2 = 1$ (upper branch, $t \ge 1$), a point is $(\cosh\varphi, \sinh\varphi)$ — this lies on the hyperbola because $\cosh^2\varphi - \sinh^2\varphi = 1$ — and $\varphi$ is the analogous "hyperbolic angle": twice the area of the hyperbolic sector bounded by the $t$-axis, the hyperbola, and the ray to $(\cosh\varphi, \sinh\varphi)$. So rapidity is to the hyperbola exactly what angle is to the circle: the natural arc-length / sector-area parameter.
>
> The velocity is the *slope* of the ray to the point, $x/t = \sinh\varphi/\cosh\varphi = \tanh\varphi = v$. The asymptotes of the hyperbola are the null lines $t = \pm x$, of slope $\pm 1$. As $\varphi \to \infty$ the point $(\cosh\varphi, \sinh\varphi)$ runs off to infinity along the upper branch, its ray's slope approaching $1$ but never reaching it — which is exactly the velocity ceiling $v = \tanh\varphi < 1$. The unreachable speed of light is the asymptote of the hyperbola, approached as the hyperbolic angle goes to infinity. A boost is a "rotation" by the hyperbolic angle $\varphi$ along this hyperbola, sliding points up the branch toward the asymptote.

> [!note]- Complete formal solution
> *Three relations.* From $\gamma = \cosh\varphi$ and $\gamma^2(1-v^2) = 1$: $\cosh^2\varphi - \cosh^2\varphi\,v^2 = 1 = \cosh^2\varphi - \sinh^2\varphi$, so $\sinh\varphi = \gamma v$ and $\tanh\varphi = v$. *Logarithmic form.* $v = \tanh\varphi \Rightarrow e^{2\varphi} = (1+v)/(1-v)$, so $\varphi = \tfrac12\ln\frac{1+v}{1-v} = \tanh^{-1}v$, a strictly increasing bijection $(-1,1) \to \mathbb{R}$ with asymptotes at $v = \pm 1$. *Doppler.* $k = e^\varphi = \cosh\varphi + \sinh\varphi = \gamma(1+v) = \sqrt{(1+v)/(1-v)}$, so $\varphi = \ln k$. *Geometry.* $(\cosh\varphi, \sinh\varphi)$ lies on $t^2 - x^2 = 1$ with $\varphi$ the hyperbolic-sector area (the hyperbolic angle); velocity is the slope $\tanh\varphi$, and the velocity ceiling $v < 1$ is the hyperbola approaching its null asymptote $t = x$ as $\varphi \to \infty$. $\blacksquare$

---

# Key Takeaways

**The three rapidity relations are one identity, anchored to $\cosh^2 - \sinh^2 = 1$.** The reusable fluency is that $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$, and $v = \tanh\varphi$ are not three facts to memorise but one fact — the hyperbolic identity $\cosh^2 - \sinh^2 = 1$ matched against the kinematic identity $\gamma^2(1 - v^2) = 1$ — so any one of them regenerates the others in a line. The pair "$\gamma$ with $\gamma v$" plays the role of "$\cosh\varphi$ with $\sinh\varphi$", and the Lorentz factor's defining relation $\gamma^2(1-v^2)=1$ is literally the hyperbolic Pythagorean identity. When you need a rapidity relation and cannot recall it, write $\cosh^2 - \sinh^2 = 1$ and the kinematic identity side by side; the relation falls out.

**A quantity that multiplies under composition has its logarithm as the additive parameter.** The Doppler factor $k = e^{\varphi}$ multiplies when boosts compose, and its logarithm $\varphi$ adds — the rapidity is $\ln k$. This is a recurring structural signal: whenever a one-parameter family of transformations acts by *scaling* some quantity (here, the frequency of light on a null direction), the scale factors multiply, so their logarithm is the canonical additive coordinate on the group. The same pattern underlies decibels (logarithm of a power ratio that multiplies), the rapidity-like "celerity" variables in fluid dynamics, and the generator of any one-parameter scaling group. Spotting a multiplicative composition law tells you to take a logarithm to linearise it.

**Rapidity is the hyperbolic angle, and the speed of light is the hyperbola's asymptote.** The geometric picture to carry is that velocity space in $1+1$ dimensions is the unit hyperbola $t^2 - x^2 = 1$, points on it are $(\cosh\varphi, \sinh\varphi)$, and rapidity is the hyperbolic-sector area — the exact analogue of the circular angle. The velocity is the slope of the ray to the point, and the null asymptotes $t = \pm x$ (slope $\pm 1$) are the speed of light, approached as the hyperbolic angle runs to infinity but never reached. This single image explains at a glance why velocity is bounded but rapidity is not, why boosts "rotate" along the hyperbola, and why composing boosts adds the hyperbolic angles. It is the relativistic counterpart of the unit-circle picture of rotations, and internalising it makes the boundedness of velocity and the unboundedness of rapidity geometrically obvious rather than algebraically surprising.
