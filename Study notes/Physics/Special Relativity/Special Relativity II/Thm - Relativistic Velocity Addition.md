---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and restore $c$ where a formula is more recognisable with it. Three inertial frames $S$, $S'$, $S''$ are in standard configuration along a common $x$-axis: $S'$ moves at velocity $v$ relative to $S$, and a particle (or $S''$) moves at velocity $u'$ relative to $S'$; $u$ denotes its velocity relative to $S$. All velocities are collinear (along $x$). The [[Def - The Lorentz Transformation|Lorentz transformation]] from $S'$ to $S$ is the inverse boost $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$, with $\gamma = (1-v^2)^{-1/2}$. The **rapidity** of a velocity $w$ is $\varphi_w = \tanh^{-1} w$, with $w = \tanh\varphi_w$, $\gamma_w = \cosh\varphi_w$, $\gamma_w w = \sinh\varphi_w$ ([[Def - Rapidity]]). Full registry on [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]].

---

# Statement

> **Relativistic velocity addition (collinear).** Let a particle move at velocity $u'$ in an inertial frame $S'$, and let $S'$ move at velocity $v$ relative to an inertial frame $S$, the two velocities being collinear. Then the particle's velocity in $S$ is
> $$u = \frac{u' + v}{1 + u'v} \qquad\left(\text{with } c: \ u = \frac{u' + v}{1 + u'v/c^2}\right),$$
> *not* the Galilean sum $u' + v$. Two structural consequences hold:
> - **$c$ is a fixed point:** if either $u' = c$ or $v = c$, then $u = c$.
> - **$c$ is a ceiling:** if $|u'| < c$ and $|v| < c$, then $|u| < c$; explicitly $c - u = \dfrac{(c - u')(c - v)\,c}{c^2 + u'v} > 0$.
>
> Equivalently, in terms of [[Def - Rapidity|rapidity]] $\varphi = \tanh^{-1}(w/c)$, collinear boosts compose by **adding rapidities**: $\varphi_u = \varphi_{u'} + \varphi_v$, so $u = c\tanh(\varphi_{u'} + \varphi_v)$.

---

# Motivation

The Galilean rule for combining velocities — if you walk at $u'$ down a train moving at $v$, your speed over the ground is $u' + v$ — is so deeply intuitive that it feels like a theorem of arithmetic rather than a law of physics. It is, in fact, a low-speed approximation, and the place it fails is precisely the place relativity was built to handle: light. Shine a torch forward from a train moving at $v$; the Galilean rule predicts the light travels at $c + v$ over the ground. But the second postulate says light travels at $c$ in *every* frame, ground included. The Galilean rule and the constancy of light are flatly incompatible, and the velocity-addition law is the formula that replaces the rule so that the two are reconciled.

The theorem answers the question "what is the correct law of combining collinear velocities?", and its two structural consequences are the whole reason it matters. First, it must reproduce the constancy of light: feeding in $u' = c$ has to give $u = c$, and it does — $c$ is a *fixed point* of the addition. Second, it must enforce the cosmic speed limit: combining two sub-light velocities must never produce a faster-than-light one, or relativity would let you bootstrap past $c$ by hopping from frame to frame to frame. The factorisation $c - u \propto (c-u')(c-v)$ makes this transparent — sub-light inputs give a strictly sub-light output, so $c$ is an *unreachable ceiling*. These two facts, fixed point and ceiling, are why you cannot catch up to a light beam and cannot accelerate a massive particle to $c$ by any chain of boosts.

