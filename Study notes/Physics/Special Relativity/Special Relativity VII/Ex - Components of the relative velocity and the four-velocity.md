---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Velocity Relative to an Observer"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{O}$ be an inertial observer with orthonormal frame $(e_\alpha)$, $e_0 = U_0$. A particle $\mathcal{P}$ moves in the $e_1$–$e_2$ plane of $\mathcal{O}$'s reference space on the circular trajectory
$$x^1(t) = R\cos\Omega t,\qquad x^2(t) = R\sin\Omega t,\qquad x^3(t) = 0,$$
where $R$ and $\Omega$ are positive constants with $R\Omega < 1$ (so the rim speed is sub-light). Working with $c = 1$:

1. Compute the relative velocity $V(t)$ and the speed $|\mathbf V|$. Show the speed is constant and identify the Lorentz factor $\Gamma$.
2. Write the four-velocity $U$ of $\mathcal{P}$ in components $u^\alpha$ in the observer's frame, and verify the unit-norm constraint and the relation $u^\alpha = (\Gamma, \Gamma V^1, \Gamma V^2, \Gamma V^3)$.
3. Confirm that the four-velocity is *not* constant along the worldline (so the particle is accelerated) even though its Lorentz factor and speed are constant.
4. State the condition on $R\Omega$ that the trajectory be sub-light, and find the Lorentz factor in the ultra-relativistic limit $R\Omega \to 1$.

**Recall:**

The exercise rests on the relative velocity, its components, and the four-velocity.

![[Def - Velocity Relative to an Observer#The Definition]]

The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] is $\Gamma = (1 - |\mathbf V|^2)^{-1/2}$, and the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is the future timelike unit vector $U$ tangent to the worldline, with components $u^\alpha = (\Gamma, \Gamma V^1, \Gamma V^2, \Gamma V^3)$ in the observer's frame, satisfying $U \cdot U = 1$.

---

# Convergent Strategy

**Problem class.** A *compute-kinematic-quantities-from-a-coordinate-trajectory* problem, the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|second source pattern]]: a worldline is given as $x^i(t)$ in an inertial frame, and the relative velocity, speed, Lorentz factor, and four-velocity follow by differentiation and assembly.

**Assumption pattern.** The trajectory is specified in coordinates, so $V^i = \mathrm{d}x^i/\mathrm{d}t$ is immediate by differentiation; the observer is inertial, so the simple component relations hold; and the motion is *circular*, which is the signal that the *speed* (and hence $\Gamma$) is constant while the *velocity vector* (and hence the four-velocity) rotates — a particle that is accelerated despite constant speed. The constraint $R\Omega < 1$ is the sub-light condition from [[Thm - Maximum Relative Velocity is c]].

**Theorem routing.** Part 1 differentiates the trajectory to get $V^i$ ([[Def - Velocity Relative to an Observer]]) and computes the constant speed $|\mathbf V| = R\Omega$, then $\Gamma = (1 - R^2\Omega^2)^{-1/2}$. Part 2 assembles the four-velocity via $u^\alpha = (\Gamma, \Gamma V^i)$ and checks $U \cdot U = 1$. Part 3 differentiates $U$ to show $\mathrm{d}U/\mathrm{d}\tau' \neq 0$, an instance of the four-acceleration being nonzero ([[Def - Four-Velocity and Four-Acceleration]]) despite constant $\Gamma$. Part 4 examines the limit, where $\Gamma \to \infty$ as $R\Omega \to 1$, an instance of the speed ceiling.

**Key decision point.** The instructive subtlety is that *constant speed does not mean constant four-velocity*: the four-velocity is a vector, and circular motion turns it without changing its length, so the particle is accelerated even though $\Gamma$ never changes. The natural error is to assume "constant speed ⇒ no acceleration", carried over from the (false) intuition that the four-velocity is determined by the speed alone; in fact the *direction* of the relative velocity matters, and its rotation is the acceleration.

---

# Legal Operations Used

1. **Differentiate the trajectory to get the relative velocity** (operation 6 from the topic page). $V^i = \mathrm{d}x^i/\mathrm{d}t$ is computed directly from $x^i(t)$.

