---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Photons and Null Geodesics"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Problem Statement

A photon travels along the null worldline $x^\mu(\lambda) = \lambda\,(1, 1, 0, 0)$ in some inertial frame. Working with $c = 1$:

1. Show that the proper time along this worldline is identically zero, and conclude that the [[Def - Proper Time|proper-time]] machinery — and hence the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U = dX/d\tau$ — cannot be defined for a photon.
2. Show more sharply that there is *no* unit null vector: a null vector cannot be normalised to $U \cdot U = 1$, so a photon cannot have a four-velocity even in principle. Contrast with the timelike case.
3. Show that the photon nonetheless carries a well-defined **four-momentum** $P^\mu = E(1, 1, 0, 0)$, a null four-vector ($P \cdot P = 0$), parametrising the worldline by the affine parameter $\lambda$ with $P = dX/d\lambda$ (energy $E$).
4. Verify that the helix $x^\mu(\sigma) = (r\sigma, r\cos\sigma, r\sin\sigma, 0)$ is a null *curve* but not a null *geodesic*, so it is not the worldline of a free photon. Explain the distinction.

**Recall:**

![[Def - Photons and Null Geodesics#The Definition]]

A vector is [[Def - Classification of Four-Vectors|null]] when $X \cdot X = 0$. The [[Def - Proper Time|proper time]] is $\tau = \int\sqrt{ds^2}$, and the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is the unit tangent $U = dX/d\tau$ with $U \cdot U = 1$. The photon's energy–momentum is supplied by quantum mechanics through $E = \hbar\omega$.

---

# Convergent Strategy

**Problem class.** A *degenerate-limit / structural* problem: understanding precisely how and why the massive-particle machinery breaks for the photon, and what replaces it. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] note on photons says: a photon has no rest frame and no four-velocity, but it has a *null* four-momentum, and that null four-momentum is what enters every calculation.

**Assumption pattern.** The single fact that drives everything is $ds^2 = 0$ along a null worldline. This forces $\tau \equiv 0$ (no proper time), which forbids $dX/d\tau$ (no four-velocity), and the deeper reason is algebraic: a null vector has zero norm, and zero cannot be rescaled to one. The repair is to use the affine parameter and the four-momentum, which survive the degeneration.

**Theorem routing.** Part 1 computes $ds^2 = 0$ directly. Part 2 is the algebraic impossibility argument (rescaling preserves zero norm). Part 3 introduces the affine parameter and the null four-momentum. Part 4 checks the helix's tangent is null but the curve is not straight, distinguishing null curve from null geodesic.

**Key decision point.** The crux is recognising that the photon is not an *exception* to be patched but a *boundary case* whose surviving object must be found. The four-velocity dies, but the four-momentum lives — and the discipline is to re-express every photon statement through the four-momentum, never the (nonexistent) four-velocity.

---

# Legal Operations Used

1. **Classify a worldline by the sign of its tangent's norm** (operation 9 from the topic page). The tangent $(1,1,0,0)$ is null, placing the worldline on the light cone.

2. **Compute proper time along the worldline** (proper-time operation). The integral $\int\sqrt{ds^2}$ is identically zero for a null worldline.

3. **Use the null four-momentum as the surviving object** (operation related to invariants). When the four-velocity fails, the null four-momentum $P \cdot P = 0$ is what carries the photon through every conservation law.

---

# Hints

> [!note]- Hint 1
> Compute $ds^2 = \eta_{\mu\nu}\,dx^\mu dx^\nu$ along $x^\mu = \lambda(1,1,0,0)$: $dx^\mu = (d\lambda, d\lambda, 0, 0)$, so $ds^2 = d\lambda^2 - d\lambda^2 = 0$. Hence $\tau = \int\sqrt{ds^2} = 0$, and $dX/d\tau$ involves division by $d\tau = 0$.

> [!note]- Hint 2
> Suppose $V$ is null, $V \cdot V = 0$. Rescaling $V \mapsto cV$ gives $(cV)\cdot(cV) = c^2(V \cdot V) = 0$, never $1$. So no positive multiple of a null vector has unit norm — unlike a timelike vector, which can always be scaled to $V \cdot V = 1$.

> [!note]- Hint 3
> Set $P^\mu = dX^\mu/d\lambda = (1,1,0,0)$ scaled by the photon energy $E$: $P^\mu = E(1,1,0,0)$. Check $P \cdot P = E^2(1 - 1) = 0$. The parameter $\lambda$ is *affine* (the tangent is constant), and $P$ is the natural choice of affine tangent.

> [!note]- Hint 4
> For the helix, compute the tangent $dx^\mu/d\sigma = (r, -r\sin\sigma, r\cos\sigma, 0)$ and its norm $r^2 - r^2\sin^2\sigma - r^2\cos^2\sigma = 0$: null everywhere. But the curve is not a straight line ($d^2x^\mu/d\sigma^2 \ne 0$), so it is not a null geodesic.

---

# Solution

The photon is where the massive-particle apparatus degenerates, and tracing exactly how it fails — and what survives — is the cleanest way to understand why photons are handled by four-momentum, not four-velocity. The plan: Step 1 shows proper time vanishes; Step 2 shows no unit null vector exists; Step 3 introduces the surviving null four-momentum; Step 4 distinguishes null curves from null geodesics.

**Step 1: Proper time vanishes, so the four-velocity is undefined.**

> [!note]- Derivation
> Along $x^\mu(\lambda) = \lambda(1, 1, 0, 0)$, the displacement is $dx^\mu = (d\lambda, d\lambda, 0, 0)$, so the [[Def - The Spacetime Interval|interval]] is
> $$ds^2 = (dx^0)^2 - (dx^1)^2 - (dx^2)^2 - (dx^3)^2 = d\lambda^2 - d\lambda^2 = 0.$$
> The proper time is therefore
> $$\tau = \int\sqrt{ds^2} = \int 0 = 0$$
> identically: **no proper time elapses along a photon's worldline.** A clock carried by the photon would be frozen. Since the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is defined as $U^\mu = dX^\mu/d\tau$, and $d\tau = 0$, the four-velocity would require division by zero — it is **undefined**. The proper-time machinery, which made $dX/d\tau$ a genuine four-vector for massive particles, simply does not apply.

**Step 2: There is no unit null vector — even in principle.**

> [!note]- Derivation
> One might hope to define a four-velocity by some other normalisation. The obstruction is sharper than "division by zero": there is *no unit null vector at all*. Suppose $V$ is null, $V \cdot V = 0$, and consider any rescaling $V \mapsto cV$ ($c > 0$). Then
> $$(cV)\cdot(cV) = c^2\,(V \cdot V) = c^2 \cdot 0 = 0,$$
> so *every* positive multiple of a null vector is still null, with norm $0$ — it can never be brought to $V \cdot V = 1$. Contrast the timelike case: a timelike $V$ has $V \cdot V > 0$, so $V/\sqrt{V \cdot V}$ has unit norm, giving the four-velocity. The defining feature of the four-velocity — *the unique future-directed unit tangent* — has **no null analogue**, because the unit-normalisation is impossible. A photon cannot have a four-velocity, not even by a cleverer definition.

**Step 3: The four-momentum survives, null and well-defined.**

> [!note]- Derivation
> What replaces the four-velocity is the **four-momentum**, which the photon does have. Parametrise the worldline by an [[Def - Photons and Null Geodesics|affine parameter]] $\lambda$ — one in which the tangent is constant — and set the tangent equal to the four-momentum:
> $$P^\mu = \frac{dX^\mu}{d\lambda} = E\,(1, 1, 0, 0),$$
> where the scale $E$ is the photon's energy (supplied by quantum mechanics, $E = \hbar\omega$). Its Minkowski norm is
> $$P \cdot P = E^2\big(1^2 - 1^2 - 0 - 0\big) = 0,$$
> a **null** four-vector, $P \cdot P = 0$, equivalently $E = |\mathbf{p}|$. This is the surviving object: a photon has no four-velocity but a perfectly good null four-momentum, and it is *this* that enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] on exactly the same footing as a massive particle's $P = mU$. The affine parameter $\lambda$ plays the role that proper time plays for massive particles — the distinguished parameter in which the geodesic is "straight" — but it is determined only up to $\lambda \mapsto a\lambda + b$, and it carries no clock interpretation.

