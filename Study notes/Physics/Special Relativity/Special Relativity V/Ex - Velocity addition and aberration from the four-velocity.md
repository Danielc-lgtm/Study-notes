---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Relativistic Velocity Addition"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

A particle moves with three-velocity $\mathbf{u}$ in inertial frame $S$, making an angle $\alpha$ with the $x$-axis: $\mathbf{u} = (u\cos\alpha, u\sin\alpha, 0)$. Frame $S'$ moves at speed $v$ along the $x$-axis of $S$. Working with $c = 1$:

1. Write the particle's [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ in $S$, and obtain its components $U'^\mu$ in $S'$ by applying the boost $U' = \Lambda U$ — *not* by transforming coordinates and re-differentiating.
2. By taking the ratio of the spatial and temporal components of $U'$, recover the relativistic velocity-addition law for the $x$-component, $u'\cos\alpha' = (u\cos\alpha - v)/(1 - uv\cos\alpha)$.
3. By taking the ratio of the $y$- and $x$-components, derive the **aberration** formula $\tan\alpha' = \dfrac{u\sin\alpha}{\gamma_v(u\cos\alpha - v)}$, and specialise to light ($u = 1$) to get the stellar-aberration formula.
4. Explain why this four-velocity method is cleaner than the coordinate method, and why "four-velocities do not add, they transform".

**Recall:**

![[Def - Four-Velocity and Four-Acceleration#The Definition]]

A boost along $x$ at speed $v$ is the [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ with $t' = \gamma_v(t - vx)$, $x' = \gamma_v(x - vt)$, $y' = y$, $z' = z$, $\gamma_v = (1 - v^2)^{-1/2}$. The collinear case of this is the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]]. The four-velocity transforms as a four-vector, $U'^\mu = \Lambda^\mu{}_\nu U^\nu$.

---

# Convergent Strategy

**Problem class.** A *transform-a-four-vector-to-another-frame* problem, showcasing the central advantage of the four-vector formalism. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: to find what another observer measures, Lorentz-transform the relevant four-vector directly, rather than transforming coordinates and recomputing — the four-vector machinery eliminates explicit coordinate gymnastics.

**Assumption pattern.** The unlock is that the three-velocity, which transforms by an ugly nonlinear rule, is packaged inside a four-velocity that transforms by a *single linear matrix*. So velocity addition (and its angular partner, aberration) is just one matrix multiplication followed by taking ratios of components. The factor $\gamma_u$ cancels in every ratio, so the speed of the particle drops out of the *direction* formulas, leaving clean expressions.

**Theorem routing.** Part 1 is the boost $U' = \Lambda U$. Parts 2–3 are ratios of the resulting components — $U'^1/U'^0$ gives the $x$-velocity (velocity addition), $U'^2/U'^1$ gives the direction (aberration). Part 4 is the conceptual payoff: four-velocities live on a hyperboloid, not a vector space, so they compose by the group action $\Lambda$, not by vector addition.

**Key decision point.** The crux is the decision *not* to transform coordinates. The naive route — write $x'(t'), y'(t')$ and differentiate — works but is laborious and error-prone. The four-velocity route replaces all of it with one matrix product, because the $\gamma_u$ packaged into $U$ carries exactly the time-dilation bookkeeping that the coordinate method has to redo by hand.

---

# Legal Operations Used

1. **Lorentz-transform a four-vector to get a component in another frame** (operation 7 from the topic page). The whole solution is $U' = \Lambda U$ followed by reading off ratios of components.

2. **Switch to rapidity / use the group structure of boosts** (operation 6 from the topic page). The fact that four-velocities compose by the Lorentz *group* action, not by addition, is the conceptual content of part 4.

3. **Compute an invariant as a check** (operation 7 from the topic page). One can confirm $U' \cdot U' = 1$ to verify the transformation preserved the unit norm.

---

# Hints

> [!note]- Hint 1
> The four-velocity in $S$ is $U^\mu = \gamma_u(1, u\cos\alpha, u\sin\alpha, 0)$ with $\gamma_u = (1 - u^2)^{-1/2}$. Apply the $x$-boost componentwise: $U'^0 = \gamma_v(U^0 - vU^1)$, $U'^1 = \gamma_v(U^1 - vU^0)$, $U'^2 = U^2$, $U'^3 = U^3$.

> [!note]- Hint 2
> The transformed velocity in $S'$ has $x$-component $u'\cos\alpha' = U'^1/U'^0$ (since $U'^\mu = \gamma_{u'}(1, \mathbf{u}')$, the spatial-over-temporal ratio gives the three-velocity). The $\gamma_v$ and $\gamma_u$ factors cancel.

> [!note]- Hint 3
> The direction angle in $S'$ satisfies $\tan\alpha' = U'^2/U'^1 = (\text{unchanged } y\text{-component})/(\text{boosted } x\text{-component})$. The $\gamma_u$ cancels but a $\gamma_v$ survives in the denominator. For light set $u = 1$.

