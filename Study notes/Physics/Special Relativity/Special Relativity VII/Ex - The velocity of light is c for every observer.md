---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Invariance of the Velocity of Light"
  - "Def - Photon Propagation Direction and Velocity"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ in the mostly-minus signature, with observers' four-velocities all future timelike unit vectors:

1. Let $\ell$ be a future null vector along a photon's worldline, adapted to an observer $\mathcal{O}$ by $\ell \cdot U_0 = 1$. By decomposing $\ell = U_0 + N$ and imposing $\ell \cdot \ell = 0$, prove that the propagation direction $N$ is a *unit* vector, $|\mathbf N| = 1$, hence that the photon's local speed is $c$.
2. Show explicitly that this derivation used *only* $U_0 \cdot U_0 = 1$ and $\ell \cdot \ell = 0$ — nothing about whether $\mathcal{O}$ is inertial or accelerated — so the result holds for *every* observer at a point of their own worldline.
3. Take a concrete photon with adapted null vector $\ell = e_0 + e_1$ in an inertial frame. Now boost to a second inertial observer $\mathcal{O}'$ moving at speed $v$ along $e_1$, with four-velocity $U_0' = \Gamma(e_0 + v e_1)$. Re-adapt the *same* photon to $\mathcal{O}'$ (rescale so $\ell' \cdot U_0' = 1$) and verify that the new propagation direction $N'$ is again a unit vector — the speed is $c$ for $\mathcal{O}'$ too, even though $N' \neq N$ (aberration).
4. For a *uniformly accelerated* observer measuring a photon at position $\overrightarrow{OM} \neq 0$ in their rest space, the velocity is $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})\,N$. Show that the *norm* of this velocity is *not* $c$ in general, and identify the configuration where the coordinate speed of light vanishes (a horizon).

**Recall:**

The exercise rests on the invariance theorem and the adapted null vector.

![[Thm - Invariance of the Velocity of Light#Statement]]

A photon has no four-velocity; instead one uses the [[Def - Photon Propagation Direction and Velocity|adapted null vector]] $\ell$ with $\ell \cdot U_0 = 1$, decomposing as $\ell = U_0 + N$ with $N$ the propagation direction in the [[Def - Observer and Local Rest Space|local rest space]]. In mostly-minus, the unit condition $|\mathbf N| = 1$ reads $N \cdot N = -1$.

---

# Convergent Strategy

**Problem class.** A *photon / velocity-of-light* problem of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|fourth strategy]]: replace the four-velocity by the adapted null vector, exploit the null condition to make the propagation direction a unit vector, and track the qualification (local, or inertial) on the constancy of $c$.

**Assumption pattern.** The photon's tangent is null — the signal to use $\ell = U_0 + N$ with $\ell \cdot U_0 = 1$ instead of a unit four-velocity. The observer is arbitrary (parts 1–2 establish the result needs only $U_0 \cdot U_0 = 1$), then concretely two inertial observers (part 3 tests boost-invariance and exhibits aberration), then accelerated (part 4 exposes the position-dependent correction).

**Theorem routing.** Part 1 is the proof of [[Thm - Invariance of the Velocity of Light]]: expand $\ell \cdot \ell = 0$ to force $N \cdot N = -1$. Part 2 audits the proof to confirm its generality. Part 3 applies the adaptation to a boosted observer using [[Def - Photon Propagation Direction and Velocity]], confirming $|\mathbf N'| = 1$ while $N' \neq N$ — the seed of [[Thm - Aberration of Light|aberration]]. Part 4 uses the general velocity formula to show the norm departs from $c$ for an accelerated observer at $\overrightarrow{OM} \neq 0$, the kinematic precursor of a horizon.

**Key decision point.** The crux is the *scope* of the constancy of light: it is exact locally and for inertial observers, but a uniformly accelerated observer measures a position-dependent coordinate speed for distant light. The natural error is to over-generalise to "light always travels at $c$ for everyone everywhere"; the correct statement carries the qualification $\overrightarrow{OM} = 0$, and recognising where this matters (and where it does not) is the conceptual payoff, since the position-dependent speed is the kinematic seed of gravitational light-bending.

