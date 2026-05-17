---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Rapidity"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Three inertial frames: $S$, $S'$, $S''$. The frame $S'$ moves at velocity $v$ relative to $S$ (all motion collinear, along $x$); a particle, or the frame $S''$, moves at velocity $u'$ relative to $S'$. The Lorentz factor is $\gamma = (1-v^2)^{-1/2}$; rapidity is $\varphi$ with $v = \tanh\varphi$ (see [[Def - Rapidity]]). Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Statement

> **Relativistic velocity addition (collinear).** Let a particle move with velocity $u'$ along the $x'$-axis of frame $S'$, and let $S'$ move with velocity $v$ along the $x$-axis of frame $S$. Then the velocity $u$ of the particle as measured in $S$ is
> $$\boxed{\quad u \;=\; \frac{u' + v}{1 + u'v} \quad}$$
> (with $c$ restored: $u = (u'+v)\big/(1 + u'v/c^2)$). Equivalently, in [[Def - Rapidity|rapidity]] variables, the rapidities add: $\varphi_u = \varphi_{u'} + \varphi_v$.
>
> Two consequences. If $u' = 1$ then $u = 1$: light has speed $1$ in every frame. If $|u'| < 1$ and $|v| < 1$ then $|u| < 1$: composing sub-light speeds never reaches the speed of light.

---

# Motivation

Newtonian physics has the obvious rule: if a ball rolls forward at $u'$ inside a train moving at $v$, then to the ground the ball moves at $u' + v$. Velocities just add. This is so intuitive it feels like a definition rather than a physical claim — but it cannot be correct, and the reason is light.

Set $u' = 1$, a light beam inside the train. The Newtonian rule gives ground speed $1 + v > 1$, contradicting the [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]], which insists every observer measures light at speed $1$. So the addition law must be wrong, and this theorem is its replacement. The question it answers is precise: *given the constancy of the speed of light, how do velocities actually combine?*

The answer, $u = (u'+v)/(1+u'v)$, is the unique formula consistent with relativity, and it has exactly the two features the physics demands. It keeps $c$ as a **fixed point**: feed in $u' = 1$ and out comes $u = 1$, no matter what $v$ is. And it keeps $c$ as a **ceiling**: feed in any two sub-light speeds and the output stays below $1$. You cannot bootstrap your way past the speed of light by stacking boosts. The Newtonian rule is recovered as the low-speed approximation — when $u'v \ll 1$ the denominator is $\approx 1$ and $u \approx u' + v$ — so relativity does not contradict everyday experience, it corrects it at high speed.

There is a second, deeper reason to expect this result, and it is the one that makes the formula unsurprising rather than mysterious. The boosts along a fixed direction form a [[Def - The Lorentz Group|group]]; composing two of them must give a third. The only question is *which* third, and the cleanest way to answer it is the rapidity ([[Def - Rapidity]]): in rapidity variables boosts compose by simple addition, $\varphi \mapsto \varphi_1 + \varphi_2$, exactly as rotation angles add. The velocity-addition formula is then nothing but $\tanh$ of a sum, $u = \tanh(\varphi_{u'} + \varphi_v)$, and the famous formula is the hyperbolic tangent addition identity in disguise.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a velocity $u'$ measured relative to a frame $S'$, which moves at $v$ relative to $S$".

The first disguised source is **a chain of three or more frames or relative motions**. If $S''$ moves relative to $S'$ moves relative to $S$, the theorem composes pairwise — but the slick recognition is that *any* number of collinear relative motions compose by adding all the rapidities at once. The bridge is the additivity of rapidity ([[Def - Rapidity]]): $\varphi_{\text{total}} = \sum_i \varphi_i$, and the final velocity is $\tanh$ of the sum. *Example problem:* a rocket whose every stage adds velocity $v$ in the previous stage's frame — after $n$ stages the speed is $\tanh(n\,\tanh^{-1}v)$, which approaches but never reaches $c$ ([[Ex - Composing boosts with rapidity]]).

The second disguised source is **a Doppler or aberration setup, where a direction or frequency is sought rather than a speed**. Light emitted in one frame, observed in another, has its direction and frequency changed; the underlying computation is the transformation of the components of a velocity (or null) four-vector, and the collinear part of it is governed by this theorem. The bridge is that the velocity-addition law is the ratio of transformed coordinates, and the same Lorentz transformation that adds velocities also tilts directions. *Example problem:* the [[Ex - Aberration of light|aberration of starlight]], where the transverse and longitudinal velocity components transform differently.

The third disguised source is **the composition of two boosts written as matrices**. If a problem hands you $\Lambda[v_1]\Lambda[v_2]$ and asks for the resulting transformation, the velocity-addition law is the velocity of the product boost. The bridge is the matrix identity $\Lambda[v_1]\Lambda[v_2] = \Lambda\big[(v_1+v_2)/(1+v_1v_2)\big]$, which is the theorem read at the level of the [[Def - The Lorentz Group|Lorentz group]]. *Example problem:* [[Ex - Composing boosts with rapidity]].

**Targets (Output Amplification)**

The conclusion is "$u = (u'+v)/(1+u'v)$".

Combine the conclusion with **the fixed-point property**. Setting $u' = c$ gives $u = c$ identically: the conclusion, specialised, *re-derives* the second postulate. The further result is that the constancy of the speed of light is not an independent assumption once the velocity-addition law is known — it is a corollary. The combination is useful as a consistency check and as the logical closure of the theory.

Combine the conclusion with **the inequality $|u| < 1$**. The theorem's output is bounded by $c$, so any quantity built by composing velocities inherits a $c$-ceiling. The further result is the unattainability of the speed of light by acceleration: a particle pushed by a force gains rapidity linearly but velocity only asymptotically. The combination underlies the relativistic equation of motion in **Special Relativity II** — a constant force produces hyperbolic, not parabolic, motion.

Combine the conclusion with **rapidity additivity to handle non-collinear cases**. While the boxed formula is collinear, recognising it as $\tanh$ of a rapidity sum lets you treat general velocity addition by adding rapidity *vectors* — and the failure of those to add as ordinary vectors produces the **Thomas precession**, a rotation accumulated by composing non-collinear boosts. The further result $E$ is this genuinely new effect, invisible in the collinear formula but forced by the group structure behind it.

---

# Why Is It True

The most illuminating reason is the group-theoretic one, and it makes the formula inevitable.

A boost is an element of the [[Def - The Lorentz Group|Lorentz group]]. Two collinear boosts, applied in succession, must produce another collinear boost — that is just closure of the group. So composing a boost of velocity $v$ with a boost of velocity $u'$ yields a boost of *some* velocity $u$; the only question is the function $u(u',v)$. Now, any reasonable composition law on a one-parameter group can be made into ordinary addition by choosing the right coordinate — the canonical coordinate. For rotations that coordinate is the angle; for boosts it is the [[Def - Rapidity|rapidity]]. In rapidity, composition *is* addition: $\varphi_u = \varphi_{u'} + \varphi_v$. Translating back through $v = \tanh\varphi$,
$$u = \tanh(\varphi_{u'} + \varphi_v),$$
and the hyperbolic tangent addition formula, $\tanh(a+b) = (\tanh a + \tanh b)/(1 + \tanh a\tanh b)$, gives exactly $u = (u'+v)/(1+u'v)$. The formula is forced; it is the only group law a one-parameter subgroup can have, written in the velocity coordinate instead of the natural one.

Why is $\tanh$ the right function — why does $u' + v$ get divided by $1 + u'v$ and not something else? Because $\tanh$ is the function that maps the whole real line (rapidity, which adds) into the interval $(-1,1)$ (velocity, which is bounded by $c$), monotonically and smoothly. Any addition law on velocities that respects a fixed ceiling at $c$ and reduces to ordinary addition near zero must be conjugate to addition by *some* such squashing function, and the requirement that the boost matrices actually multiply correctly pins that function down to $\tanh$.

A second, more elementary intuition: the constancy of light alone almost forces the denominator. The law must satisfy $u(c, v) = c$ — light stays light. Any formula of the form $u = (u'+v)/D(u',v)$ with $D$ built from $u', v$ achieves this only if $D = 1 + u'v$ (so that the numerator and denominator each pick up a factor when $u' = c$): with $u' = 1$, numerator $= 1+v$, denominator $= 1+v$, ratio $= 1$. The denominator $1 + u'v$ is exactly the correction that makes light a fixed point, and it is small (so the law looks Newtonian) precisely when $u'v$ is small.

The fixed-point and ceiling properties are then not separate facts to be checked but structural consequences: $\tanh$ has fixed points at $\pm\infty \mapsto \pm 1$ and maps $\mathbb{R}$ into $(-1,1)$, so composing rapidities (unbounded, additive) always yields a velocity inside $(-1,1)$ with $c$ as the unreachable boundary.

---

# What Makes This Hard

The direct derivation — divide the Lorentz-transformed $\Delta x$ by $\Delta t$ — is short, and the place people stumble is algebraic: the factors of $\gamma$ must cancel between numerator and denominator, and forgetting that both $\Delta x$ and $\Delta t$ transform (not just $\Delta x$) gives the wrong, Newtonian-looking answer. The genuinely non-obvious step is conceptual: recognising that the messy formula is $\tanh$ of a rapidity sum, which is invisible unless one already knows rapidity is the additive coordinate. The most common error is to apply the collinear formula to non-collinear velocities, where it simply fails — general velocity addition requires transforming the velocity *vector's* components, and the transverse and longitudinal parts behave differently.

---

# Rederivation Scaffold

**High-level strategy:**
Either (A) write the particle's worldline in $S'$, Lorentz-transform to $S$, and form $u = \Delta x/\Delta t$, watching the $\gamma$'s cancel; or (B) switch to rapidity, add, convert back. Route B is shorter and explains the formula; route A is self-contained.

**Subgoal decomposition (route A):**

1. **Write the particle's motion in $S'$.** Its worldline is $x' = u't'$, so a displacement is $\Delta x' = u'\Delta t'$.
   - *Hint:* "moves at $u'$ in $S'$" means exactly $\Delta x' = u'\Delta t'$.
   - *Why needed:* It encodes the input velocity as a relation between coordinate differences.

2. **Transform the displacement to $S$.** Apply the inverse Lorentz transformation: $\Delta x = \gamma(\Delta x' + v\Delta t')$, $\Delta t = \gamma(\Delta t' + v\Delta x')$.
   - *Hint:* The transformation is linear, so it acts on differences exactly as on coordinates.
   - *Why needed:* Both numerator and denominator of $u = \Delta x/\Delta t$ must be transformed.

3. **Form the ratio and substitute $\Delta x' = u'\Delta t'$.**
   - *Hint:* $u = \Delta x/\Delta t = \gamma(\Delta x' + v\Delta t')\big/\gamma(\Delta t' + v\Delta x')$; the $\gamma$'s cancel; substitute $\Delta x' = u'\Delta t'$ and cancel $\Delta t'$.
   - *Why needed:* It produces $(u'+v)/(1+u'v)$ directly.

**Subgoal decomposition (route B):**

1. **Express both boosts in rapidity.** $v = \tanh\varphi_v$, $u' = \tanh\varphi_{u'}$.
2. **Add the rapidities.** Collinear boosts compose by $\varphi_u = \varphi_{u'} + \varphi_v$ ([[Def - Rapidity]]).
3. **Convert back.** $u = \tanh\varphi_u = \tanh(\varphi_{u'}+\varphi_v)$; expand by the $\tanh$ addition formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: A displacement along the particle's worldline satisfies $\Delta x' = u'\Delta t'$
> **Statement:** A particle moving at constant velocity $u'$ in $S'$ has, between any two events on its worldline, $\Delta x' = u'\,\Delta t'$.
>
> **Hint:** Constant velocity means the worldline is the straight line $x' = u't' + \text{const}$.
>
> **Why needed:** It is the algebraic form of the hypothesis "moves at $u'$ in $S'$", fed into the transformation.
>
> > [!note]- Full proof
> > "Moves at constant velocity $u'$" means the worldline in $S'$ is $x'(t') = u't' + x'_0$. For any two events on it, subtracting gives $\Delta x' = u'\,\Delta t'$. $\blacksquare$

> [!note]- Lemma 2: The $\gamma$ factors cancel in the velocity ratio
> **Statement:** With $\Delta x = \gamma(\Delta x' + v\Delta t')$ and $\Delta t = \gamma(\Delta t' + v\Delta x')$, the ratio $\Delta x/\Delta t$ is independent of $\gamma$.
>
> **Hint:** $\gamma$ multiplies both numerator and denominator.
>
> **Why needed:** It is why the final formula has no $\gamma$ in it — velocity addition is $\gamma$-free, unlike time dilation.
>
> > [!note]- Full proof
> > $\dfrac{\Delta x}{\Delta t} = \dfrac{\gamma(\Delta x' + v\Delta t')}{\gamma(\Delta t' + v\Delta x')} = \dfrac{\Delta x' + v\Delta t'}{\Delta t' + v\Delta x'}$: the common factor $\gamma$ cancels. $\blacksquare$

> [!note]- Lemma 3: Rapidities of collinear boosts add
> **Statement:** $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$ for collinear boosts.
>
> **Hint:** Multiply the two hyperbolic-rotation matrices and use the $\cosh, \sinh$ addition formulas.
>
> **Why needed:** It is route B in one line, and it explains *why* the velocity formula has the form it does.
>
> > [!note]- Full proof
> > With $\Lambda[\varphi] = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$,
> > $$\Lambda[\varphi_1]\Lambda[\varphi_2] = \begin{pmatrix}\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 & \cosh\varphi_1\sinh\varphi_2 + \sinh\varphi_1\cosh\varphi_2\\ \sinh\varphi_1\cosh\varphi_2 + \cosh\varphi_1\sinh\varphi_2 & \sinh\varphi_1\sinh\varphi_2 + \cosh\varphi_1\cosh\varphi_2\end{pmatrix}.$$
> > By the hyperbolic addition formulas $\cosh(\varphi_1+\varphi_2) = \cosh\varphi_1\cosh\varphi_2+\sinh\varphi_1\sinh\varphi_2$ and $\sinh(\varphi_1+\varphi_2) = \sinh\varphi_1\cosh\varphi_2+\cosh\varphi_1\sinh\varphi_2$, this equals $\begin{pmatrix}\cosh(\varphi_1+\varphi_2) & \sinh(\varphi_1+\varphi_2)\\\sinh(\varphi_1+\varphi_2) & \cosh(\varphi_1+\varphi_2)\end{pmatrix} = \Lambda[\varphi_1+\varphi_2]$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Route A (Lorentz transformation).** A particle moves at constant velocity $u'$ in $S'$; by Lemma 1, between any two events on its worldline $\Delta x' = u'\,\Delta t'$. The frame $S'$ moves at velocity $v$ relative to $S$, so the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] gives, for the (linear, hence difference-respecting) coordinate change,
> $$\Delta x = \gamma(\Delta x' + v\,\Delta t'), \qquad \Delta t = \gamma(\Delta t' + v\,\Delta x').$$
> The velocity of the particle in $S$ is $u = \Delta x/\Delta t$. By Lemma 2 the $\gamma$ cancels:
> $$u = \frac{\Delta x' + v\,\Delta t'}{\Delta t' + v\,\Delta x'}.$$
> Substitute $\Delta x' = u'\,\Delta t'$ and cancel the common $\Delta t'$:
> $$u = \frac{u'\,\Delta t' + v\,\Delta t'}{\Delta t' + v\,u'\,\Delta t'} = \frac{u' + v}{1 + u'v}.$$
>
> **Route B (rapidity).** Write $v = \tanh\varphi_v$ and $u' = \tanh\varphi_{u'}$. The boost from $S$ to $S'$ has rapidity $\varphi_v$; the particle's motion in $S'$ corresponds to rapidity $\varphi_{u'}$. By Lemma 3 the composite boost has rapidity $\varphi_u = \varphi_{u'} + \varphi_v$, so
> $$u = \tanh\varphi_u = \tanh(\varphi_{u'} + \varphi_v) = \frac{\tanh\varphi_{u'} + \tanh\varphi_v}{1 + \tanh\varphi_{u'}\tanh\varphi_v} = \frac{u' + v}{1 + u'v}.$$
>
> **The two consequences.** If $u' = 1$: $u = (1+v)/(1+v) = 1$. If $|u'| < 1$ and $|v| < 1$: compute $1 - u = 1 - \frac{u'+v}{1+u'v} = \frac{(1-u')(1-v)}{1+u'v}$, which is positive since each factor is positive; similarly $1 + u = \frac{(1+u')(1+v)}{1+u'v} > 0$. Hence $-1 < u < 1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The relativistic rocket.** A rocket fires its engine so as to add a fixed velocity increment $\delta v$ in its instantaneous rest frame at each step. Naively the speed grows without bound; relativistically each step adds a fixed *rapidity* $\delta\varphi$, so after a long burn the rapidity is large but the velocity $\tanh\varphi$ saturates just below $c$. The application is nonobvious because "add a bit of speed repeatedly" sounds like it should reach any speed, and only the rapidity picture shows why it cannot.

**Stellar aberration and the headlight effect.** A source emitting light isotropically in its rest frame appears, to an observer it moves towards, to beam its light forward into a narrow cone — the relativistic headlight effect. This is velocity addition applied to the *direction* of light rays: each ray's velocity components transform, and the collinear part is governed by this theorem; see [[Ex - Aberration of light]]. The application is out-of-distribution because it looks like an optics problem, not a velocity-composition problem.

**Compton-style kinematics.** When two particles collide head-on, their relative speed — the speed of one in the rest frame of the other — is computed by velocity addition, and the formula's $c$-ceiling guarantees the relative speed never exceeds $c$ even when both particles individually approach $c$. The application is surprising because one might expect two near-light particles approaching each other to have relative speed near $2c$; the theorem forbids it.

---

# Bridges

- **[[Def - Rapidity]]** — velocity addition *is* rapidity addition; the theorem is the hyperbolic tangent addition formula. Rapidity is the bridge that turns the nonlinear group law into a sum.

- **The angle-addition formula for rotations** — the exact Euclidean analogue: composing rotations adds angles, $\tan(\theta_1+\theta_2) = (\tan\theta_1+\tan\theta_2)/(1-\tan\theta_1\tan\theta_2)$. The relativistic law is the same identity with $\tan \to \tanh$ and the sign of the cross term flipped — the signature change of Minkowski versus Euclidean geometry.

- **[[Def - The Lorentz Group]]** — the theorem is the closure of the boost subgroup made explicit: composing two collinear boosts gives a third, and the velocity-addition law names it. Non-collinear composition brings in the Wigner rotation, the boost subgroup's failure to be normal.

- **[[Thm - The Reversed Triangle Inequality]]** — both are facts about the indefinite geometry; velocity addition lives on the velocity hyperboloid, where rapidity is hyperbolic distance and the triangle inequality reverses.

---

# Unlocked by This

> [!tip] The Unattainability of the Speed of Light *(from Relativistic Dynamics)*
> Because composing sub-light speeds never reaches $c$, a particle under a constant force gains *rapidity* uniformly but velocity only asymptotically — its worldline is a hyperbola, not a parabola. This is the content of the relativistic [[Thm - The Relativistic Equation of Motion|equation of motion]], and the reason no finite energy accelerates a massive particle to $c$.

> [!tip] Thomas Precession *(from Relativistic Dynamics and Atomic Physics)*
> Composing two *non-collinear* boosts yields a boost together with a rotation — the **Thomas–Wigner rotation**. Accumulated along an accelerating, turning worldline it produces the **Thomas precession** of a gyroscope or an electron's spin, a measurable correction to atomic fine structure.