> [!note]- Hint 4
> Two four-velocities $U_1, U_2$ do not sum to a four-velocity ($U_1 + U_2$ is generally not unit-normalised), so the space of four-velocities is not a vector space — it is the unit hyperboloid. Combining velocities means composing boosts (group elements), which is why the law is nonlinear.

---

# Solution

This exercise is the four-vector formalism earning its keep: velocity addition and aberration, which are painful by coordinate methods, collapse to one matrix multiplication. The plan: Step 1 boosts the four-velocity; Step 2 reads off the $x$-velocity; Step 3 reads off the direction (aberration); Step 4 draws the structural moral.

**Step 1: Boost the four-velocity.**

> [!note]- Derivation
> In $S$ the particle has four-velocity
> $$U^\mu = \gamma_u(1,\ u\cos\alpha,\ u\sin\alpha,\ 0), \qquad \gamma_u = (1 - u^2)^{-1/2}.$$
> Apply the $x$-boost $\Lambda$ to frame $S'$ (moving at $+v$ along $x$):
> $$
> \begin{aligned}
> U'^0 &= \gamma_v(U^0 - vU^1) = \gamma_v\gamma_u(1 - uv\cos\alpha),\\
> U'^1 &= \gamma_v(U^1 - vU^0) = \gamma_v\gamma_u(u\cos\alpha - v),\\
> U'^2 &= U^2 = \gamma_u\,u\sin\alpha,\\
> U'^3 &= 0.
> \end{aligned}
> $$
> This is the entire calculation — one matrix multiplication. Everything else is reading off ratios. (Check: $U' \cdot U' = (U'^0)^2 - (U'^1)^2 - (U'^2)^2$ collapses to $1$, since the boost preserves the [[Def - Four-Velocity and Four-Acceleration|unit norm]].)

**Step 2: Velocity addition (the $x$-component).**

> [!note]- Derivation
> In $S'$ the four-velocity is, by definition, $U'^\mu = \gamma_{u'}(1, \mathbf{u}')$, so the three-velocity is recovered as the spatial-over-temporal ratio, $\mathbf{u}' = (U'^1, U'^2, U'^3)/U'^0$. The $x$-component is
> $$u'\cos\alpha' = \frac{U'^1}{U'^0} = \frac{\gamma_v\gamma_u(u\cos\alpha - v)}{\gamma_v\gamma_u(1 - uv\cos\alpha)} = \frac{u\cos\alpha - v}{1 - uv\cos\alpha}.$$
> The factors $\gamma_v\gamma_u$ cancel completely. This is the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]] for the component along the boost; for purely collinear motion ($\alpha = 0$) it is the familiar $u' = (u - v)/(1 - uv)$.

**Step 3: Aberration (the direction).**

> [!note]- Derivation
> The angle the velocity makes with the $x'$-axis in $S'$ is given by the ratio of the $y'$- and $x'$-components:
> $$\tan\alpha' = \frac{u'\sin\alpha'}{u'\cos\alpha'} = \frac{U'^2}{U'^1} = \frac{\gamma_u\,u\sin\alpha}{\gamma_v\gamma_u(u\cos\alpha - v)} = \frac{u\sin\alpha}{\gamma_v(u\cos\alpha - v)}.$$
> Here $\gamma_u$ cancels but a single $\gamma_v$ survives in the denominator — this is the relativistic **aberration of motion**. For a *light ray*, $u = 1$:
> $$\tan\alpha' = \frac{\sin\alpha}{\gamma_v(\cos\alpha - v)},$$
> the **stellar aberration** formula: the apparent direction of a star shifts as the observer's velocity $v$ changes (over Earth's orbit, $v \approx 10^{-4}$, giving the historically measured $\sim 20''$ annual ellipse). The factor $\gamma_v$ is the genuinely relativistic correction to the classical aberration, which would have $\gamma_v = 1$.

**Step 4: Why four-velocities transform rather than add.**

> [!note]- Derivation
> The classical instinct is to "add velocities". Relativistically this is wrong, and the four-vector picture shows exactly why. Two four-velocities $U_1, U_2$ both satisfy $U_i \cdot U_i = 1$, so they live on the **unit hyperboloid** $\{X : X \cdot X = 1\}$ — a curved surface, *not* a linear subspace. Their sum $U_1 + U_2$ has $(U_1 + U_2)\cdot(U_1 + U_2) = 1 + 1 + 2U_1\cdot U_2 \ne 1$ in general, so it is *not* a four-velocity. The space of four-velocities is therefore **not a vector space**, and "adding" them is meaningless.
>
> What *is* meaningful is to change frames, which acts on a four-velocity by the [[Def - The Lorentz Transformation|Lorentz transformation]] $U \mapsto \Lambda U$ — a group action that maps the hyperboloid to itself (boosts are its isometries). "Combining velocities" means composing two such boosts, $\Lambda_2\Lambda_1$, and because boosts form a *group* (not a vector space), the composition law is the nonlinear velocity-addition formula, not vector addition. In [[Def - Rapidity|rapidity]] variables collinear boosts *do* add (the rapidity is the additive coordinate along a one-parameter boost subgroup), which is the cleanest way to see the structure: velocities are $\tanh$ of the additive rapidity, and $\tanh$ of a sum is the velocity-addition formula. The moral: velocities are not vectors you add — they are parameters of group elements you compose.