---

# Legal Operations Used

1. **Adapt a null vector to the observer for a photon** (operation 8 from the topic page). The photon's tangent is normalised by $\ell \cdot U_0 = 1$ instead of unit norm, giving $\ell = U_0 + N$.

2. **Use the null condition $\ell\cdot\ell = 0$** (the photon analogue of operation 4). Imposing nullity on the decomposition forces $|\mathbf N| = 1$, the source of the speed being $c$.

3. **Project onto the local rest space** (operation 3). The propagation direction is $N = \perp_{U_0}\ell$, the spatial part of the adapted null vector.

4. **Specialise to the simplest case, then add corrections** (operation 7). The local/inertial case gives $\mathbf V = cN$; the accelerated distant case adds the factor $1 + A_0\cdot\overrightarrow{OM}$.

---

# Hints

> [!note]- Hint 1
> Expand $0 = \ell\cdot\ell = (U_0 + N)\cdot(U_0 + N) = U_0\cdot U_0 + 2N\cdot U_0 + N\cdot N$. With $U_0\cdot U_0 = 1$ and $N\cdot U_0 = 0$ (rest-space part is orthogonal to $U_0$), this is $1 + N\cdot N = 0$, so $N\cdot N = -1$, i.e. $|\mathbf N| = 1$.

> [!note]- Hint 2
> Look back at Hint 1: the only facts used were $U_0\cdot U_0 = 1$ (true for *any* observer's four-velocity) and $\ell\cdot\ell = 0$ (the photon's nullity, a property of the photon). Neither mentions acceleration or rotation. So the result holds for every observer at a point of their worldline.

> [!note]- Hint 3
> To re-adapt to $\mathcal{O}'$: the photon direction is the null ray $\ell \propto e_0 + e_1$. Compute $(e_0 + e_1)\cdot U_0'$ with $U_0' = \Gamma(e_0 + v e_1)$: this is $\Gamma(1 - v)$. So $\ell' = (e_0 + e_1)/[\Gamma(1-v)]$ satisfies $\ell'\cdot U_0' = 1$. Then $N' = \ell' - U_0'$; check $|\mathbf N'| = 1$ by computing $N'\cdot N'$.

> [!note]- Hint 4
> For the accelerated observer, $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})N$ has norm $|1 + A_0\cdot\overrightarrow{OM}|\cdot|\mathbf N| = |1 + A_0\cdot\overrightarrow{OM}|$, which equals $1$ only if $A_0\cdot\overrightarrow{OM} = 0$. The coordinate speed *vanishes* when $1 + A_0\cdot\overrightarrow{OM} = 0$, i.e. $A_0\cdot\overrightarrow{OM} = -1$ — a surface behind the accelerating observer: the Rindler horizon.

---

# Solution

The route is to prove the local constancy of light from the null condition, audit the proof for generality, verify boost-invariance on a concrete photon (exhibiting aberration), and finally expose the position-dependent coordinate speed for an accelerated observer. Step 1 forces $|\mathbf N| = 1$; Step 2 confirms it needs only $U_0\cdot U_0 = 1$ and nullity; Step 3 boosts and checks; Step 4 finds the horizon. The non-obvious thread is that the constancy is exact locally and approximate globally, and the global correction is gravity in disguise.

**Step 1: The null condition forces $|\mathbf N| = 1$, so the local speed of light is $c$.**

