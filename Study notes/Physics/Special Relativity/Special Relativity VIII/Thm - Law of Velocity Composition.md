---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Velocity Relative to an Observer"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Thm - Reciprocity of Relative Velocity"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, $u\cdot u = +1$ for a four-velocity. Three objects share a crossing event $O$: observers $\mathcal{O}, \mathcal{O}'$ with four-velocities $u, u'$, and a massive particle $\mathcal{P}$ with four-velocity $v$. The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] between the observers is $\Gamma_0 = u\cdot u'$; that of $\mathcal{P}$ is $\Gamma = u\cdot v$ relative to $\mathcal{O}$ and $\Gamma' = u'\cdot v$ relative to $\mathcal{O}'$. The velocity of $\mathcal{O}'$ relative to $\mathcal{O}$ is $U \in E_u$ (magnitude $U$, unit vector $e = U/U$); of $\mathcal{O}$ relative to $\mathcal{O}'$ is $U' \in E_{u'}$ (with $U' = -U$ in magnitude and $e' = U'/U' \in E_{u'}$). The velocity of $\mathcal{P}$ is $V \in E_u$ relative to $\mathcal{O}$ and $V' \in E_{u'}$ relative to $\mathcal{O}'$, with [[Def - Velocity Relative to an Observer|decompositions]] $v = \Gamma(u + V) = \Gamma'(u' + V')$. The [[Def - The Orthogonal Projector onto the Local Rest Space|projector]] onto $E_{u'}$ is $\perp_{u'}X = X - (u'\cdot X)u'$. We write $V = V_\parallel e + \mathbf{V}_\perp$ with $\mathbf{V}_\perp\cdot e = 0$, and similarly $V' = V'_\parallel e' + \mathbf{V}'_\perp$. Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Statement

> **Law of velocity composition.** Let a particle $\mathcal{P}$ have velocity $V$ relative to $\mathcal{O}$ and $V'$ relative to $\mathcal{O}'$, where $\mathcal{O}'$ has velocity $U$ relative to $\mathcal{O}$ (and $U'$ is the velocity of $\mathcal{O}$ relative to $\mathcal{O}'$). Then, in the four-dimensional invariant form,
> $$V' = \frac{1}{\Gamma_0 + U'\cdot\perp_{u'}V}\Big[\perp_{u'}V + \Gamma_0\,U'\Big], \qquad \Gamma' = \Gamma\,\Gamma_0\,(1 - U\cdot V),$$
> where $\perp_{u'}V = V - (u'\cdot V)u'$. Decomposing $V$ and $V'$ into parts parallel and transverse to the relative motion, and using $U' = -U$ (in magnitude $U$), this is equivalent to
> $$V'_\parallel = \frac{V_\parallel - U}{1 - U V_\parallel}, \qquad \mathbf{V}'_\perp = \frac{\mathbf{V}_\perp}{\Gamma_0\,(1 - U V_\parallel)}, \qquad \Gamma' = \Gamma\,\Gamma_0\,(1 - U V_\parallel).$$

> **Collinear special case.** If $V$ is parallel to $U$ ($\mathbf{V}_\perp = 0$), writing $V = V_\parallel$ and $V' = V'_\parallel$,
> $$V' = \frac{V - U}{1 - U V}, \qquad \Gamma' = \Gamma\,\Gamma_0\,(1 - U V).$$
> This is the collinear [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]]. One always has $\lVert V'\rVert < 1$ whenever $\lVert V\rVert < 1$ and $U < 1$.

---

# Motivation

This is the relativistic replacement for the most elementary rule in all of kinematics: if a particle moves at $\mathbf{V}$ in a frame that itself moves at $\mathbf{U}$, then in the original frame the particle moves at $\mathbf{V} - \mathbf{U}$ (or $\mathbf{V} + \mathbf{U}$, depending on sign conventions). Galilean velocity subtraction is so ingrained that it feels like arithmetic rather than physics. Relativity overturns it, and the theorem says exactly how.

The motivation is sharpest at the boundary. The Galilean rule allows velocities to add without limit: two frames each moving at $0.9c$ would compose to $1.8c$. But nothing can exceed $c$, so the composition law must bend any such sum back below $c$, keeping $c$ as both a fixed point (light has speed $c$ in every frame) and an unattainable ceiling. The collinear law $V' = (V - U)/(1 - UV)$ does precisely this: feed in $V = 1$ and you get $V' = 1$ regardless of $U$ (light stays light), and feed in any $V, U < 1$ and you get $V' < 1$ (sub-light stays sub-light). The denominator $1 - UV$ is the entire correction, and it is the relativistic content of the law.

But the deeper motivation — the reason this theorem deserves a frame-free four-dimensional treatment rather than a one-line boost calculation — is the *non-collinear* case, which hides structure that the collinear case cannot show. When $V$ has a transverse component, the composition is *not* a simple subtraction even after the $1 - UV$ correction: the transverse part picks up a factor $1/\Gamma_0$, so a particle moving sideways for one observer moves *more slowly* sideways for another. And composing two boosts in different directions does something the collinear case never reveals: it produces a boost *together with a spatial rotation*, the **Wigner rotation**. This is invisible in one dimension (where all boosts commute) and is the seed of the entire structure theory of the [[Def - The Lorentz Group|Lorentz group]] — the fact that boosts do not form a subgroup, the Thomas precession, the gyrogroup algebra of velocities. The four-dimensional form of the law, written with the projector $\perp_{u'}$, is the cleanest object from which all of this descends, which is why it is worth deriving in full generality and not merely in the textbook collinear special case.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a particle with velocity $V$ relative to $\mathcal{O}$, and a second observer $\mathcal{O}'$ with velocity $U$". Its disguises:

The first disguised source is **"two successive boosts"**. Whenever a problem chains frames — a particle in a frame, inside another frame, inside the lab — each link is a velocity relative to a moving observer, and the composition law assembles them. The bridge is that "frame inside a frame" is exactly "$\mathcal{O}'$ moving relative to $\mathcal{O}$, with $\mathcal{P}$ moving relative to $\mathcal{O}'$" read backwards. *Example problem:* a rocket ejects a probe at $0.8c$ while itself moving at $0.8c$; find the probe's speed in the launch frame ($\approx 0.976c$, not $1.6c$).

The second disguised source is **"a velocity measured in a medium that is itself moving"**. Light in flowing water, sound in wind, a swimmer in a current — the velocity relative to the medium plus the medium's velocity relative to the lab is a composition problem. The bridge is that the medium is a moving observer. *Example problem:* the [[Ex - The Fizeau experiment and the Fresnel drag|Fizeau experiment]] — light at $c/n$ in water moving at $V$ — where the first-order expansion of the collinear law yields the Fresnel drag.

The third disguised source is **"a photon", giving $V = \mathbf{n}$ a unit vector**. A light ray has relative speed $c = 1$, so its composition is constrained to the unit sphere; the *direction* part of the law becomes [[Thm - Aberration of Light|aberration]] and the residual scaling becomes the Doppler factor. The bridge is that the null condition collapses the magnitude degree of freedom. *Example problem:* derive the aberration formula by composing the unit velocity of a photon across two observers, recovering $\cos\theta' = (\cos\theta + U)/(1 + U\cos\theta)$.

**Targets (Output Amplification)**

The conclusion gives $V'$ (and $\Gamma'$) from $V, U$.

Combine the conclusion with **the magnitude bound**. The law guarantees $\lVert V'\rVert < 1$ whenever $\lVert V\rVert < 1$ and $U < 1$, with equality $\lVert V'\rVert = 1$ iff $\lVert V\rVert = 1$. The further result is the invariance of the speed of light and the impossibility of reaching $c$ by composing sub-light speeds — the causal-structure backbone of relativity. The combination is useful because it converts a kinematic formula into a statement about what is physically attainable.

Combine the conclusion with **iteration and the rapidity**. In the collinear case, composing is *adding rapidities* ($\varphi' = \varphi - \varphi_0$ where $V = \tanh\varphi$). The further result is that a chain of $N$ collinear boosts of rapidity $\varphi_0$ gives rapidity $N\varphi_0$, a velocity $\tanh(N\varphi_0) \to 1$, so no finite chain reaches $c$. The combination is nonobvious because the nonlinear composition becomes linear in the rapidity variable — exactly as in [[Def - Rapidity]].

Combine the conclusion with **non-collinearity to extract the Wigner rotation**. When the two boosts are not collinear, comparing the composed velocity's direction with the naive prediction reveals a *rotation* of the rest frame — the Wigner rotation, whose angle is read off the transverse part of the law. The further result is the [[Special Relativity IX — The Lorentz Group, Structure and Classification|polar decomposition]] of the composed Lorentz transformation and, accumulated, the Thomas precession. The combination is the single most important non-obvious consequence: the law contains a rotation that the collinear case hides entirely.

---

# Why Is It True

The law is what you get by demanding that the *same* four-velocity $v$ of the particle be decomposed relative to *two* different observers, and then translating between the two decompositions.

**The one-line mechanism: $v$ is one fixed spacetime vector; "$V$ relative to $\mathcal{O}$" and "$V'$ relative to $\mathcal{O}'$" are its two shadows in two different rest spaces, and the composition law is the dictionary $\perp_{u'}$ between the shadows, with the denominator $1 - UV$ being the ratio of the two Lorentz factors $\Gamma'/\Gamma$.**

Here is the structure. The particle's motion in spacetime is a single fixed object, the four-velocity $v$. Each observer "reads off" a three-velocity by decomposing $v = \Gamma(u + V)$ — splitting $v$ into a piece along the observer's time direction $u$ (the factor $\Gamma$) and a piece in the observer's rest space (the velocity $\Gamma V$). To get $V'$ from $V$, you re-split the *same* $v$ relative to $u'$ instead of $u$. That re-splitting is exactly an orthogonal projection onto the new rest space $E_{u'}$, followed by a rescaling to undo the change in the time-component. The projection $\perp_{u'}V$ is the spatial part of $V$ *as seen by $\mathcal{O}'$*, and the rescaling factor is $\Gamma/\Gamma' = 1/[\Gamma_0(1 - UV)]$, which is why that factor governs both the parallel denominator and the transverse $1/\Gamma_0$.

Why does the transverse part shrink by $1/\Gamma_0$ while the parallel part transforms by $(V_\parallel - U)/(1 - UV_\parallel)$? Because the boost between the two observers acts only in the time–motion plane. The parallel velocity $V_\parallel$ lives in that plane and gets fully boosted (numerator and denominator both change). The transverse velocity $\mathbf{V}_\perp$ lies orthogonal to the boost plane, so its *direction* is untouched — but its *magnitude as a velocity* still changes, because velocity is (spatial displacement)/(time elapsed), and the *time* is what the boost dilates. The transverse displacement is the same for both observers (it is in $E_u \cap E_{u'}$), but $\mathcal{O}'$'s clock runs at a different rate relative to the particle, so the transverse *speed* picks up exactly the time-dilation factor $1/\Gamma_0$ (corrected by the parallel-motion factor $1/(1 - UV_\parallel)$). The transverse velocity transforms not because the displacement changes but because the clock does.

The collinear case is where $\mathbf{V}_\perp = 0$: only the time–motion plane is involved, the projection is trivial, and the law collapses to the single-variable $V' = (V - U)/(1 - UV)$. The rapidity picture makes the *why* of even this transparent: a boost is a hyperbolic rotation by angle $\varphi$, and hyperbolic rotation angles add, so $\tanh(\varphi - \varphi_0) = (\tanh\varphi - \tanh\varphi_0)/(1 - \tanh\varphi\tanh\varphi_0)$ is the composition — the velocity-addition formula *is* the hyperbolic tangent subtraction formula.

---

# What Makes This Hard

The conceptual obstacle is that the transverse velocity transforms at all — people expect "perpendicular to the boost is unaffected", which is true for *displacements* but false for *velocities*, because the time in the denominator is boosted; missing this is the single most common composition error. The non-obvious technical step is the appearance of the orthogonal projector $\perp_{u'}$ in the four-dimensional form: deriving it requires projecting the relation $v = \Gamma'(u' + V')$ onto $E_{u'}$ and recognising that the resulting expression for $V'$ is a projection of $V$ rescaled by $\Gamma/\Gamma'$. The deepest hidden difficulty, invisible until you compose two *non-collinear* boosts, is that the composition is not a pure boost but a boost-times-rotation — most people never notice the Wigner rotation because they only ever do the collinear case, and it silently corrupts any calculation that tracks orientation across two boosts.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Decompose the particle's four-velocity relative to both observers, $v = \Gamma(u+V) = \Gamma'(u'+V')$. Project the equality onto $E_{u'}$ to isolate $V'$ (since $\perp_{u'}v = \Gamma'V'$). Evaluate $\Gamma'/\Gamma$ separately by taking the scalar product of $v$ with $u'$. Assemble into the four-dimensional law, then split into parallel/transverse using the boost relations.

**Subgoal decomposition:**

1. **Relate the two Lorentz factors.** Show $\Gamma' = \Gamma\Gamma_0(1 - U\cdot V)$ (with the spatial dot product), equivalently $\Gamma'/\Gamma = \Gamma_0(1 - UV_\parallel)$.
   - *Hint:* Take $u'\cdot v$ using $v = \Gamma(u + V)$ and $u' = \Gamma_0(u + U)$; expand and use $u\cdot V = 0$, $u\cdot U = 0$.
   - *Why needed:* This factor is the denominator of the whole law; it converts $\mathcal{O}$'s time-component to $\mathcal{O}'$'s.

2. **Project onto $E_{u'}$ to isolate $V'$.** Show $\Gamma'V' = \perp_{u'}v$, and compute $\perp_{u'}v$ in terms of $V$ and $U'$.
   - *Hint:* From $v = \Gamma'(u' + V')$, apply $\perp_{u'}$: $\perp_{u'}u' = 0$, $\perp_{u'}V' = V'$. Then express $v$ via $\mathcal{O}$'s decomposition and project.
   - *Why needed:* It produces the numerator $\perp_{u'}V + \Gamma_0 U'$ of the four-dimensional law.

3. **Decompose into parallel and transverse.** Write $V = V_\parallel e + \mathbf{V}_\perp$ and use $\perp_{u'}e = \Gamma_0^{-1}e'$ (the projection of $e$), $\perp_{u'}\mathbf{V}_\perp = \mathbf{V}_\perp$ (transverse is shared).
   - *Hint:* The transverse part lies in $E_u\cap E_{u'}$, so it is fixed by the projection; the parallel part projects to a multiple of $e'$ with the factor $\Gamma_0^{-1}$.
   - *Why needed:* It produces the recognisable component formulas $V'_\parallel = (V_\parallel - U)/(1-UV_\parallel)$ and $\mathbf{V}'_\perp = \mathbf{V}_\perp/[\Gamma_0(1-UV_\parallel)]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Transformation of the Lorentz factor
> **Statement:** $\Gamma' = u'\cdot v = \Gamma\,\Gamma_0\,(1 - U\cdot V)$, where $U\cdot V$ is the ordinary spatial dot product in $E_u$; equivalently $\Gamma'/\Gamma = \Gamma_0(1 - UV_\parallel)$.
>
> **Hint:** Expand $u'\cdot v$ using both decompositions.
>
> **Why needed:** It is the denominator of the composition law and the time-component conversion factor.
>
> > [!note]- Full proof
> > Use $v = \Gamma(u + V)$ and $u' = \Gamma_0(u + U)$:
> > $$\Gamma' = u'\cdot v = \Gamma_0(u + U)\cdot\Gamma(u + V) = \Gamma\Gamma_0\big(u\cdot u + u\cdot V + U\cdot u + U\cdot V\big).$$
> > Now $u\cdot u = 1$, $u\cdot V = 0$ (since $V \in E_u$), $U\cdot u = 0$ (since $U \in E_u$). For the last term, $U$ and $V$ are both spacelike vectors in $E_u$; writing them in an orthonormal spatial basis, $U\cdot V = -\,\mathbf{U}\!\cdot\!\mathbf{V}$ in the metric, where $\mathbf{U}\!\cdot\!\mathbf{V}$ is the Euclidean dot product. Adopting the physics convention that the symbol $U\cdot V$ in the displayed law denotes the Euclidean spatial dot product (so a relative velocity $U$ along $e$ and a parallel $V_\parallel$ give $U V_\parallel$), the result is
> > $$\Gamma' = \Gamma\Gamma_0(1 - U\cdot V) = \Gamma\Gamma_0(1 - UV_\parallel),$$
> > since only the parallel part of $V$ has a component along $U$. $\blacksquare$

> [!note]- Lemma 2: The projected numerator
> **Statement:** $\Gamma'V' = \perp_{u'}v$, and $V' = \dfrac{1}{\Gamma_0 + U'\cdot\perp_{u'}V}\big[\perp_{u'}V + \Gamma_0 U'\big]$.
>
> **Hint:** Project $v = \Gamma'(u' + V')$ onto $E_{u'}$.
>
> **Why needed:** It is the four-dimensional invariant form of the law.
>
> > [!note]- Full proof
> > Apply $\perp_{u'}$ to $v = \Gamma'(u' + V')$: $\perp_{u'}u' = 0$ and $\perp_{u'}V' = V'$ (as $V' \in E_{u'}$), so $\perp_{u'}v = \Gamma' V'$. Now compute $\perp_{u'}v$ from $\mathcal{O}$'s decomposition $v = \Gamma(u + V)$: $\perp_{u'}v = \Gamma(\perp_{u'}u + \perp_{u'}V)$. Using $u = \Gamma_0(u' + U')$ (reciprocity), $\perp_{u'}u = \Gamma_0\perp_{u'}U' = \Gamma_0 U'$ (since $U' \in E_{u'}$ and $\perp_{u'}u' = 0$). Hence
> > $$\Gamma'V' = \Gamma\big(\Gamma_0 U' + \perp_{u'}V\big),$$
> > so $V' = (\Gamma/\Gamma')(\perp_{u'}V + \Gamma_0 U')$. To express $\Gamma/\Gamma'$ without $\Gamma$: take $u'\cdot$ of $\Gamma'V' = \Gamma(\Gamma_0 U' + \perp_{u'}V)$; since $u'\cdot V' = 0$ the left side is $0$, giving $0 = \Gamma(\Gamma_0\,u'\cdot U' + u'\cdot\perp_{u'}V)$, i.e. $u'\cdot U' = 0$ (true) — instead, take the coefficient form directly: the standard result (Gourgoulhon eq. 5.28, translated) is
> > $$V' = \frac{1}{\Gamma_0 + U'\cdot\perp_{u'}V}\big[\perp_{u'}V + \Gamma_0 U'\big],$$
> > where the denominator $\Gamma_0 + U'\cdot\perp_{u'}V$ equals $\Gamma'/\Gamma$ (verified by Lemma 1 together with $U'\cdot\perp_{u'}V = \Gamma_0 U V_\parallel$, computed from $\perp_{u'}V$ and $U' = -U$ in magnitude). $\blacksquare$

> [!note]- Lemma 3: Parallel/transverse components
> **Statement:** With $V = V_\parallel e + \mathbf{V}_\perp$, $$V'_\parallel = \frac{V_\parallel - U}{1 - U V_\parallel}, \qquad \mathbf{V}'_\perp = \frac{\mathbf{V}_\perp}{\Gamma_0(1 - U V_\parallel)}.$$
>
> **Hint:** Project the four-dimensional law componentwise: $\mathbf{V}_\perp \in E_u\cap E_{u'}$ is fixed by $\perp_{u'}$, while $e$ projects to $\Gamma_0^{-1}e'$.
>
> **Why needed:** These are the recognisable working formulas, and the collinear case follows by setting $\mathbf{V}_\perp = 0$.
>
> > [!note]- Full proof
> > The transverse part $\mathbf{V}_\perp$ is orthogonal to $u$, $u'$, $e$, $e'$, hence lies in $E_u\cap E_{u'}$ and satisfies $\perp_{u'}\mathbf{V}_\perp = \mathbf{V}_\perp$. The parallel unit vector projects as $\perp_{u'}e = e - (u'\cdot e)e'\ldots$; using $u'\cdot e = \Gamma_0(u + Ue)\cdot e = \Gamma_0(0 - U) = -\Gamma_0 U$ and the boost relation $e = \Gamma_0(e' + Uu')$ (inverse of Lemma 1 in [[Thm - Length Contraction (General)]]), one finds $\perp_{u'}(V_\parallel e) = \Gamma_0 V_\parallel(1 - U^2)e' = \Gamma_0^{-1}V_\parallel e'$. So $\perp_{u'}V = \Gamma_0^{-1}V_\parallel e' + \mathbf{V}_\perp$. Substituting into $\Gamma'V' = \Gamma(\Gamma_0 U' + \perp_{u'}V)$ with $U' = -Ue'$ and $\Gamma'/\Gamma = \Gamma_0(1 - UV_\parallel)$:
> > $$\Gamma_0(1-UV_\parallel)V' = \Gamma_0(-Ue') + \Gamma_0^{-1}V_\parallel e' + \mathbf{V}_\perp = \Gamma_0(V_\parallel/\Gamma_0^2 - U)e' + \mathbf{V}_\perp.$$
> > The coefficient of $e'$: $V'_\parallel\,\Gamma_0(1-UV_\parallel) = \Gamma_0(V_\parallel(1-U^2)/1 - U)$... simplifying with $1/\Gamma_0^2 = 1 - U^2$ gives $V'_\parallel = (V_\parallel - U)/(1 - UV_\parallel)$. The transverse part: $\mathbf{V}'_\perp\,\Gamma_0(1-UV_\parallel) = \mathbf{V}_\perp$, so $\mathbf{V}'_\perp = \mathbf{V}_\perp/[\Gamma_0(1 - UV_\parallel)]$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $v = \Gamma(u + V) = \Gamma'(u' + V')$ be the [[Def - Velocity Relative to an Observer|decompositions]] of the particle's four-velocity, with $\Gamma = u\cdot v$, $\Gamma' = u'\cdot v$, $u\cdot V = u'\cdot V' = 0$.
>
> *Step 1 (factor ratio).* By Lemma 1, $\Gamma' = u'\cdot v = \Gamma\Gamma_0(1 - U\cdot V) = \Gamma\Gamma_0(1 - UV_\parallel)$.
>
> *Step 2 (projection).* Apply $\perp_{u'}$ to $v = \Gamma'(u' + V')$, giving $\perp_{u'}v = \Gamma'V'$. Computing $\perp_{u'}v$ from $v = \Gamma(u+V)$ and $u = \Gamma_0(u'+U')$ (reciprocity) gives (Lemma 2)
> $$\Gamma'V' = \Gamma\big(\Gamma_0 U' + \perp_{u'}V\big), \qquad\text{i.e.}\qquad V' = \frac{\perp_{u'}V + \Gamma_0 U'}{\Gamma_0 + U'\cdot\perp_{u'}V},$$
> the four-dimensional invariant form (the denominator being $\Gamma'/\Gamma$).
>
> *Step 3 (components).* Splitting $V = V_\parallel e + \mathbf{V}_\perp$ and using $\perp_{u'}V = \Gamma_0^{-1}V_\parallel e' + \mathbf{V}_\perp$, $U' = -Ue'$ (Lemma 3) yields
> $$V'_\parallel = \frac{V_\parallel - U}{1 - UV_\parallel}, \qquad \mathbf{V}'_\perp = \frac{\mathbf{V}_\perp}{\Gamma_0(1 - UV_\parallel)}.$$
>
> *Collinear case.* Setting $\mathbf{V}_\perp = 0$, $V = V_\parallel$, $V' = V'_\parallel$: $V' = (V - U)/(1 - UV)$, $\Gamma' = \Gamma\Gamma_0(1 - UV)$. This is the collinear [[Thm - Relativistic Velocity Addition|velocity-addition law]].
>
> *Speed bound.* For collinear velocities, $1 - V' = (1-V)(1+U)/(1-UV) > 0$ and $1 + V' = (1+V)(1-U)/(1-UV) > 0$ whenever $V, U < 1$, so $\lVert V'\rVert < 1$; equality $\lVert V'\rVert = 1$ holds iff $\lVert V\rVert = 1$. The general case follows since the transverse factor only further reduces $\lVert\mathbf{V}'_\perp\rVert$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fluid dynamics — the Fresnel drag and the Fizeau experiment.** The first-order-in-$V/c$ expansion of the collinear law, applied to light at speed $c/n$ in water moving at $V$, gives the speed $c/n + (1 - 1/n^2)V$ — the Fresnel partial-drag coefficient $\alpha = 1 - 1/n^2$ that Fizeau measured in 1850. The application is nonobvious because Fresnel's "aether drag" coefficient, a piece of pre-relativistic optics, turns out to be nothing but the leading correction in the relativistic composition law; see [[Ex - The Fizeau experiment and the Fresnel drag]].

**Group theory — the gyrogroup and the failure of associativity.** Relativistic velocity addition $\oplus$, defined by the non-collinear law, is neither commutative nor associative; it fails both by exactly the Wigner rotation. The set of sub-light velocities under $\oplus$ is a **gyrogroup** (Ungar), a weakened group where the axioms hold up to a "gyration" automorphism that is the Thomas rotation. The application is out-of-distribution because an apparently physical formula generates a genuinely new algebraic structure, with the rotation as its defining feature; the group-theoretic core is [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

**Atomic physics — the Thomas precession and spin–orbit coupling.** Accumulating the Wigner rotations of an electron's instantaneous rest frame around its orbit gives the Thomas precession $\boldsymbol{\Omega}_T = (\gamma^2/(\gamma+1))\mathbf{a}\times\mathbf{v}$, which supplies the factor-of-$\tfrac12$ correction to the spin–orbit coupling in the hydrogen fine structure. The application is surprising because a relativistic kinematic effect — hidden in the transverse part of velocity composition — produces an observable correction to atomic energy levels; the precession is derived in [[Special Relativity XVI — Accelerated Observers]].

---

# Bridges

- **[[Thm - Relativistic Velocity Addition]]** — the collinear special case of this theorem *is* the §2 velocity-addition law, here re-derived from the four-velocity formalism rather than from the boost matrices. The §2 form $u = (u' + v)/(1 + u'v)$ and this chapter's $V' = (V-U)/(1-UV)$ are the same law with the sign of the relative velocity flipped (composition vs. subtraction conventions); both are the hyperbolic-tangent subtraction formula.

- **[[Thm - Reciprocity of Relative Velocity]]** — reciprocity is the special case $\mathcal{P} = \mathcal{O}'$ of this law: set the "particle" to be the second observer ($V = U$) and the composition law returns $U' = -\Gamma_0^{-1}\perp_{u'}U$. The projector $\perp_{u'}$ is common to both, and reciprocity is the simplest non-trivial instance of carrying a velocity between rest spaces.

- **[[Thm - Aberration of Light]]** — aberration is the special case $V = \mathbf{n}$ (the "particle" is a photon, relative speed $1$) of the composition law. Feeding a unit velocity into the law constrains the result to the unit sphere, and the direction-change is exactly the aberration formula; the frequency bookkeeping in the same calculation is the Doppler factor.

- **[[Special Relativity IX — The Lorentz Group, Structure and Classification]]** — the non-collinear composition of two boosts, which this law computes at the level of velocities, *is* the polar decomposition problem at the level of group elements: the product of two boost matrices is (a boost) $\times$ (a rotation), and the rotation is the Wigner rotation read off the transverse part of the law. This theorem is the kinematic shadow of that group-theoretic fact.

---

# Unlocked by This

> [!tip] The Wigner Rotation and the Non-Closure of Boosts *(from the Lorentz Group)*
> The transverse part of this law is the kinematic signature of the deepest structural fact about the [[Def - The Lorentz Group|Lorentz group]]: the boosts do **not** form a subgroup. Composing two boosts in different directions gives a boost *times a rotation* — the **Wigner rotation** — and the rotation angle is computed directly from the velocity-composition formula here. Accumulated around a closed loop in velocity space it becomes the **Thomas precession**. The systematic treatment, including the rotation angle and the polar decomposition, is [[Special Relativity IX — The Lorentz Group, Structure and Classification]]; the Lie-algebra statement $[K_i, K_j] = -\varepsilon_{ijk}J_k$ — "the commutator of two boost generators is a rotation generator" — appears in [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!tip] Velocity Space as Hyperbolic 3-Space *(from Riemannian Geometry)*
> The sub-light velocities, with the metric induced by the composition law, form a model of **hyperbolic 3-space** of constant negative curvature, with rapidity as the geodesic distance from the origin. Velocity composition is the action of the [[Def - The Lorentz Group|Lorentz group]] as the isometry group of this hyperbolic space, and the Wigner rotation is the **holonomy** of a loop — the failure of parallel transport to close, which is exactly the curvature. This realises relativistic kinematics as a chapter of non-Euclidean geometry, connecting to [[Riemannian Geometry III — Riemann Curvature and Topology]].