**Step 4: Null curve versus null geodesic.**

> [!note]- Derivation
> A free photon follows a null *geodesic* — a null *straight line*. Not every null curve qualifies. Consider the helix
> $$x^\mu(\sigma) = (r\sigma,\ r\cos\sigma,\ r\sin\sigma,\ 0), \qquad r > 0.$$
> Its tangent is $\dfrac{dx^\mu}{d\sigma} = (r,\ -r\sin\sigma,\ r\cos\sigma,\ 0)$, with norm
> $$r^2 - r^2\sin^2\sigma - r^2\cos^2\sigma = r^2 - r^2 = 0,$$
> null at every point — so this is a **null curve**. But its second derivative is $\dfrac{d^2x^\mu}{d\sigma^2} = (0, -r\cos\sigma, -r\sin\sigma, 0) \ne 0$, so the curve is *not* a straight line: it is **not a null geodesic**, hence not the worldline of a free photon. The distinction is exactly parallel to the timelike case (a worldline can curve while staying timelike, an accelerated massive particle) — a null curve can bend while staying null — but a *free* photon, like a *free* massive particle, follows the straight (geodesic) version. The helix would require some agent continuously deflecting the light, which is not free propagation in vacuum.

> [!note]- Complete formal solution
> Along $x^\mu = \lambda(1,1,0,0)$, $ds^2 = d\lambda^2 - d\lambda^2 = 0$, so $\tau = \int\sqrt{ds^2} = 0$ and $U = dX/d\tau$ is undefined (division by $d\tau = 0$). More sharply, no unit null vector exists: rescaling a null $V$ gives $(cV)\cdot(cV) = c^2(V\cdot V) = 0 \ne 1$, so a photon cannot have a four-velocity even in principle — unlike a timelike $V$, normalisable to $V/\sqrt{V\cdot V}$. The surviving object is the null four-momentum $P^\mu = dX^\mu/d\lambda = E(1,1,0,0)$ with $P\cdot P = 0$, $\lambda$ an affine parameter; this enters conservation of four-momentum like a massive particle's. The helix $x^\mu = (r\sigma, r\cos\sigma, r\sin\sigma, 0)$ has null tangent (norm $r^2 - r^2 = 0$) but nonzero second derivative, so it is a null curve, not a null geodesic, hence not a free photon's worldline. $\blacksquare$