> [!note]- Derivation
> The adapted null vector decomposes against the observer as $\ell = (\ell\cdot U_0)U_0 + \perp_{U_0}\ell = U_0 + N$, using $\ell\cdot U_0 = 1$ and writing $N = \perp_{U_0}\ell$ for the rest-space part, which satisfies $N\cdot U_0 = 0$. Impose the null condition $\ell\cdot\ell = 0$:
> $$0 = (U_0 + N)\cdot(U_0 + N) = \underbrace{U_0\cdot U_0}_{1} + 2\underbrace{N\cdot U_0}_{0} + N\cdot N = 1 + N\cdot N.$$
> Therefore $N\cdot N = -1$. Since $N$ is spacelike, its Euclidean rest-space norm is
> $$|\mathbf N| = \sqrt{-N\cdot N} = \sqrt{1} = 1.$$
> The propagation direction is automatically a unit vector. The photon's velocity (locally) is $\mathbf V = cN = N$, of norm $\|\mathbf V\|_g = c|\mathbf N| = c$. The constancy of the speed of light is exactly this: the $+1$ from the timelike part $U_0$ and the $-1$ from the spacelike part $N$ cancel (that is what "null" means), forcing $N$ to be unit length.

**Step 2: The derivation used only $U_0\cdot U_0 = 1$ and $\ell\cdot\ell = 0$ — so it holds for every observer.**

> [!note]- Derivation
> Audit Step 1. The expansion $0 = U_0\cdot U_0 + 2N\cdot U_0 + N\cdot N$ used three facts:
> - $U_0\cdot U_0 = 1$ — true for *any* observer's four-velocity, because every observer (inertial, accelerated, or rotating) has a future timelike *unit* four-velocity by definition;
> - $N\cdot U_0 = 0$ — true by construction, since $N = \perp_{U_0}\ell$ is the rest-space part, orthogonal to $U_0$ by definition of the projector;
> - $\ell\cdot\ell = 0$ — true because the photon's worldline is null, a property of the *photon*, not of the observer.
>
> None of these mentions the observer's acceleration $A_0$ or rotation $\boldsymbol\omega$. So the conclusion $|\mathbf N| = 1$, hence $\|\mathbf V\|_g = c$, holds for *every* observer at a point of their own worldline — inertial or not. This is the precise sense in which Einstein's postulate (about inertial frames) is a *special case* of a more general geometric fact: the local constancy of light is a property of null vectors in a Minkowski metric, and it does not care how the observer moves.

**Step 3: For a boosted observer, the propagation direction $N'$ is again unit length, though $N' \neq N$ (aberration).**

> [!note]- Derivation
> The photon's direction is the null ray spanned by $e_0 + e_1$. For the first observer $\mathcal{O}$ ($U_0 = e_0$), the adapted null vector is $\ell = e_0 + e_1$ (check $\ell\cdot U_0 = 1$), so $N = e_1$, $|\mathbf N| = 1$.
>
> For the boosted observer $\mathcal{O}'$ with $U_0' = \Gamma(e_0 + v e_1)$, re-adapt the *same* null ray. Compute the scalar product:
> $$(e_0 + e_1)\cdot U_0' = (e_0 + e_1)\cdot\Gamma(e_0 + v e_1) = \Gamma\big(e_0\cdot e_0 + v\,e_0\cdot e_1 + e_1\cdot e_0 + v\,e_1\cdot e_1\big) = \Gamma(1 + 0 + 0 - v) = \Gamma(1 - v).$$
> So to satisfy $\ell'\cdot U_0' = 1$ we rescale: $\ell' = \dfrac{e_0 + e_1}{\Gamma(1-v)}$. The new propagation direction is
> $$N' = \ell' - U_0' = \frac{e_0 + e_1}{\Gamma(1-v)} - \Gamma(e_0 + v e_1).$$
> Compute its norm. Using $\ell'\cdot\ell' = 0$ (still null) and $\ell'\cdot U_0' = 1$, the same expansion as Step 1 gives $N'\cdot N' = -(\ell'\cdot U_0')^2\cdot\frac{U_0'\cdot U_0'}{\cdots}$... more directly: $N' = \ell' - U_0'$, so
> $$N'\cdot N' = (\ell' - U_0')\cdot(\ell' - U_0') = \underbrace{\ell'\cdot\ell'}_{0} - 2\underbrace{\ell'\cdot U_0'}_{1} + \underbrace{U_0'\cdot U_0'}_{1} = 0 - 2 + 1 = -1.$$
> So $|\mathbf N'| = \sqrt{-N'\cdot N'} = 1$: the propagation direction is again a unit vector, and the speed of light is $c$ for $\mathcal{O}'$ too. But $N' \neq N$ in general — the photon arrives from a *different direction* for the boosted observer. This change of direction is **aberration**: the speed is invariant, the direction is not. (The general aberration formula expressing the angle of $N'$ in terms of the angle of $N$ and the boost $v$ is derived in [[Special Relativity VIII — Kinematics II, Change of Observer]].)

