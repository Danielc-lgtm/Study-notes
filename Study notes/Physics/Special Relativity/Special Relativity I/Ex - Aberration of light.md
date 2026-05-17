---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Thm - Relativistic Velocity Addition"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$. A light ray travels in frame $S$ at an angle $\theta$ to the $x$-axis, so its velocity has components $(\cos\theta, \sin\theta)$. Frame $S'$ moves at velocity $v$ along the $x$-axis of $S$.

1. By transforming the components of the light ray's velocity, find the angle $\theta'$ the same ray makes with the $x'$-axis in $S'$. Show that
$$\cos\theta' = \frac{\cos\theta - v}{1 - v\cos\theta}.$$
2. Verify the speed of the ray in $S'$ is still $1$ — light stays light.
3. **The headlight effect.** A source at rest in $S'$ emits light *isotropically* — uniformly in all directions. Show that an observer in $S$, towards whom the source moves at speed $v$, sees the light beamed forward into a narrow cone, and find the half-angle of the cone that contains half the light, in the ultra-relativistic limit $v \to 1$.

**Recall:**

Aberration is the transformation of a *direction* under a boost.

![[Def - The Lorentz Transformation#The Definition]]

A light ray's worldline is **null** ([[Def - Classification of Four-Vectors]]): its velocity has magnitude $1$ in every frame. The transformation of velocity *components* is governed by [[Thm - Relativistic Velocity Addition|the velocity-addition law]] — the $x$-component adds relativistically, the transverse component picks up a factor of $\gamma$ in the denominator.

---

# Convergent Strategy

**Problem class.** A *compute-a-relativistic-effect* problem where the effect is a change of *direction* rather than of speed. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] routes velocity-component questions through the velocity-addition machinery.

**Assumption pattern.** A velocity with both a longitudinal and a transverse component is given, and the question asks for the direction in a boosted frame. The signpost: "what angle does it make in $S'$" means transform *both* velocity components and take the ratio.

**Theorem routing.** Transform $v_x = \cos\theta$ and $v_y = \sin\theta$ separately to $S'$: the $x$-component by the [[Thm - Relativistic Velocity Addition|collinear addition law]], the $y$-component by the transverse rule $v_y' = v_y/[\gamma(1+\cdots)]$. Then $\cos\theta' = v_x'/|\mathbf{v}'| = v_x'$ since the speed stays $1$.

**Key decision point.** The non-obvious point is that the *transverse* velocity component does not stay fixed — even though transverse *lengths* are uncontracted. The transverse component transforms because *time* dilates: $v_y' = \Delta y'/\Delta t' = \Delta y/[\gamma(\Delta t - v\Delta x)]$, and the $\gamma$ in the denominator is what tilts the ray forward.

---

# Legal Operations Used

1. **Add velocities relativistically** — the $x$-component of the light ray's velocity transforms by the collinear addition law.

2. **Apply the Lorentz transformation** to velocity components, including the transverse rule for $v_y$.

3. **Classify a four-vector** — the light ray is null, so its speed is $1$ in every frame, which is what lets $\cos\theta' = v_x'$.

4. **Work in the rest frame, then boost out** — part 3 starts with the source's isotropic emission in its rest frame $S'$.

---

# Hints

> [!note]- Hint 1
> The light ray's velocity in $S$ is $\mathbf{v} = (\cos\theta, \sin\theta)$. To get its velocity in $S'$, transform each component. For $v_x$, use the collinear velocity-addition law (the frame $S'$ moves at $+v$, so the ray's $x$-velocity in $S'$ is $(\cos\theta - v)/(1 - v\cos\theta)$). For $v_y$: from $v_y' = \Delta y'/\Delta t'$ with $\Delta y' = \Delta y$ and $\Delta t' = \gamma(\Delta t - v\Delta x)$, get $v_y' = \sin\theta/[\gamma(1 - v\cos\theta)]$.

> [!note]- Hint 2
> Compute $v_x'^2 + v_y'^2$ and show it equals $1$. You will need $\gamma^2 = 1/(1-v^2)$ and $\cos^2\theta + \sin^2\theta = 1$. The denominators are the same; expand the numerator $(\cos\theta - v)^2 + \sin^2\theta/\gamma^2$.

> [!note]- Hint 3
> An isotropic source emits equally into all directions; in $S'$, half the light goes into the forward hemisphere $\theta' \in [0, \pi/2]$, i.e. the cone bounded by $\theta' = \pi/2$. Use the aberration formula *inverted* to find what $\theta$ in $S$ corresponds to $\theta' = \pi/2$: set $\cos\theta' = 0$ and solve for $\cos\theta$. That $\theta$ is the half-angle of the forward cone in $S$. Take $v \to 1$.

---

# Solution

A boost changes the *direction* of a light ray, not just speeds — because the transverse velocity component transforms (time dilates) even though transverse lengths do not contract. A source rushing towards you appears to beam its light forward.

**Step 1: The aberration formula.**

> [!note]- Derivation
> The light ray has velocity $\mathbf{v} = (\cos\theta, \sin\theta)$ in $S$, with $|\mathbf{v}| = 1$. Frame $S'$ moves at $+v$ along $x$. Transform each component.
>
> *Longitudinal.* The $x$-component is a velocity collinear with the boost, so by [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] (combining $\cos\theta$ with a frame velocity $v$, the ray's $x$-velocity in $S'$ is the addition law with $-v$):
> $$v_x' = \frac{\cos\theta - v}{1 - v\cos\theta}.$$
>
> *Transverse.* The $y$-component is $v_y' = \Delta y'/\Delta t'$. Under the [[Def - The Lorentz Transformation|Lorentz transformation]], $\Delta y' = \Delta y$ (transverse lengths untouched) but $\Delta t' = \gamma(\Delta t - v\Delta x)$. So
> $$v_y' = \frac{\Delta y}{\gamma(\Delta t - v\Delta x)} = \frac{\Delta y/\Delta t}{\gamma(1 - v\,\Delta x/\Delta t)} = \frac{v_y}{\gamma(1 - v\,v_x)} = \frac{\sin\theta}{\gamma(1 - v\cos\theta)}.$$
> The transverse component is *not* invariant: it carries a factor $1/\gamma$ from time dilation.
>
> Since (Step 2) the speed in $S'$ is still $1$, the new direction satisfies $\cos\theta' = v_x'/|\mathbf{v}'| = v_x'$:
> $$\boxed{\;\cos\theta' = \frac{\cos\theta - v}{1 - v\cos\theta}\;}$$
> and correspondingly $\sin\theta' = \dfrac{\sin\theta}{\gamma(1 - v\cos\theta)}$. This is the **aberration of light**: the same ray makes different angles in the two frames.

**Step 2: The speed of the ray is $1$ in $S'$.**

> [!note]- Derivation
> Compute the squared speed in $S'$:
> $$v_x'^2 + v_y'^2 = \frac{(\cos\theta - v)^2}{(1-v\cos\theta)^2} + \frac{\sin^2\theta}{\gamma^2(1-v\cos\theta)^2} = \frac{(\cos\theta - v)^2 + (1-v^2)\sin^2\theta}{(1-v\cos\theta)^2},$$
> using $1/\gamma^2 = 1 - v^2$. Expand the numerator:
> $$(\cos\theta - v)^2 + (1-v^2)\sin^2\theta = \cos^2\theta - 2v\cos\theta + v^2 + \sin^2\theta - v^2\sin^2\theta.$$
> Group $\cos^2\theta + \sin^2\theta = 1$ and $v^2 - v^2\sin^2\theta = v^2\cos^2\theta$:
> $$= 1 - 2v\cos\theta + v^2\cos^2\theta = (1 - v\cos\theta)^2.$$
> Hence $v_x'^2 + v_y'^2 = (1-v\cos\theta)^2/(1-v\cos\theta)^2 = 1$. The light ray travels at speed $1$ in $S'$ as well — exactly as the [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]] requires. A boost re-aims the ray but cannot change its speed, because a null worldline stays null ([[Def - Classification of Four-Vectors]]).

**Step 3: The headlight effect.**

> [!note]- Derivation
> A source at rest in $S'$ emits light **isotropically**: equal intensity into every direction $\theta'$. In particular, exactly half the light goes into the forward hemisphere $0 \le \theta' \le \pi/2$ — the cone whose boundary is $\theta' = \pi/2$.
>
> Now ask: in frame $S$, towards which the source moves at speed $v$, what is the half-angle $\theta$ of the cone containing that same half of the light? It is the angle $\theta$ that the boundary ray $\theta' = \pi/2$ has in $S$. Set $\cos\theta' = 0$ in the aberration formula and solve for $\cos\theta$. The aberration formula inverted (swap roles, $v \to -v$):
> $$\cos\theta = \frac{\cos\theta' + v}{1 + v\cos\theta'}.$$
> With $\cos\theta' = 0$:
> $$\cos\theta = \frac{0 + v}{1 + 0} = v.$$
> So in $S$, half of all the source's light is concentrated into the forward cone of half-angle $\theta$ with $\cos\theta = v$. For a slow source ($v \approx 0$), $\cos\theta \approx 0$, $\theta \approx \pi/2$ — still roughly a hemisphere. But as $v \to 1$, $\cos\theta \to 1$, so $\theta \to 0$: **the forward cone collapses to a pencil-thin beam.**
>
> Quantitatively, in the ultra-relativistic limit write $v = 1 - \varepsilon$ with $\varepsilon \ll 1$. Then $\cos\theta = v = 1 - \varepsilon$, and for small $\theta$, $\cos\theta \approx 1 - \theta^2/2$, so $\theta^2/2 \approx \varepsilon$, giving
> $$\theta \approx \sqrt{2\varepsilon} = \sqrt{2(1-v)}.$$
> A more standard form uses $\gamma$: since $1 - v = 1 - v \approx (1-v^2)/2 = 1/(2\gamma^2)$ for $v \to 1$, one gets $\theta \approx 1/\gamma$. Half the source's light is squeezed into a forward cone of half-angle $\sim 1/\gamma$. This is the **relativistic headlight (or beaming) effect**: a fast-moving source appears as a searchlight aimed in its direction of motion. It is why the jets of light from relativistic astrophysical sources are so sharply collimated, and why synchrotron radiation from a circulating relativistic electron arrives in brief, forward-beamed flashes.

> [!note]- Complete formal solution
> A light ray with velocity $(\cos\theta,\sin\theta)$ in $S$ has, in $S'$ (moving at $+v$): $v_x' = (\cos\theta-v)/(1-v\cos\theta)$ by collinear velocity addition, and $v_y' = \sin\theta/[\gamma(1-v\cos\theta)]$ since $\Delta y' = \Delta y$ but $\Delta t' = \gamma(\Delta t - v\Delta x)$. Then $v_x'^2 + v_y'^2 = [(\cos\theta-v)^2 + (1-v^2)\sin^2\theta]/(1-v\cos\theta)^2 = (1-v\cos\theta)^2/(1-v\cos\theta)^2 = 1$, so the speed is $1$ and $\cos\theta' = v_x' = (\cos\theta-v)/(1-v\cos\theta)$. For an isotropic source at rest in $S'$, half the light fills $\theta' \le \pi/2$; the boundary $\cos\theta' = 0$ corresponds in $S$ to $\cos\theta = (\cos\theta'+v)/(1+v\cos\theta') = v$, so half the light lies in a forward cone of half-angle $\theta$ with $\cos\theta = v$. As $v\to 1$, $\theta \approx \sqrt{2(1-v)} \approx 1/\gamma \to 0$ — the headlight effect. $\blacksquare$

---

# Key Takeaways

**A boost transforms directions because the transverse velocity component is not invariant — and the culprit is time dilation, not length contraction.** It is tempting to think that since transverse *lengths* are unchanged by a boost, transverse *velocities* are too. They are not. A transverse velocity is $\Delta y/\Delta t$, and while $\Delta y$ is indeed unchanged, $\Delta t$ transforms — it picks up the factor $\gamma(1 - v\cos\theta)$. So $v_y' = v_y/[\gamma(1-v\cos\theta)]$: the transverse velocity changes, carried along by the transformation of *time*. This is the general lesson for any "transverse" quantity in relativity: check whether it is built from a time, because lengths perpendicular to the boost are safe but durations never are. Aberration, the transverse Doppler effect, and the headlight effect all trace to this single fact.

**Light stays light: a boost re-aims a ray but cannot change its speed.** Step 2's verification that $|\mathbf{v}'| = 1$ is not a lucky coincidence — it is forced, because a light ray's worldline is *null* ([[Def - Classification of Four-Vectors]]), and the null condition $X\cdot X = 0$ is Lorentz invariant. Every boost maps the light cone to itself. So whatever a boost does to a light ray, it does it *along the light cone*: it can rotate the ray's direction, blue- or red-shift its frequency, but never make it sub- or super-luminal. This is the geometric content of the second postulate, and it is the reason the aberration formula always returns a unit-speed velocity. When transforming a light ray, you may take its speed as fixed at $1$ and solve only for its direction — the speed is not a free quantity.

**Aberration concentrates a moving source's light forward into a cone of half-angle $\sim 1/\gamma$ — the headlight effect.** An isotropic emitter, viewed from a frame it rushes towards, does not look isotropic: its light is swept into a forward beam, and at speed $v$ the cone containing half the light has $\cos\theta = v$, collapsing to half-angle $\sim 1/\gamma$ as $v \to c$. The trigger for this kind of analysis is any "what does a fast-moving source look like" question: emission is simplest in the source's rest frame (isotropic, symmetric), and the boost to the observer's frame tilts every ray forward by the aberration formula. The effect is not a curiosity — it is why relativistic jets in astrophysics appear as thin collimated beams, why a synchrotron electron radiates in sharp forward pulses, and why a fast-moving emitter is seen far more brightly head-on than from behind. The general pattern: describe emission isotropically in the rest frame, then aberrate, and the angular distribution in the lab frame follows.
