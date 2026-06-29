---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Let a massive particle move along a timelike worldline parametrised by its proper time $\tau$, with four-velocity $U^\mu = dX^\mu/d\tau$ and four-acceleration $A^\mu = dU^\mu/d\tau$. Working with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$:

1. Show directly from the definition that the four-velocity is unit-normalised, $U \cdot U = 1$, in two ways: (a) by evaluating in a general inertial frame using $U^\mu = \gamma(1, \mathbf{u})$, and (b) by evaluating in the particle's instantaneous rest frame.
2. Deduce that the four-acceleration is Minkowski-orthogonal to the four-velocity, $A \cdot U = 0$, by differentiating the result of part 1.
3. Show that the four-acceleration is spacelike or zero, $A \cdot A \le 0$, with equality if and only if $A = 0$. (Use the fact, to be proved here, that any vector orthogonal to a timelike vector is spacelike or zero.)
4. Verify all three properties on the explicit example of uniformly accelerated (hyperbolic) motion, $U^\mu = (\cosh a\tau, \sinh a\tau, 0, 0)$.

**Recall:**

![[Def - Four-Velocity and Four-Acceleration#The Definition]]

The Minkowski inner product is $X \cdot Y = \eta_{\mu\nu}X^\mu Y^\nu = X^0 Y^0 - \mathbf{X}\cdot\mathbf{Y}$; a vector is [[Def - Classification of Four-Vectors|timelike]] if $X \cdot X > 0$, spacelike if $X \cdot X < 0$, null if $X \cdot X = 0$. The factor $\gamma = (1 - u^2)^{-1/2}$ relates [[Def - Proper Time|proper time]] to coordinate time by $dt/d\tau = \gamma$.

---

# Convergent Strategy

**Problem class.** A *verify-an-invariant-identity* problem — the most basic kind in the four-vector formalism. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: when an inner product of four-vectors must be evaluated, compute it in whichever frame makes it trivial, and the answer holds in all frames because inner products are Lorentz invariant. Here the identities are so basic they form the foundation every later dynamical calculation rests on.

**Assumption pattern.** The only inputs are the *definitions* of four-velocity and four-acceleration as proper-time derivatives, plus the normalisation choice that proper time is the metric arc length. The unit-norm of $U$ is not an extra assumption — it follows from $d\tau = \sqrt{ds^2}$. Everything else (orthogonality, spacelike acceleration) cascades from $U \cdot U = 1$ by differentiation and a single fact about the indefinite metric.

**Theorem routing.** Part 1 is direct computation. Part 2 routes through the product rule: differentiate the constant $U \cdot U = 1$ along the worldline. Part 3 routes through a structural fact about the signature — a [[Def - Classification of Four-Vectors|vector orthogonal to a timelike vector]] is spacelike or zero — proved by choosing a frame where the timelike vector is purely temporal. Part 4 is a consistency check on the canonical accelerated worldline.

**Key decision point.** The one genuinely instructive choice is in part 1(b) and part 3: *go to the rest frame of the particle*. In its rest frame $U = (1, \mathbf{0})$ and the inner products collapse to one-line statements; because $U \cdot U$ and $A \cdot A$ are invariants, the rest-frame answer is the universal answer. Trying to prove part 3 in a general frame, by manipulating components of $A^\mu = \gamma^4(u\dot u, \dot u, \dots)$, is possible but needlessly messy — the frame choice is the whole art.

---

# Legal Operations Used

1. **Compute an invariant in the most convenient frame** (operation 7 from the topic page). Both $U \cdot U$ and $A \cdot A$ are Lorentz scalars; evaluating them in the rest frame, where $U = (1,\mathbf 0)$, trivialises them.

2. **Differentiate a normalisation constraint** (operation 8 from the topic page). The orthogonality $A \cdot U = 0$ is obtained for free by differentiating $U \cdot U = 1$ with respect to proper time.

3. **Differentiate with respect to proper time** (operation 5 from the topic page). The four-acceleration is $dU/d\tau$, and the product rule for $d(U \cdot U)/d\tau$ is what delivers part 2.

---

# Hints

> [!note]- Hint 1
> For part 1(a), write out $U \cdot U = (U^0)^2 - |\mathbf{U}|^2 = \gamma^2(1 - u^2)$ and use the definition of $\gamma$. For part 1(b), recall that in the particle's rest frame $\mathbf{u} = 0$, so $\gamma = 1$ and $U = (1, \mathbf{0})$.

> [!note]- Hint 2
> The function $\tau \mapsto U(\tau) \cdot U(\tau)$ is constant (equal to $1$). Differentiate it with respect to $\tau$ using the product rule for the bilinear form $\eta$, remembering $dU/d\tau = A$.

> [!note]- Hint 3
> To prove "orthogonal to timelike $\Rightarrow$ spacelike or zero", go to the frame where the timelike vector $U$ is purely temporal, $U = (1, \mathbf{0})$. The orthogonality $A \cdot U = 0$ then forces $A^0 = 0$, so $A = (0, \mathbf{A})$ is purely spatial — compute its norm.

> [!note]- Hint 4
> For part 4, differentiate $U^\mu = (\cosh a\tau, \sinh a\tau, 0, 0)$ to get $A$, then form $U \cdot U$, $A \cdot U$, $A \cdot A$ using $\cosh^2 - \sinh^2 = 1$.

---

# Solution

These three identities are the algebraic backbone of relativistic kinematics, and all three flow from a single source: proper time is the metric arc length, so the proper-time derivative of the four-position is a *unit* tangent. The plan: Step 1 establishes $U \cdot U = 1$ from the definition (two ways); Step 2 differentiates it to get $A \cdot U = 0$; Step 3 uses a frame argument to show $A$ is spacelike or zero; Step 4 checks everything on hyperbolic motion.

**Step 1: The four-velocity has unit norm, $U \cdot U = 1$.**

> [!note]- Derivation
> *(a) General frame.* In an inertial frame the four-velocity is $U^\mu = \gamma(1, \mathbf{u})$ with $\gamma = (1 - u^2)^{-1/2}$, $u = |\mathbf{u}|$. Its Minkowski norm is
> $$U \cdot U = (U^0)^2 - |\mathbf{U}|^2 = \gamma^2 \cdot 1 - \gamma^2 u^2 = \gamma^2(1 - u^2) = \frac{1 - u^2}{1 - u^2} = 1.$$
>
> *(b) Rest frame.* In the particle's instantaneous rest frame $\mathbf{u} = 0$, so $\gamma = 1$ and $U = (1, 0, 0, 0)$. Then $U \cdot U = 1^2 - 0 = 1$. Since $U \cdot U$ is a Lorentz scalar — the same number in every inertial frame — this rest-frame value $1$ is the value in *all* frames, confirming (a) without any algebra. The unit norm is a direct consequence of parametrising by proper time: $U \cdot U = \dfrac{dX}{d\tau}\cdot\dfrac{dX}{d\tau} = \dfrac{ds^2}{d\tau^2} = 1$ because $d\tau = \sqrt{ds^2}$ by [[Def - Proper Time|definition]].

**Step 2: The four-acceleration is orthogonal to the four-velocity, $A \cdot U = 0$.**

> [!note]- Derivation
> The quantity $U \cdot U$ is identically $1$ along the worldline, so its proper-time derivative vanishes. By the product rule for the symmetric bilinear form $\eta$,
> $$0 = \frac{d}{d\tau}(U \cdot U) = \frac{d}{d\tau}\big(\eta_{\mu\nu}U^\mu U^\nu\big) = 2\,\eta_{\mu\nu}\frac{dU^\mu}{d\tau}U^\nu = 2\, A \cdot U.$$
> Hence $A \cdot U = 0$: the four-acceleration is Minkowski-orthogonal to the four-velocity. This costs nothing beyond Step 1 — orthogonality is the derivative of unit-normalisation. Geometrically, $U$ is confined to the unit hyperboloid $\{X : X \cdot X = 1\}$, and $A = dU/d\tau$ is tangent to that surface, hence orthogonal to the radial direction $U$.

**Step 3: The four-acceleration is spacelike or zero, $A \cdot A \le 0$.**

> [!note]- Derivation
> We prove the general fact: *any vector orthogonal to a timelike vector is spacelike or zero.* Let $U$ be timelike (here $U \cdot U = 1 > 0$) and let $A \cdot U = 0$. Work in the frame where $U$ is purely temporal, $U = (1, \mathbf{0})$ — such a frame exists because $U$ is future timelike (it is the rest frame). The orthogonality condition reads
> $$0 = A \cdot U = A^0 \cdot 1 - \mathbf{A}\cdot\mathbf{0} = A^0,$$
> so $A^0 = 0$: in this frame the four-acceleration is purely spatial, $A = (0, \mathbf{A})$. Its norm is then
> $$A \cdot A = (A^0)^2 - |\mathbf{A}|^2 = -|\mathbf{A}|^2 \le 0,$$
> with equality if and only if $\mathbf{A} = 0$, i.e. $A = 0$. Since $A \cdot A$ is invariant, $A \cdot A \le 0$ in every frame: the four-acceleration is spacelike, or zero precisely when the worldline is straight. The **proper acceleration** is $a = \sqrt{-A \cdot A} = |\mathbf{A}|_{\text{rest}}$, the magnitude of the ordinary acceleration in the rest frame — what an accelerometer reads.

**Step 4: Verification on hyperbolic motion.**

> [!note]- Derivation
> Take $U^\mu(\tau) = (\cosh a\tau, \sinh a\tau, 0, 0)$, the four-velocity of a particle with constant proper acceleration $a$ along $x$ (the [[Def - Rapidity|rapidity]] $a\tau$ grows linearly with proper time).
> - *Unit norm:* $U \cdot U = \cosh^2 a\tau - \sinh^2 a\tau = 1$. ✓
> - *Four-acceleration:* $A^\mu = dU^\mu/d\tau = (a\sinh a\tau, a\cosh a\tau, 0, 0)$.
> - *Orthogonality:* $A \cdot U = (a\sinh a\tau)(\cosh a\tau) - (a\cosh a\tau)(\sinh a\tau) = 0$. ✓
> - *Spacelike:* $A \cdot A = (a\sinh a\tau)^2 - (a\cosh a\tau)^2 = a^2(\sinh^2 - \cosh^2) = -a^2 < 0$, so $\|A\| = a$ is constant. ✓
>
> All three identities hold, and the proper acceleration is the constant $a$ — confirming that this is genuinely "uniformly accelerated" motion.

> [!note]- Complete formal solution
> In an inertial frame $U^\mu = \gamma(1, \mathbf{u})$, so $U \cdot U = \gamma^2(1 - u^2) = 1$; equivalently, in the rest frame $U = (1, \mathbf 0)$ gives $U \cdot U = 1$, and invariance extends it to all frames (the deep reason being $U\cdot U = ds^2/d\tau^2 = 1$). Differentiating the constant identity $U \cdot U = 1$ along the worldline, $0 = \frac{d}{d\tau}(U \cdot U) = 2A \cdot U$, so $A \cdot U = 0$. To see $A$ is spacelike or zero, pass to the rest frame where $U = (1, \mathbf 0)$; then $A \cdot U = A^0 = 0$, so $A = (0, \mathbf A)$ and $A \cdot A = -|\mathbf A|^2 \le 0$, zero iff $A = 0$; invariance extends this to all frames. On hyperbolic motion $U = (\cosh a\tau, \sinh a\tau, 0, 0)$, $A = a(\sinh a\tau, \cosh a\tau, 0, 0)$, one checks $U\cdot U = 1$, $A \cdot U = 0$, $A \cdot A = -a^2$, with proper acceleration $\|A\| = a$ constant. $\blacksquare$

---

# Key Takeaways

**Unit norm, orthogonality, and spacelike acceleration are one fact differentiated twice — and each is a free equation.** The single source is that proper time is the metric arc length, which makes $U = dX/d\tau$ a unit vector, $U \cdot U = 1$. Differentiate once and orthogonality $A \cdot U = 0$ falls out; combine with one structural fact about the indefinite metric and $A \cdot A \le 0$ follows. None of these required solving the equation of motion or knowing the forces — they hold on *every* worldline, for *every* particle, identically. The reusable reflex: whenever you have a four-velocity in a problem, you immediately have two free scalar equations ($U \cdot U = 1$ and $A \cdot U = 0$) to exploit, before any dynamics. This is why relativistic calculations are often shorter than their Newtonian counterparts — the kinematic constraints are handed to you.

**Compute invariants in the rest frame: the master labour-saving move.** Both $U \cdot U$ and $A \cdot A$ are Lorentz scalars, so they may be evaluated in any convenient frame, and the rest frame — where $U = (1, \mathbf{0})$ — is almost always the convenient one. In it, $U \cdot U = 1$ is immediate and the proof that $A$ is spacelike reduces to "$A^0 = 0$, so $A$ is purely spatial". The general-frame computation with $\gamma^4$ factors is avoidable. The trigger for this move is any quantity you can recognise as a frame-independent inner product or norm; the action is "evaluate where the four-velocity is $(1, \mathbf{0})$ and transport the scalar answer everywhere". This same move computes invariant masses, relative speeds ($U \cdot U' = \gamma_{\text{rel}}$), and threshold energies throughout [[Special Relativity XIII — Energy and Momentum|relativistic dynamics]].

**Orthogonality of $A$ to $U$ is why a force cannot change rest mass.** The geometric statement "$A \cdot U = 0$" has a powerful physical reading: a unit vector can only change by sliding along the surface of unit vectors, never by changing length, so the four-velocity's "length" (which encodes the rest mass once you multiply by $m$ to get the four-momentum) is preserved. Concretely, the [[Def - Four-Force|four-force]] $F = mA$ inherits $F \cdot U = 0$, and this is precisely the statement $dm/d\tau = 0$: an ordinary mechanical or electromagnetic force changes a particle's energy and momentum but never its rest mass. When a process *does* change rest mass (radiation reaction, particle decay), the four-force acquires a component along $U$ and is no longer of the simple form $mA$. The diagnostic to carry away: orthogonality to the four-velocity is the relativistic signature of "rest-mass-preserving", and any violation flags a process that converts rest mass into something else. See [[Ex - Proper time along an accelerated worldline]] for the same four-velocity put to work computing elapsed time.