**Step 4: For an accelerated observer at a distance, the coordinate speed differs from $c$ and can vanish — a horizon.**

> [!note]- Derivation
> For a uniformly accelerated observer measuring a photon at position $\overrightarrow{OM} \neq 0$ in their rest space, the velocity is (from [[Def - Photon Propagation Direction and Velocity]], with $\boldsymbol\omega = 0$ for a non-rotating accelerated observer)
> $$\mathbf V = (1 + A_0\cdot\overrightarrow{OM})\,N.$$
> Its norm is
> $$\|\mathbf V\|_g = |1 + A_0\cdot\overrightarrow{OM}|\cdot|\mathbf N| = |1 + A_0\cdot\overrightarrow{OM}|,$$
> which equals $c = 1$ *only* when $A_0\cdot\overrightarrow{OM} = 0$ — that is, at the observer's own position ($\overrightarrow{OM} = 0$) or for a photon in the directions perpendicular to the acceleration. For a photon ahead of the observer (in the direction of $A_0$), $A_0\cdot\overrightarrow{OM} > 0$ and the coordinate speed *exceeds* $c$; for a photon behind, $A_0\cdot\overrightarrow{OM} < 0$ and it is *less* than $c$.
>
> The striking case is when
> $$1 + A_0\cdot\overrightarrow{OM} = 0,\qquad\text{i.e.}\qquad A_0\cdot\overrightarrow{OM} = -1,$$
> a surface *behind* the accelerating observer (in the direction opposite $A_0$, at distance $1/|A_0|$). There the coordinate speed of light *vanishes*: light at that surface, as the accelerated observer reckons it, stands still and never approaches. This is the **Rindler horizon** — the boundary beyond which the eternally accelerating observer can never receive a signal. It is not a violation of the constancy of light (which is local), but its global, accelerated-frame manifestation, and by the equivalence principle it is the special-relativistic precursor of the event horizon of a black hole and of the bending and slowing of light in a gravitational potential. The position-dependent coordinate speed $1 + A_0\cdot\overrightarrow{OM}$ is, to first order, the gravitational redshift factor $1 + \Phi$ with $\Phi$ the Newtonian potential — the bridge to [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!note]- Complete formal solution
> The [[Def - Photon Propagation Direction and Velocity|adapted null vector]] $\ell = U_0 + N$ (with $\ell\cdot U_0 = 1$, $N = \perp_{U_0}\ell$) satisfies $0 = \ell\cdot\ell = U_0\cdot U_0 + 2N\cdot U_0 + N\cdot N = 1 + N\cdot N$, so $N\cdot N = -1$, i.e. $|\mathbf N| = 1$ and the local speed of light is $\|\mathbf V\|_g = c$. This used only $U_0\cdot U_0 = 1$ (any observer) and $\ell\cdot\ell = 0$ (the photon), so it holds for every observer at a point of their worldline. For a boosted inertial observer $U_0' = \Gamma(e_0 + ve_1)$, re-adapting the photon $e_0 + e_1$ gives $\ell' = (e_0+e_1)/[\Gamma(1-v)]$ and $N' = \ell' - U_0'$ with $N'\cdot N' = \ell'\cdot\ell' - 2\ell'\cdot U_0' + U_0'\cdot U_0' = 0 - 2 + 1 = -1$, so $|\mathbf N'| = 1$ — the speed is $c$ for $\mathcal{O}'$ too, but $N' \neq N$ (aberration). For a uniformly accelerated observer at $\overrightarrow{OM} \neq 0$, $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})N$ has norm $|1 + A_0\cdot\overrightarrow{OM}| \neq c$ in general, vanishing where $A_0\cdot\overrightarrow{OM} = -1$ — the Rindler horizon, the kinematic precursor of gravitational light-bending. $\blacksquare$