> [!warning] Illegal but tempting: defining a photon four-velocity as a limit $m \to 0$
> One might try to define the photon four-velocity as the $m \to 0$ limit of a massive particle's $U = \gamma(1, \mathbf{u})$ as $u \to 1$. This fails: as $u \to 1$, $\gamma \to \infty$, so the components of $U$ diverge — there is no finite limiting four-velocity. The object that *does* have a finite limit is the four-*momentum* $P = mU = m\gamma(1, \mathbf{u})$: holding the energy $E = m\gamma$ fixed while $m \to 0$ and $u \to 1$ gives a finite null $P = E(1, \hat{\mathbf{u}})$ with $P \cdot P = m^2 \to 0$. This is the right way to take the massless limit: keep the object that survives (the four-momentum, with $P \cdot P = m^2 \to 0$) and discard the one that diverges (the four-velocity). The diagnostic: when a construction degenerates, find the combination that has a finite limit — for the photon it is energy and momentum, supplied by $E = \hbar\omega$, never the four-velocity.

---

# Key Takeaways

**A photon has no four-velocity because there is no unit null vector — the obstruction is algebraic, not technical.** It is tempting to think the four-velocity is "merely" undefined for a photon because of a $0/0$ in $dX/d\tau$. The deeper truth is that no unit null vector *exists*: a null vector has zero norm, and rescaling preserves zero, so it can never be normalised to $V \cdot V = 1$. The four-velocity is *defined* to be the unique unit tangent, and the unit-normalisation has no null analogue. This is the precise sense in which the photon sits on the boundary of the theory: timelike vectors can be normalised (giving four-velocities), spacelike vectors can be normalised (to $-1$), but null vectors cannot — they are the degenerate case. The reusable lesson: whenever a normalisation $\|V\| = 1$ is required, it silently assumes $V$ is non-null, and the construction fails exactly on the light cone.

**When a construction degenerates, find the object that survives — for the photon it is the null four-momentum.** The general strategy for handling a degenerate limit is not to patch the broken object but to identify what remains finite and well-defined. The four-velocity dies as $m \to 0$ (it diverges), but the four-momentum $P = mU$ survives with a finite null limit $P \cdot P = m^2 \to 0$, its magnitude fixed not by proper time but by quantum mechanics ($E = \hbar\omega$). Everything that needed the four-velocity is re-expressed through the four-momentum, and the photon then participates in [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] exactly as a massive particle does — which is what makes Compton scattering, pair production, and the Doppler effect computable. The trigger to internalise: in any photon calculation, reach for $P_\gamma$ with $P_\gamma \cdot P_\gamma = 0$ (an even stronger simplifier than the massive mass-shell relation, since the term vanishes), and never write a photon four-velocity.

**Null geodesic versus null curve: free propagation is straight, exactly as for massive particles.** The condition "all tangents null" defines a null *curve*, but a *free* photon follows the stronger condition of a null *geodesic* — a null straight line. The helix example shows these are genuinely different: a curve can be null at every point yet bend, just as a massive worldline can be timelike yet accelerate. The parallel is exact and worth holding: free massive particles follow timelike geodesics (straight timelike lines, [[Thm - Inertial Worldlines Maximise Proper Time|maximising proper time]]), free photons follow null geodesics (straight null lines), and in both cases "free" means "geodesic". A bending null curve, like an accelerating massive worldline, requires an external agent. In [[Special Relativity XXV — Toward Relativistic Gravitation|curved spacetime]] this is exactly how gravity acts on light: it bends null geodesics (gravitational lensing), the massless analogue of how it bends the timelike geodesics of free-falling matter. See [[Def - Photons and Null Geodesics]] for the light-cone structure these geodesics generate.