There is a deeper reading that the rapidity formulation supplies, and it is the one a mathematician should keep. The reason velocities add *non*-linearly is that velocity is the wrong coordinate on the boost group. The right coordinate is rapidity, and in rapidity the law is dead simple: rapidities just *add*. Velocity addition looks complicated only because $u = \tanh\varphi$ is a nonlinear function of the thing that actually adds. This is the exact analogue of rotations: angles add, but the slopes $\tan\theta$ of the rotated axes do not, and "slope addition" is a messy formula that hides the simple "angle addition" underneath. The hyperbolic-tangent addition formula $\tanh(\varphi_{u'} + \varphi_v) = (\tanh\varphi_{u'} + \tanh\varphi_v)/(1 + \tanh\varphi_{u'}\tanh\varphi_v)$ *is* the velocity-addition law; the theorem is the statement that boosts are hyperbolic rotations and rapidity is their angle.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a velocity is given relative to a frame that is itself moving relative to the frame you want the answer in". Its disguises:

The first disguised source is **"a projectile is fired from a moving platform"**. A bullet, rocket, or light pulse emitted at speed $u'$ in the rest frame of a ship moving at $v$ has ground-frame speed given by the law, not by $u' + v$. The bridge is "emission speed in the platform frame $=$ $u'$, platform speed $=$ $v$". *Example problem:* a rocket moving at $0.8c$ fires a missile forward at $0.5c$ relative to itself; the ground sees the missile at $(0.5 + 0.8)/(1 + 0.4) = 0.93c$, not $1.3c$.

The second disguised source is **"the closing speed of two approaching objects is wanted, as reckoned in one of their rest frames"**. If two objects approach with Earth-frame speeds $u'$ and $v$ (towards each other), the speed of one *as measured in the rest frame of the other* is the relativistic combination, not the Earth-frame sum $u' + v$. The bridge is to sit in one object's rest frame and ask how fast the other approaches; this is a *boost of the frame*, governed by the same formula. *Example problem:* two ships each at $0.7c$ towards each other; one reckons the other's approach speed as $(0.7 + 0.7)/(1 + 0.49) = 0.94c$, comfortably below $c$, not $1.4c$ ([[Ex - Two spaceships and the relativistic closing speed]]).

The third disguised source is **"several boosts must be composed in succession"**. A chain of frames, each moving relative to the previous, demands iterated velocity addition; the natural tool is rapidity, where the chain becomes a sum. The bridge is that composing boosts $=$ adding rapidities. *Example problem:* $N$ successive collinear boosts each of velocity $w$ give net rapidity $N\varphi_w$ and net velocity $\tanh(N\varphi_w) \to c$ as $N \to \infty$ — many boosts approach but never reach $c$.

**Targets (Output Amplification)**

The conclusion is "$u = (u' + v)/(1 + u'v)$".

Combine the conclusion with **the fixed-point property** to recover the second postulate as a *theorem*. Setting $u' = c$ gives $u = c$ identically; so the constancy of light's speed, taken as a postulate in [[Def - Inertial Frame and the Postulates of Special Relativity|the postulates]], re-emerges as a consequence of the addition law (which itself follows from the Lorentz transformation, which followed from the postulates). The further result closes the logical loop and shows the structure is self-consistent. The combination is nonobvious because it derives a postulate from a formula. *Example:* verifying $u = c$ for any $v$ when $u' = c$.

Combine the conclusion with **the ceiling property** to forbid faster-than-light bootstrapping. The factorisation $c - u = (c-u')(c-v)c/(c^2 + u'v)$ shows sub-light plus sub-light stays sub-light; iterating, *no finite chain of sub-light boosts reaches $c$*. The further result is the kinematic half of "you cannot accelerate a massive particle to light speed" (the dynamical half is that it would take infinite energy). The combination is useful because it converts a single inequality into a global impossibility. *Example:* the $N$-boost chain above, and the [[Def - Causality and the Light Cone|light-cone]] statement that causal worldlines never cross $45^\circ$.

Combine the conclusion with **rapidity additivity** to linearise problems and connect to geometry. Writing $u = \tanh\varphi$ turns the nonlinear law into $\varphi_u = \varphi_{u'} + \varphi_v$, which makes iterated boosts, inverse boosts, and the "approach to $c$" all trivial, and exposes velocity space as hyperbolic geometry with rapidity as distance. The further result is the gateway to the [[Def - Rapidity|rapidity]] formalism, the Wigner rotation, and Thomas precession. The combination is nonobvious because a messy rational function turns out to be a hidden addition. *Example:* deriving the law itself from $\tanh(\varphi_{u'} + \varphi_v)$, the cleanest proof.

---

# Why Is It True

The result is forced the moment you remember what "velocity" means — a ratio of a space-step to a time-step along a worldline — and that the Lorentz transformation mixes space and time. **The Galilean rule fails because both the numerator and the denominator of $\Delta x/\Delta t$ transform; velocity addition is what you get when you transform the ratio honestly instead of just the top.**

Trace the particle's motion in $S'$: it advances $\Delta x' = u'\,\Delta t'$ for each time-step $\Delta t'$ (that is what $u'$ means). Now ask how $S$ sees this same pair of events at the ends of the step. The [[Def - The Lorentz Transformation|Lorentz transformation]] gives the $S$-step from the $S'$-step:
$$\Delta x = \gamma(\Delta x' + v\,\Delta t'), \qquad \Delta t = \gamma(\Delta t' + v\,\Delta x').$$
The particle's $S$-velocity is the ratio of these:
$$u = \frac{\Delta x}{\Delta t} = \frac{\gamma(\Delta x' + v\,\Delta t')}{\gamma(\Delta t' + v\,\Delta x')} = \frac{\Delta x'/\Delta t' + v}{1 + v\,\Delta x'/\Delta t'} = \frac{u' + v}{1 + u'v}.$$
The $\gamma$'s cancel — velocity is a ratio, so the common stretch factor drops out — and the Galilean numerator $u' + v$ survives, but a *new denominator* $1 + u'v$ appears, coming entirely from the fact that $\Delta t$ also mixes in some $\Delta x'$. That denominator is the relativity of simultaneity at work on the time-step, and it is the whole difference from Galileo. In the limit $u'v \ll 1$ (low speeds, $c \to \infty$) the denominator is $\approx 1$ and the Galilean rule is recovered; near $c$ it is the denominator that tames the sum.

Why $c$ is a fixed point is then immediate: put $u' = c = 1$, and $u = (1 + v)/(1 + v) = 1 = c$ for *every* $v$. The denominator grows in exact step with the numerator, pinning light at $c$ in all frames. Why $c$ is a ceiling is the factorisation
$$c - u = c - \frac{u' + v}{1 + u'v/c^2} = \frac{c(1 + u'v/c^2) - (u' + v)}{1 + u'v/c^2} = \frac{(c - u')(c - v)}{c(1 + u'v/c^2)} = \frac{(c-u')(c-v)\,c}{c^2 + u'v},$$
which is a ratio of positive quantities when $u', v < c$ (so $c - u', c - v > 0$ and $c^2 + u'v > 0$), giving $u < c$. The same algebra with $-c$ gives $u > -c$. So sub-light in, sub-light out, always.

The rapidity reading explains *why* the formula has this exact shape rather than some other speed-limited interpolation. A boost is a hyperbolic rotation of the $(t,x)$-plane through "angle" $\varphi$, and composing two collinear boosts is composing two hyperbolic rotations, which adds the angles: $\varphi_u = \varphi_{u'} + \varphi_v$. Converting back with $u = \tanh\varphi$ and the addition formula for $\tanh$ reproduces the law exactly. In this picture the fixed point is $\tanh\varphi \to 1$ as $\varphi \to \infty$ (light is rapidity infinity, the asymptote of the hyperbola), and the ceiling is that a finite sum of finite rapidities is finite, so $\tanh$ of it is strictly below $1$. The velocity-addition law is just the angle-addition law of hyperbolic rotations, viewed through the nonlinear coordinate $\tanh$.

---

# What Makes This Hard

The derivation is a two-line ratio, and the only place to stumble is mechanical: one must transform *both* $\Delta x$ and $\Delta t$ and take their quotient, not transform $\Delta x$ alone and divide by an untransformed $\Delta t$ (which would give the wrong, Galilean-looking answer). The genuinely non-obvious content is conceptual — that the numerator is Galilean but a new denominator appears from the mixing of time and space — and that "closing speed" problems require a *boost*, not a Galilean sum of two Earth-frame speeds; the common error is to compute the closing speed of two approaching objects as $u' + v$ rather than $(u'+v)/(1+u'v)$. A subtler trap is to expect the law to be commutative and associative in *more than one dimension*: collinearly it is, but non-collinear boosts compose to a boost *plus a rotation* (the Wigner rotation), so the naive expectation fails off-axis.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the particle's worldline in $S'$ as $x' = u't'$, transform both coordinates to $S$ with the inverse boost, and take the ratio $u = x/t$ (equivalently the ratio of differentials $dx/dt$). The $\gamma$'s cancel; the answer is $(u' + v)/(1 + u'v)$. For the structural facts, substitute $u' = c$ and factorise $c - u$.

**Subgoal decomposition:**

1. **Write the worldline in $S'$.** A particle at velocity $u'$ in $S'$ satisfies $x' = u't'$ (through the origin), or $dx' = u'\,dt'$.
   - *Hint:* Velocity in $S'$ is $u' = dx'/dt'$ by definition.
   - *Why needed:* It encodes the input velocity as a relation between the primed coordinates.

2. **Transform both coordinates to $S$.** Apply the inverse boost $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$.
   - *Hint:* You want $S$-coordinates from $S'$-coordinates, so use the inverse boost (sign $+v$).
   - *Why needed:* It expresses the $S$-step in terms of the $S'$-step; transforming *both* is essential.

3. **Take the ratio and substitute the worldline.** Form $u = x/t = \gamma(x' + vt')/\gamma(t' + vx')$, divide top and bottom by $t'$, and put $x'/t' = u'$.
   - *Hint:* The factors of $\gamma$ cancel because velocity is a ratio.
   - *Why needed:* This produces $u = (u' + v)/(1 + u'v)$, the theorem.

4. **Check the fixed point and ceiling.** Set $u' = c$ to get $u = c$; factor $c - u = (c-u')(c-v)c/(c^2 + u'v)$ to get $u < c$ for sub-light inputs.
   - *Hint:* For the ceiling, combine the fraction $c - u$ over a common denominator and factor the numerator.
   - *Why needed:* These are the two structural consequences that make the law physically meaningful.

5. **(Rapidity route.)** Replace each velocity by its rapidity and use $\tanh(\varphi_{u'} + \varphi_v)$.
   - *Hint:* $u = \tanh\varphi_u$, and the boost matrices multiply to add rapidities.
   - *Why needed:* It is the cleanest derivation and explains the formula's shape.

---

# Lemma Decomposition

> [!note]- Lemma 1: Velocity transforms by the ratio of transformed coordinate differences
> **Statement:** For a particle moving along $x$, its velocity in $S$ is $u = dx/dt = \dfrac{\gamma(dx' + v\,dt')}{\gamma(dt' + v\,dx')}$, where $dx', dt'$ are its coordinate differentials in $S'$.
>
> **Hint:** Differentiate the inverse Lorentz transformation and divide.
>
> **Why needed:** It is the engine of the whole theorem — velocity is a ratio of transformed differentials, and the cancellation of $\gamma$ happens here.
>
> > [!note]- Full proof
> > The inverse [[Def - The Lorentz Transformation|Lorentz transformation]] is $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$ with constant $\gamma, v$. Taking differentials, $dx = \gamma(dx' + v\,dt')$ and $dt = \gamma(dt' + v\,dx')$. The $S$-velocity is the ratio $u = dx/dt = \gamma(dx' + v\,dt')/[\gamma(dt' + v\,dx')]$; the factor $\gamma$ is common to numerator and denominator and cancels, leaving $u = (dx' + v\,dt')/(dt' + v\,dx')$. $\blacksquare$

> [!note]- Lemma 2: The collinear addition formula
> **Statement:** With $u' = dx'/dt'$, the ratio in Lemma 1 equals $u = (u' + v)/(1 + u'v)$.
>
> **Hint:** Divide numerator and denominator of Lemma 1 by $dt'$.
>
> **Why needed:** It is the theorem's formula.
>
> > [!note]- Full proof
> > From Lemma 1, $u = (dx' + v\,dt')/(dt' + v\,dx')$. Divide top and bottom by $dt'$: $u = (dx'/dt' + v)/(1 + v\,dx'/dt')$. Since $dx'/dt' = u'$, this is $u = (u' + v)/(1 + u'v)$. Restoring $c$ (each velocity carries a $1/c$ in the cross term): $u = (u' + v)/(1 + u'v/c^2)$. $\blacksquare$

> [!note]- Lemma 3: Fixed point and ceiling
> **Statement:** If $u' = c$ then $u = c$ for all $v$; and if $|u'|, |v| < c$ then $|u| < c$, via $c - u = (c-u')(c-v)c/(c^2 + u'v)$.
>
> **Hint:** Substitute $u' = c$ directly; for the ceiling, write $c - u$ over a common denominator and factor.
>
> **Why needed:** These are the two structural consequences that distinguish the relativistic law from any arbitrary speed-limited interpolation.
>
> > [!note]- Full proof
> > *Fixed point.* With $u' = c$: $u = (c + v)/(1 + cv/c^2) = (c + v)/(1 + v/c) = (c + v)/[(c + v)/c] = c$, for every $v$ (and symmetrically $v = c \Rightarrow u = c$). *Ceiling.* Compute
> > $$c - u = c - \frac{u' + v}{1 + u'v/c^2} = \frac{c(1 + u'v/c^2) - (u' + v)}{1 + u'v/c^2} = \frac{c + u'v/c - u' - v}{1 + u'v/c^2}.$$
> > The numerator is $c - u' - v + u'v/c = (c - u') - \tfrac{v}{c}(c - u') = (c - u')(1 - v/c) = (c-u')(c-v)/c$. Hence $c - u = \dfrac{(c-u')(c-v)/c}{(c^2 + u'v)/c^2} = \dfrac{(c-u')(c-v)\,c}{c^2 + u'v}$. For $|u'|, |v| < c$ the factors $c - u', c - v > 0$ and $c^2 + u'v > c^2 - c^2 = 0$, so $c - u > 0$, i.e. $u < c$. The identical computation with $-c$ gives $u > -c$. $\blacksquare$

> [!note]- Lemma 4: Rapidity additivity gives the same law
> **Statement:** With $\varphi_w = \tanh^{-1}(w/c)$, collinear boosts compose by $\varphi_u = \varphi_{u'} + \varphi_v$, and $u = c\tanh(\varphi_{u'} + \varphi_v)$ reproduces the formula.
>
> **Hint:** Multiply the two boost matrices in $(\cosh\varphi, \sinh\varphi)$ form and read off the result; then expand $\tanh$ of a sum.
>
> **Why needed:** It is the structural proof — boosts are hyperbolic rotations, rapidity is their additive angle — and it explains the algebraic shape of the law.
>
> > [!note]- Full proof
> > A collinear boost of velocity $w$ acts on $(ct, x)$ by the matrix $B(\varphi_w) = \begin{pmatrix}\cosh\varphi_w & \sinh\varphi_w\\ \sinh\varphi_w & \cosh\varphi_w\end{pmatrix}$ with $\varphi_w = \tanh^{-1}(w/c)$ ([[Def - Rapidity]]). Composing the boost $S \to S'$ (rapidity $\varphi_v$) with $S' \to S''$ (rapidity $\varphi_{u'}$) multiplies the matrices, and by the hyperbolic angle-sum identities
> > $$B(\varphi_{u'})B(\varphi_v) = \begin{pmatrix}\cosh(\varphi_{u'}+\varphi_v) & \sinh(\varphi_{u'}+\varphi_v)\\ \sinh(\varphi_{u'}+\varphi_v) & \cosh(\varphi_{u'}+\varphi_v)\end{pmatrix} = B(\varphi_{u'} + \varphi_v),$$
> > so the net boost has rapidity $\varphi_u = \varphi_{u'} + \varphi_v$. Hence $u/c = \tanh(\varphi_{u'} + \varphi_v) = \dfrac{\tanh\varphi_{u'} + \tanh\varphi_v}{1 + \tanh\varphi_{u'}\tanh\varphi_v} = \dfrac{u'/c + v/c}{1 + (u'/c)(v/c)}$, i.e. $u = (u' + v)/(1 + u'v/c^2)$, the same law. The fixed point is the asymptote $\tanh\varphi \to 1$ as $\varphi \to \infty$; the ceiling is that any finite sum of rapidities is finite, so $|\tanh| < 1$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let a particle move at velocity $u'$ along the $x'$-axis in $S'$, and let $S'$ move at velocity $v$ along the $x$-axis of $S$. The particle's worldline in $S'$ is $x' = u't'$, so along it $dx' = u'\,dt'$.
>
> By the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$ (Lemma 1), the differentials transform as $dx = \gamma(dx' + v\,dt')$, $dt = \gamma(dt' + v\,dx')$. The $S$-velocity is their ratio, with the common factor $\gamma$ cancelling:
> $$u = \frac{dx}{dt} = \frac{dx' + v\,dt'}{dt' + v\,dx'} = \frac{u' + v}{1 + u'v},$$
> on dividing through by $dt'$ and using $dx'/dt' = u'$ (Lemma 2). Restoring $c$: $u = (u' + v)/(1 + u'v/c^2)$.
>
> *Fixed point* (Lemma 3): setting $u' = c$ gives $u = (c+v)/(1 + v/c) = c$ for all $v$; light travels at $c$ in every frame.
>
> *Ceiling* (Lemma 3): $c - u = \dfrac{(c-u')(c-v)\,c}{c^2 + u'v}$, a ratio of positive quantities when $|u'|, |v| < c$, so $u < c$; symmetrically $u > -c$. Sub-light inputs give a sub-light output, and no finite chain of boosts reaches $c$.
>
> *Rapidity route* (Lemma 4): writing each velocity as $w = c\tanh\varphi_w$, the boosts are hyperbolic rotations $B(\varphi)$ whose product satisfies $B(\varphi_{u'})B(\varphi_v) = B(\varphi_{u'} + \varphi_v)$; hence $\varphi_u = \varphi_{u'} + \varphi_v$ and $u = c\tanh(\varphi_{u'} + \varphi_v)$, which expands by the $\tanh$ addition formula to the same law. This is the cleanest derivation and exhibits the fixed point ($\tanh\varphi \to 1$) and ceiling (finite rapidity sum) directly. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fizeau's experiment: light in moving water (optics, history).** Light travelling through water moving at speed $v$ has, to first order, speed $c/n + v(1 - 1/n^2)$ in the lab, where $n$ is the refractive index; the curious factor $(1 - 1/n^2)$, the *Fresnel drag coefficient*, was measured by Fizeau in 1851 and is exactly the first-order expansion of the relativistic velocity-addition law $u = (c/n + v)/(1 + v/(nc))$. The application is the bridge "speed in the medium's frame $= c/n$, medium speed $= v$", and it is historically striking because a relativistic prediction was confirmed decades before relativity, then explained by it. The exercise: expand the addition law to first order in $v$ and recover the drag coefficient.

**The relativistic rocket and the staged-boost limit (astronautics).** A rocket that performs many small velocity boosts, each $\Delta w$ in its instantaneous rest frame, accumulates rapidity additively, so after total rapidity $\varphi$ its speed is $c\tanh\varphi$ — approaching but never reaching $c$ however long it burns. The application is rapidity additivity (Lemma 4) applied to a continuous sequence of boosts; it is illuminating because it shows the speed limit is not a force opposing acceleration but a feature of how velocities compose, and that "constant proper acceleration" means constant rate of rapidity gain.

**Aberration of starlight and the headlight effect (astronomy).** The transformation of the *direction* of a velocity between frames — the relativistic aberration formula — is the two-dimensional generalisation of velocity addition, and it predicts that a fast observer sees the sky's light concentrated ahead into a forward cone (the "headlight effect"), and that stars appear shifted toward the direction of motion. The application extends the collinear law to transverse components ($u_\perp$ picks up a factor $1/\gamma(1 + u'_\parallel v)$); it is out-of-distribution because it turns velocity addition into a statement about angles and the appearance of the sky, and it is what a relativistic starship's forward view would actually show.

---

# Bridges

- **[[Def - Rapidity]]** — the variable in which this law is linear. Rapidity $\varphi = \tanh^{-1} v$ is the additive parameter of collinear boosts, and the velocity-addition formula is *exactly* the hyperbolic-tangent addition identity. The whole theorem is the statement that boosts are hyperbolic rotations and velocities are the $\tanh$ of their angles; reaching for rapidity converts every velocity-composition problem into ordinary addition, and makes the speed limit visible as the asymptote $\tanh\varphi \to 1$.

- **[[Def - Causality and the Light Cone]]** — the geometric face of the ceiling. The statement "sub-light plus sub-light stays sub-light" is the kinematic version of "causal worldlines stay inside the light cone": a chain of boosts of timelike worldlines composes to a timelike worldline, never crossing the $45^\circ$ boundary. The fixed point ($u = c$ when $u' = c$) is that null worldlines map to null worldlines under every boost — the light cone is Lorentz-invariant.

- **[[Def - The Lorentz Transformation]]** — the source of the formula. Velocity addition is not an independent law but a corollary: it is what the Lorentz transformation does to the ratio $dx/dt$, with the new denominator $1 + u'v$ arising precisely because the time coordinate $t$ mixes in some $\Delta x'$ (the relativity of simultaneity). The theorem is the Lorentz transformation expressed in the language of velocities rather than coordinates.

- **The Wigner rotation and Thomas precession (atomic physics, group theory)** — the non-collinear generalisation. When the boosts are not collinear, their composition is a boost *followed by a rotation* — the Wigner rotation — so the velocity-addition operation is non-commutative and non-associative, making the velocity space a **gyrogroup** with the metric of hyperbolic geometry. The accumulated rotation around a closed orbit is the **Thomas precession**, responsible (with a factor $\tfrac12$) for the spin–orbit coupling of atomic fine structure. The collinear law of this theorem is the flat one-dimensional slice where the rotation vanishes.

---

# Unlocked by This

> [!tip] The Gyrogroup Structure of the Velocity Space *(from Differential Geometry)*
> Off-axis, relativistic velocity addition is neither commutative nor associative: composing non-collinear boosts yields a boost *plus a rotation* (the **Wigner rotation**), and the resulting algebraic structure of the velocity ball $\{|\mathbf{v}| < c\}$ is a **gyrogroup** — a group "up to a rotation", with a built-in *gyration* operator correcting associativity. The velocity ball with this operation is a model of **hyperbolic three-space**, the relativistic velocity-addition formula is its law of cosines, and rapidity is hyperbolic distance from the origin. The innocent collinear formula of this page is the geodesic line through the origin where the curvature is invisible.

> [!tip] Thomas Precession and Atomic Fine Structure *(from Atomic Physics)*
> The residual rotation of a composed boost, accumulated continuously around the closed orbit of a circling particle, is the **Thomas precession** of its spin axis. For an electron orbiting a nucleus this halves the naive spin–orbit coupling — the famous **Thomas factor of $\tfrac12$** — bringing the predicted **fine-structure** splitting of atomic spectral lines into agreement with experiment. That a purely kinematic effect of how velocities compose should show up in the energy levels of hydrogen is one of the most surprising downstream consequences of this theorem; it is velocity addition, made non-collinear, leaving its fingerprint on the periodic table.