2. **Compute in the observer's own frame** (operation 5). The components $V^i$, $|\mathbf V|$, and $u^\alpha = (\Gamma, \Gamma V^i)$ are all read off in the inertial frame with $e_0 = U_0$.

3. **Use the unit-norm constraint** (operation 4). The four-velocity is checked against $U \cdot U = 1$, confirming $\Gamma = (1 - |\mathbf V|^2)^{-1/2}$.

4. **Decompose the four-velocity orthogonally** (operation 2). The assembly $u^\alpha = (\Gamma, \Gamma V^i)$ is the component form of $U = \Gamma(U_0 + V)$.

---

# Hints

> [!note]- Hint 1
> Differentiate the trajectory: $V^1 = \mathrm{d}x^1/\mathrm{d}t = -R\Omega\sin\Omega t$ and $V^2 = R\Omega\cos\Omega t$. The speed is $|\mathbf V| = \sqrt{(V^1)^2 + (V^2)^2}$; use $\sin^2 + \cos^2 = 1$ to see it is constant.

> [!note]- Hint 2
> Once $|\mathbf V| = R\Omega$ is known, $\Gamma = (1 - R^2\Omega^2)^{-1/2}$ is constant. The four-velocity components are $u^\alpha = (\Gamma, \Gamma V^1, \Gamma V^2, 0) = \Gamma(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$.

> [!note]- Hint 3
> The four-velocity is $U = \Gamma(e_0 + V)$ with $V$ rotating in the $e_1$–$e_2$ plane. Even though $\Gamma$ and $|V|$ are constant, the *direction* of $V$ changes, so $\mathrm{d}U/\mathrm{d}t \neq 0$. Differentiate the spatial components and observe they do not vanish — the particle is accelerated.

> [!note]- Hint 4
> Sub-light requires $|\mathbf V| = R\Omega < 1$. As $R\Omega \to 1^-$, the denominator $\sqrt{1 - R^2\Omega^2} \to 0$, so $\Gamma \to \infty$: the rim approaches the speed of light and the Lorentz factor diverges, exactly as [[Thm - Maximum Relative Velocity is c|the speed ceiling]] predicts.

---

# Solution

The route is to differentiate the trajectory for the relative velocity, observe the speed is constant (so $\Gamma$ is), assemble the four-velocity, and then show — the instructive twist — that the four-velocity nonetheless rotates, making the particle accelerated. Step 1 gives $V$ and the constant speed; Step 2 assembles $U$ and checks its norm; Step 3 exhibits the nonzero four-acceleration; Step 4 takes the sub-light condition and the ultra-relativistic limit. The non-obvious thread is that a vector of constant length can still change — circular motion turns the four-velocity without lengthening it.

**Step 1: The relative velocity rotates with constant speed $|\mathbf V| = R\Omega$, giving $\Gamma = (1 - R^2\Omega^2)^{-1/2}$.**

> [!note]- Derivation
> Differentiate the trajectory with respect to the observer's proper time $t$:
> $$V^1 = \frac{\mathrm{d}x^1}{\mathrm{d}t} = -R\Omega\sin\Omega t,\qquad V^2 = \frac{\mathrm{d}x^2}{\mathrm{d}t} = R\Omega\cos\Omega t,\qquad V^3 = 0.$$
> So $V(t) = -R\Omega\sin\Omega t\,e_1 + R\Omega\cos\Omega t\,e_2$, a vector tangent to the circle, rotating at angular rate $\Omega$. Its speed is
> $$|\mathbf V| = \sqrt{(V^1)^2 + (V^2)^2} = \sqrt{R^2\Omega^2\sin^2\Omega t + R^2\Omega^2\cos^2\Omega t} = R\Omega\sqrt{\sin^2\Omega t + \cos^2\Omega t} = R\Omega,$$
> *constant* in time. The Lorentz factor is therefore also constant:
> $$\Gamma = \frac{1}{\sqrt{1 - |\mathbf V|^2}} = \frac{1}{\sqrt{1 - R^2\Omega^2}}.$$
> The speed and Lorentz factor do not change, even though the velocity *vector* sweeps around the circle.

**Step 2: The four-velocity is $u^\alpha = \Gamma(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$, with $U \cdot U = 1$.**

> [!note]- Derivation
> Assemble the four-velocity from $u^\alpha = (\Gamma, \Gamma V^1, \Gamma V^2, \Gamma V^3)$:
> $$u^\alpha = \big(\Gamma,\ -\Gamma R\Omega\sin\Omega t,\ \Gamma R\Omega\cos\Omega t,\ 0\big) = \Gamma\big(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0\big).$$
> Check the unit-norm constraint:
> $$U \cdot U = (u^0)^2 - (u^1)^2 - (u^2)^2 - (u^3)^2 = \Gamma^2\big[1 - R^2\Omega^2\sin^2\Omega t - R^2\Omega^2\cos^2\Omega t\big] = \Gamma^2(1 - R^2\Omega^2) = 1,$$
> using $\Gamma^2(1 - R^2\Omega^2) = 1$ from Step 1. The four-velocity is a unit vector, as required, and its assembly from $(\Gamma, \Gamma V^i)$ is the component form of the decomposition $U = \Gamma(U_0 + V)$.

**Step 3: The four-velocity rotates — $\mathrm{d}U/\mathrm{d}\tau' \neq 0$ — so the particle is accelerated despite constant speed.**

> [!note]- Derivation
> The four-velocity is $U = \Gamma\big(e_0 - R\Omega\sin\Omega t\,e_1 + R\Omega\cos\Omega t\,e_2\big)$. Differentiate with respect to the observer's time (using $\Gamma$ constant and $e_\alpha$ constant for the inertial observer):
> $$\frac{\mathrm{d}U}{\mathrm{d}t} = \Gamma\big(-R\Omega^2\cos\Omega t\,e_1 - R\Omega^2\sin\Omega t\,e_2\big) \neq 0.$$
> The four-acceleration is $A = \mathrm{d}U/\mathrm{d}\tau' = \Gamma\,\mathrm{d}U/\mathrm{d}t$, which is nonzero: the particle is accelerated. The key observation is that this happened *with constant speed and constant Lorentz factor* — the four-velocity is a *vector*, and circular motion turns it (changes its direction in the $e_1$–$e_2$ plane) without changing its length. The relative acceleration is purely centripetal, $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$, pointing toward the centre; the speed is unchanged precisely because the acceleration is transverse to the velocity. (Constant $\Gamma$ is consistent with nonzero acceleration exactly because $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V) = 0$ for transverse $\boldsymbol\gamma$ — see [[Thm - Expression of the Four-Acceleration]].)

**Step 4: Sub-light requires $R\Omega < 1$; as $R\Omega \to 1$, $\Gamma \to \infty$.**

> [!note]- Derivation
> The speed is $|\mathbf V| = R\Omega$, so the trajectory is sub-light — and the four-velocity exists — exactly when
> $$R\Omega < 1\qquad(\text{with }c:\ R\Omega < c).$$
> This is the [[Thm - Maximum Relative Velocity is c|maximum-relative-velocity]] bound applied to the rim speed: a point on a rotating disk of radius $R$ spinning at angular rate $\Omega$ cannot exceed $c$, so $R\Omega < c$, which limits how fast or how large a relativistically rotating disk can be. As the rim speed approaches the speed of light,
> $$\lim_{R\Omega \to 1^-}\Gamma = \lim_{R\Omega\to1^-}\frac{1}{\sqrt{1 - R^2\Omega^2}} = +\infty.$$
> The Lorentz factor diverges, the rim's clock runs arbitrarily slow relative to the centre, and the four-velocity tilts arbitrarily far toward the null cone — but never reaches it, since $R\Omega < 1$ strictly. This rotating-rim configuration is the kinematic seed of the Ehrenfest paradox and the Sagnac effect of [[Special Relativity XVII — Rotating Observers]].

> [!note]- Complete formal solution
> Differentiating the circular trajectory gives the [[Def - Velocity Relative to an Observer|relative velocity]] $V = -R\Omega\sin\Omega t\,e_1 + R\Omega\cos\Omega t\,e_2$, of constant speed $|\mathbf V| = R\Omega$ (by $\sin^2 + \cos^2 = 1$), so the Lorentz factor $\Gamma = (1 - R^2\Omega^2)^{-1/2}$ is constant. The four-velocity is $u^\alpha = \Gamma(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$, and $U \cdot U = \Gamma^2(1 - R^2\Omega^2) = 1$. Differentiating, $\mathrm{d}U/\mathrm{d}t = -\Gamma R\Omega^2(\cos\Omega t\,e_1 + \sin\Omega t\,e_2) \neq 0$: the particle is accelerated, because the four-velocity vector rotates even though its length (and the speed) is fixed — the relative acceleration $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$ is purely centripetal, transverse to the velocity, hence leaves the speed and $\Gamma$ unchanged. The trajectory is sub-light iff $R\Omega < 1$, and as $R\Omega \to 1^-$ the Lorentz factor $\Gamma \to \infty$, the rim approaching but never reaching the speed of light. $\blacksquare$

---

# Key Takeaways

**Reading kinematics off a coordinate trajectory is pure differentiation, and the four-velocity is the assembly $(\Gamma, \Gamma V^i)$.** Whenever a worldline is handed to you as $x^i(t)$ in an inertial frame, the entire kinematic apparatus follows mechanically: differentiate once for the relative velocity $V^i = \dot x^i$, form the speed $|\mathbf V| = \sqrt{\sum (V^i)^2}$, compute the Lorentz factor $\Gamma = (1-|\mathbf V|^2)^{-1/2}$, and assemble the four-velocity as $u^\alpha = (\Gamma, \Gamma V^i)$. This is the chapter's most routine computation and the one to reach for first when a trajectory is given. The unit-norm check $U \cdot U = \Gamma^2(1-|\mathbf V|^2) = 1$ is the built-in verification that the assembly is correct — if it fails, a factor of $\Gamma$ has gone astray. The same procedure handles any worldline: helical, hyperbolic, oscillatory; the circle is just the cleanest case because the speed comes out constant.

**Constant speed does not mean constant four-velocity — a vector can turn without changing length, and that turning is acceleration.** This is the conceptual lesson of circular motion and a common stumbling block. The four-velocity is a *vector*, not a scalar; circular motion holds its length fixed (constant speed, constant $\Gamma$) while rotating its direction, and a vector whose direction changes is changing, so its derivative — the four-acceleration — is nonzero. The particle is genuinely accelerated despite a constant Lorentz factor. The reusable diagnostic is the formula $\mathrm{d}\Gamma/\mathrm{d}t = \Gamma^3(\boldsymbol\gamma\cdot\mathbf V)$: the Lorentz factor changes only when the acceleration has a *component along the velocity* (which changes the speed); a purely transverse acceleration (like the centripetal acceleration of circular motion) turns the velocity without speeding or slowing it, leaving $\Gamma$ constant while the four-velocity rotates. Whenever you see "constant speed", do not conclude "no acceleration" — conclude "the acceleration, if any, is transverse".

**The sub-light bound limits a rotating disk's size and speed, and the divergence of $\Gamma$ at the rim is the seed of the rotating-observer paradoxes.** The condition $R\Omega < c$ — that the rim speed of a rotating disk stay below light — is the [[Thm - Maximum Relative Velocity is c|speed ceiling]] applied to rotation, and it has real consequences: you cannot rigidly rotate a disk so large or so fast that its rim would exceed $c$, which is already a hint that rigid rotation is subtle in relativity. As the rim approaches $c$, the Lorentz factor diverges, the rim clock desynchronises arbitrarily from the centre, and the four-velocity tilts toward the null cone. This rotating-rim kinematics is exactly the input to the **Ehrenfest paradox** (the rim is length-contracted but the radius is not, so the circumference-to-radius ratio exceeds $2\pi$) and the **Sagnac effect** (counter-rotating light beams return at different times), both developed in [[Special Relativity XVII — Rotating Observers]]. The trigger to remember: a rotating configuration brings in the speed ceiling at the rim, and the divergence of $\Gamma$ there is where the interesting rotating-frame physics lives.