> [!note]- Complete formal solution
> In $S$, $U^\mu = \gamma_u(1, u\cos\alpha, u\sin\alpha, 0)$. Boosting to $S'$ (speed $v$ along $x$): $U'^0 = \gamma_v\gamma_u(1 - uv\cos\alpha)$, $U'^1 = \gamma_v\gamma_u(u\cos\alpha - v)$, $U'^2 = \gamma_u u\sin\alpha$. The three-velocity in $S'$ is the spatial-over-temporal ratio: $u'\cos\alpha' = U'^1/U'^0 = (u\cos\alpha - v)/(1 - uv\cos\alpha)$ (velocity addition), and $\tan\alpha' = U'^2/U'^1 = u\sin\alpha/[\gamma_v(u\cos\alpha - v)]$ (aberration); for light $u = 1$, $\tan\alpha' = \sin\alpha/[\gamma_v(\cos\alpha - v)]$ (stellar aberration). Four-velocities lie on the unit hyperboloid $U\cdot U = 1$, not a vector space — $U_1 + U_2$ is not unit-normalised — so they compose by the Lorentz group action $U \mapsto \Lambda U$, whose nonlinear law is velocity addition; in rapidity variables collinear boosts add. $\blacksquare$

> [!warning] Illegal but tempting: transforming coordinates and re-differentiating
> The "obvious" route is to transform the coordinate functions $x(t), y(t)$ to $x'(t'), y'(t')$ and then compute $\mathbf{u}' = d\mathbf{x}'/dt'$ from scratch. This is correct but laborious: one must transform both numerator and denominator, track the time-dilation factor between $dt$ and $dt'$, and the algebra is several times longer and far more error-prone. The four-velocity method avoids all of it because the factor $\gamma_u$ *already packaged inside* $U^\mu = \gamma_u(1, \mathbf u)$ carries exactly the $dt/d\tau$ bookkeeping the coordinate method has to reconstruct. The diagnostic: whenever a problem asks "what does the other observer measure for a velocity, energy, frequency, or angle", transform the *four-vector* directly ($U$, $P$, or the wave four-vector $K$), never the coordinates — this is the entire labour-saving point of the four-vector formalism, the relativistic analogue of using dot products instead of coordinates in Euclidean geometry.

---

# Key Takeaways

**Velocity addition and aberration are one matrix multiplication on the four-velocity.** The painful nonlinear three-velocity transformation, and its angular partner aberration, both reduce to "boost the four-velocity $U' = \Lambda U$, then take ratios of components". The $x$-velocity is $U'^1/U'^0$, the direction is $U'^2/U'^1$, and the $\gamma_u$ factors cancel automatically. This is the reusable power of packaging a velocity into a four-vector: the ugly composition law is hidden inside a clean linear transformation, and you extract whatever component ratio the question wants at the end. The trigger: any "what velocity/angle does the moving observer see" question is answered by transforming $U^\mu$ directly, and the same template (transform the four-vector, take ratios) handles the [[Def - The Four-Momentum of a Photon|Doppler effect and aberration of light]] by transforming the wave four-vector $K^\mu$ instead.

**Four-velocities live on a hyperboloid and compose by the group, not by addition.** The deepest structural fact is that the set of four-velocities is the unit hyperboloid $U \cdot U = 1$ — a curved surface, not a vector space — so adding two of them produces something that is not a four-velocity. "Combining velocities" therefore cannot be vector addition; it must be composition of the boosts that carry one four-velocity to another, and because boosts form a *group*, the composition is the nonlinear velocity-addition law. In [[Def - Rapidity|rapidity]] coordinates the group is locally $(\mathbb{R}, +)$ and collinear velocities add as rapidities, which is the clean linearisation. The reusable insight: whenever a quantity is constrained to a nonlinear surface (here the mass/velocity hyperboloid), it transforms by a group action, not by addition, and the apparent nonlinearity of the composition law is just the curvature of that surface. This is the same reason rest masses are not additive and boosts do not commute.

**The $\gamma_u$ inside the four-velocity is the time-dilation bookkeeping done for you.** The reason the four-velocity method beats the coordinate method is that $U^\mu = \gamma_u(1, \mathbf{u})$ already contains the factor $\gamma_u = dt/d\tau$, which is precisely the time-dilation relation the coordinate method must reconstruct by transforming $dt \to dt'$ separately. Packaging the velocity with its $\gamma$ into a single four-vector means the boost handles position and time *together*, so no separate time-dilation step is needed. The general lesson for relativistic calculations: build the right four-vector (four-velocity, [[Def - Four-Momentum and Rest Mass|four-momentum]], wave four-vector), and the frame change is a single linear map that automatically does the bookkeeping that component-by-component methods do by hand. See [[Ex - Four-velocity has unit norm and four-acceleration is orthogonal to it]] for the foundational identities of the four-velocity used here.