---

# Key Takeaways

**The constancy of the speed of light is the cancellation of the $+1$ timelike norm against the $-1$ spacelike norm of a null vector — and it needs only that the observer's four-velocity be a unit vector.** The entire content of "light travels at $c$ for everyone" is the three-line algebra $0 = \ell\cdot\ell = 1 + N\cdot N$, forcing $N\cdot N = -1$, i.e. $|\mathbf N| = 1$. The timelike part of a null vector adapted by $\ell\cdot U_0 = 1$ has norm $+1$, the spacelike part has norm $-1$, they sum to zero (that is what null means), and so the spatial direction is automatically unit length. The crucial observation — drilled in part 2 — is that this used *only* $U_0\cdot U_0 = 1$, which every observer's four-velocity satisfies, and the nullity of the photon, which is the photon's property. So the constancy of light is not a postulate about inertial frames but a geometric fact about null vectors, valid for accelerated observers too (locally). The reusable insight: whenever you must show light travels at $c$, adapt the null tangent by $\ell\cdot U_0 = 1$ and the null condition delivers the unit propagation direction for free.

**The speed of light is invariant but its direction is not — that is the entire distinction between the constancy of $c$ and aberration.** Part 3 makes the point sharply: under a boost, the *same* photon has a different propagation direction $N' \neq N$ (it arrives from a different angle) but the *same* speed $|\mathbf N'| = |\mathbf N| = 1$. The boost re-slices the null cone with a different hyperplane, moving the point where the photon's ray crosses the rest space, but the null condition guarantees the spatial part is unit length whichever observer slices it. So a change of observer changes *where in the sky* a star appears (aberration) and *at what frequency* (Doppler), but never *how fast* its light travels. The reusable diagnostic: separate the three observer-dependent aspects of light — speed (invariant, always $c$), direction (aberration), frequency (Doppler) — and remember that only the latter two change under a boost. This separation is the organising principle of the change-of-observer optics in [[Special Relativity VIII — Kinematics II, Change of Observer]], and the conformal structure of the aberration map (it preserves angles between nearby stars) is the geometric heart of the spinor formalism in **Special Relativity XI**.

**The constancy of light is exact only locally; the position-dependent coordinate speed for an accelerated observer is gravity in disguise.** The qualification "$\overrightarrow{OM} = 0$" on the invariance theorem is not pedantry — it is the seam where special relativity meets gravity. A uniformly accelerated observer measures a coordinate speed $1 + A_0\cdot\overrightarrow{OM}$ for distant light: faster ahead, slower behind, and *zero* at the surface $A_0\cdot\overrightarrow{OM} = -1$ behind them — the Rindler horizon, beyond which no signal ever reaches them. By the equivalence principle, this accelerated-frame position-dependence is indistinguishable from the behaviour of light in a gravitational field, where light bends toward stronger potential and arrives delayed (the Shapiro delay), and the factor $1 + A_0\cdot\overrightarrow{OM}$ becomes the gravitational redshift factor $1 + \Phi$. The reusable principle: a local invariance with position-dependent global corrections is the universal signature of a tangent-space approximation to a curved geometry — special relativity is exact at a point and approximate in a neighbourhood, exactly as a tangent plane matches a curved surface to first order. This is the kinematic bridge from this chapter to [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]], the deflection of starlight, and black-hole horizons.
