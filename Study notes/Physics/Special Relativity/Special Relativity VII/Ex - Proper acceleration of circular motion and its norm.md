---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Expression of the Four-Acceleration"
  - "Def - Acceleration Relative to an Observer"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A particle $\mathcal{P}$ moves in uniform circular motion in the $e_1$–$e_2$ plane of an inertial observer $\mathcal{O}$:
$$x^1 = R\cos\Omega t,\qquad x^2 = R\sin\Omega t,\qquad x^3 = 0,\qquad R\Omega < 1.$$
Working with $c = 1$:

1. Compute the relative acceleration $\boldsymbol\gamma$ and show it is purely centripetal, $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$, with magnitude $|\boldsymbol\gamma| = R\Omega^2$. Verify directly that $\boldsymbol\gamma$ is transverse to the relative velocity $\mathbf V$.
2. Using the norm formula of [[Thm - Expression of the Four-Acceleration|the four-acceleration]], compute the proper acceleration $\|A\|_g$ for this transverse case, and simplify to $\|A\|_g = \Gamma^2 R\Omega^2$. Show it is constant in time.
3. Re-derive the proper acceleration by the four-vector route: write the four-velocity components, differentiate to get $A^\alpha$, and compute $\|A\|_g = \sqrt{-A\cdot A}$ directly. Confirm it matches part 2.
4. Compare the proper acceleration $\Gamma^2 R\Omega^2$ to the relative (observed) acceleration $R\Omega^2$. By what factor does the proper acceleration exceed the observed one, and what is the limiting behaviour as the rim speed $R\Omega \to 1$? Comment on the relevance to synchrotron radiation.

**Recall:**

The exercise rests on the expression of the four-acceleration and the two notions of acceleration.

![[Thm - Expression of the Four-Acceleration#Statement]]

For *transverse* acceleration ($\boldsymbol\gamma \perp \mathbf V$, so $\gamma_\parallel = 0$, $\gamma_\perp = |\boldsymbol\gamma|$), the proper-acceleration norm reduces to $\|A\|_g = \Gamma^2|\boldsymbol\gamma|$. The [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm{d}U/\mathrm{d}\tau'$ is orthogonal to $U$ and spacelike, with $\|A\|_g = \sqrt{-A\cdot A}$ the proper acceleration.

---

# Convergent Strategy

**Problem class.** An *acceleration* problem combining the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|third strategy]] with a frame-invariance check: compute the proper acceleration two independent ways (via the expression theorem, and via the raw four-vector) and confirm they agree.

**Assumption pattern.** Circular motion gives *transverse* acceleration ($\boldsymbol\gamma \perp \mathbf V$), the complementary case to the collinear one, so the norm formula reduces to $\Gamma^2|\boldsymbol\gamma|$ (a single power of $\Gamma^2$, versus $\Gamma^3$ for collinear). Constant speed (from the circular geometry) means constant $\Gamma$, so the proper acceleration is constant. The instruction to "re-derive by the four-vector route" signals the independent-method confirmation.

**Theorem routing.** Part 1 differentiates the trajectory twice for $\boldsymbol\gamma$ ([[Def - Acceleration Relative to an Observer]]) and checks transversality. Part 2 applies the transverse case of [[Thm - Expression of the Four-Acceleration]], $\|A\|_g = \Gamma^2|\boldsymbol\gamma| = \Gamma^2 R\Omega^2$. Part 3 computes $A^\alpha = \mathrm{d}u^\alpha/\mathrm{d}\tau'$ from the four-velocity components and forms $\sqrt{-A\cdot A}$ — the [[Def - Four-Velocity and Four-Acceleration|raw definition]] — as an independent check. Part 4 compares the two accelerations and takes the ultra-relativistic limit.

**Key decision point.** The instructive subtlety is the *difference between transverse and parallel acceleration weighting*: transverse acceleration enters the proper acceleration with a factor $\Gamma^2$, parallel with $\Gamma^3$. The natural error is to use the collinear factor $\Gamma^3$ by reflex; the correct factor for circular (transverse) motion is $\Gamma^2$, and getting this right is the whole point of distinguishing $\gamma_\parallel$ from $\gamma_\perp$ in the norm formula. The two-method confirmation in part 3 guards against sign errors in the mostly-minus metric.

---

# Legal Operations Used

1. **Differentiate the trajectory to get the relative acceleration** (operation 6 from the topic page). Two differentiations of $x^i(t)$ give $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$.

2. **Specialise to the simplest case** (operation 7). The transverse condition $\gamma_\parallel = 0$ collapses the norm formula to $\Gamma^2|\boldsymbol\gamma|$.

3. **Evaluate a four-vector invariant in any frame** (operation 9). The proper acceleration $\|A\|_g = \sqrt{-A\cdot A}$ is computed directly from the four-acceleration components and is frame-independent.

4. **Compute in the observer's own frame** (operation 5). Both routes are carried out in the inertial frame with $e_0 = U_0$, where the components are explicit.

---

# Hints

> [!note]- Hint 1
> Differentiate twice: $\boldsymbol\gamma = \mathrm{d}^2\mathbf x/\mathrm{d}t^2 = (-R\Omega^2\cos\Omega t, -R\Omega^2\sin\Omega t, 0) = -\Omega^2\overrightarrow{OM}$, magnitude $R\Omega^2$. For transversality, dot with $\mathbf V = (-R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$: the product $\boldsymbol\gamma\cdot\mathbf V = R^2\Omega^3(\sin\Omega t\cos\Omega t - \cos\Omega t\sin\Omega t) = 0$.

> [!note]- Hint 2
> Transverse means $\gamma_\parallel = \boldsymbol\gamma\cdot\hat{\mathbf V} = 0$ and $\gamma_\perp = |\boldsymbol\gamma| = R\Omega^2$. The norm formula $\|A\|_g = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}$ becomes $\Gamma^2\sqrt{0 + (R\Omega^2)^2} = \Gamma^2 R\Omega^2$. Constant because $\Gamma = (1-R^2\Omega^2)^{-1/2}$ is constant.

> [!note]- Hint 3
> The four-velocity is $u^\alpha = \Gamma(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$. Differentiate with respect to proper time $\tau'$ using $\mathrm{d}/\mathrm{d}\tau' = \Gamma\,\mathrm{d}/\mathrm{d}t$ (and $\Gamma$ constant): $A^\alpha = \Gamma\,\mathrm{d}u^\alpha/\mathrm{d}t = \Gamma^2(0, -R\Omega^2\cos\Omega t, -R\Omega^2\sin\Omega t, 0)$. Then $A\cdot A = -(A^1)^2 - (A^2)^2 = -\Gamma^4 R^2\Omega^4$, so $\|A\|_g = \Gamma^2 R\Omega^2$.

> [!note]- Hint 4
> Proper acceleration $\Gamma^2 R\Omega^2$ exceeds the observed $R\Omega^2$ by the factor $\Gamma^2$. As $R\Omega \to 1$, $\Gamma \to \infty$, so $\Gamma^2 \to \infty$: the proper acceleration diverges. Radiated power scales as $\|A\|_g^2 \propto \Gamma^4$, which is why circular accelerators (synchrotrons) radiate so fiercely at high energy.

---

# Solution

The route is to compute the centripetal relative acceleration, confirm it is transverse, apply the transverse case of the norm formula, then re-derive the same proper acceleration from the raw four-vector as a cross-check, and finally compare the two accelerations. Step 1 gives $\boldsymbol\gamma$ and transversality; Step 2 applies the $\Gamma^2$ formula; Step 3 confirms by the four-vector route; Step 4 contrasts proper and observed acceleration. The non-obvious thread is that transverse acceleration carries a factor $\Gamma^2$ (not $\Gamma^3$), and the independent four-vector computation guards against metric-sign slips.

**Step 1: The relative acceleration is centripetal, $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$, magnitude $R\Omega^2$, transverse to $\mathbf V$.**

> [!note]- Derivation
> From [[Ex - Components of the relative velocity and the four-velocity|the velocity computation]], $\mathbf V = (-R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$. Differentiate again:
> $$\boldsymbol\gamma = \frac{\mathrm{d}^2\mathbf x}{\mathrm{d}t^2} = \big(-R\Omega^2\cos\Omega t,\ -R\Omega^2\sin\Omega t,\ 0\big) = -\Omega^2\,(R\cos\Omega t, R\sin\Omega t, 0) = -\Omega^2\overrightarrow{OM}.$$
> This points from the particle toward the centre of the circle (opposite to $\overrightarrow{OM}$), with magnitude
> $$|\boldsymbol\gamma| = \Omega^2|\overrightarrow{OM}| = R\Omega^2,$$
> the familiar centripetal acceleration. Check transversality by dotting with the relative velocity:
> $$\boldsymbol\gamma\cdot\mathbf V = (-R\Omega^2\cos\Omega t)(-R\Omega\sin\Omega t) + (-R\Omega^2\sin\Omega t)(R\Omega\cos\Omega t) = R^2\Omega^3(\sin\Omega t\cos\Omega t - \sin\Omega t\cos\Omega t) = 0.$$
> So $\boldsymbol\gamma \perp \mathbf V$: the acceleration is purely transverse to the velocity, which is why the speed (and $\Gamma$) stays constant — a transverse acceleration turns the velocity without changing its magnitude.

**Step 2: The proper acceleration is $\|A\|_g = \Gamma^2 R\Omega^2$, constant in time.**

> [!note]- Derivation
> For transverse acceleration the parallel component vanishes, $\gamma_\parallel = \boldsymbol\gamma\cdot\hat{\mathbf V} = 0$, and the transverse component is $\gamma_\perp = |\boldsymbol\gamma| = R\Omega^2$. The norm formula of [[Thm - Expression of the Four-Acceleration|the four-acceleration]] gives
> $$\|A\|_g = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2} = \Gamma^2\sqrt{0 + (R\Omega^2)^2} = \Gamma^2 R\Omega^2.$$
> Since the speed is constant, $|\mathbf V| = R\Omega$, the Lorentz factor $\Gamma = (1 - R^2\Omega^2)^{-1/2}$ is constant, and therefore so is the proper acceleration $\|A\|_g = \Gamma^2 R\Omega^2$. Note the weighting: transverse acceleration enters with a *single* factor $\Gamma^2$, in contrast to the $\Gamma^3$ that weights collinear acceleration — the norm formula treats parallel and transverse accelerations differently, and circular motion is the clean transverse case.

**Step 3: The four-vector route gives the same $\|A\|_g = \Gamma^2 R\Omega^2$.**

> [!note]- Derivation
> The four-velocity components are $u^\alpha = \Gamma(1, -R\Omega\sin\Omega t, R\Omega\cos\Omega t, 0)$ (constant $\Gamma$). The four-acceleration is $A = \mathrm{d}U/\mathrm{d}\tau' = \Gamma\,\mathrm{d}U/\mathrm{d}t$ (using $\mathrm{d}/\mathrm{d}\tau' = \Gamma\,\mathrm{d}/\mathrm{d}t$):
> $$A^\alpha = \Gamma\,\frac{\mathrm{d}u^\alpha}{\mathrm{d}t} = \Gamma\cdot\Gamma\big(0,\ -R\Omega^2\cos\Omega t,\ -R\Omega^2\sin\Omega t,\ 0\big) = \Gamma^2\big(0,\ -R\Omega^2\cos\Omega t,\ -R\Omega^2\sin\Omega t,\ 0\big).$$
> (The time component vanishes because $u^0 = \Gamma$ is constant.) Now compute the Minkowski norm, remembering the mostly-minus signs:
> $$A \cdot A = (A^0)^2 - (A^1)^2 - (A^2)^2 - (A^3)^2 = 0 - \Gamma^4 R^2\Omega^4\cos^2\Omega t - \Gamma^4 R^2\Omega^4\sin^2\Omega t - 0 = -\Gamma^4 R^2\Omega^4.$$
> So $A$ is spacelike ($A\cdot A < 0$), and the proper acceleration is
> $$\|A\|_g = \sqrt{-A\cdot A} = \sqrt{\Gamma^4 R^2\Omega^4} = \Gamma^2 R\Omega^2,$$
> in exact agreement with Step 2. The two independent routes — the norm formula and the raw four-vector — give the same answer, confirming the computation and the sign handling. (As a further check, $A \cdot U = \Gamma^3(0\cdot 1 - (-R\Omega^2\cos)(-R\Omega\sin) - (-R\Omega^2\sin)(R\Omega\cos)) = 0$, so $A$ is orthogonal to $U$, as every four-acceleration must be.)

**Step 4: The proper acceleration exceeds the observed by $\Gamma^2$; it diverges as $R\Omega \to 1$, driving synchrotron radiation.**

> [!note]- Derivation
> The observed (relative) acceleration is $|\boldsymbol\gamma| = R\Omega^2$; the proper acceleration is $\|A\|_g = \Gamma^2 R\Omega^2$. The ratio is
> $$\frac{\|A\|_g}{|\boldsymbol\gamma|} = \Gamma^2 = \frac{1}{1 - R^2\Omega^2}.$$
> The proper acceleration — what the particle "feels" and what governs its radiation — exceeds the lab-observed acceleration by $\Gamma^2$. As the rim speed approaches light, $R\Omega \to 1^-$, the Lorentz factor diverges and so does the proper acceleration:
> $$\lim_{R\Omega\to1^-}\|A\|_g = \lim_{R\Omega\to1^-}\frac{R\Omega^2}{1-R^2\Omega^2} = +\infty.$$
> This has a dramatic experimental consequence. A relativistic charged particle radiates power proportional to the *square* of its proper acceleration (the relativistic Larmor formula), so the radiated power scales as $\|A\|_g^2 \propto \Gamma^4$. In a circular accelerator (a synchrotron) the acceleration is transverse and the particles are ultra-relativistic ($\Gamma \gg 1$), so they radiate enormously — the $\Gamma^4$ scaling is why synchrotron radiation is the dominant energy loss in circular electron machines and why very-high-energy electron colliders must be linear (where the acceleration is parallel and the geometry avoids the perpetual transverse acceleration of a ring). The factor $\Gamma^2$ separating proper from observed acceleration, innocuous at low speed, becomes the decisive engineering constraint at high energy. This connects to the radiation analysis of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!note]- Complete formal solution
> Differentiating the circular trajectory twice gives the [[Def - Acceleration Relative to an Observer|relative acceleration]] $\boldsymbol\gamma = -\Omega^2\overrightarrow{OM}$, centripetal, of magnitude $R\Omega^2$, and transverse to $\mathbf V$ (since $\boldsymbol\gamma\cdot\mathbf V = 0$). Being transverse ($\gamma_\parallel = 0$, $\gamma_\perp = R\Omega^2$), the proper-acceleration norm from [[Thm - Expression of the Four-Acceleration|the four-acceleration]] is $\|A\|_g = \Gamma^2\gamma_\perp = \Gamma^2 R\Omega^2$, constant since $\Gamma = (1-R^2\Omega^2)^{-1/2}$ is. Independently, the four-acceleration components are $A^\alpha = \Gamma^2(0, -R\Omega^2\cos\Omega t, -R\Omega^2\sin\Omega t, 0)$, giving $A\cdot A = -\Gamma^4 R^2\Omega^4$ and $\|A\|_g = \sqrt{-A\cdot A} = \Gamma^2 R\Omega^2$ — confirming the norm formula. The proper acceleration exceeds the observed $R\Omega^2$ by $\Gamma^2$, diverging as $R\Omega\to1$; since radiated power scales as $\|A\|_g^2 \propto \Gamma^4$, this is the origin of synchrotron radiation in circular accelerators. $\blacksquare$

---

# Key Takeaways

**Transverse acceleration is weighted by $\Gamma^2$, parallel by $\Gamma^3$ — circular motion is the clean transverse case.** The norm formula $\|A\|_g = \Gamma^2\sqrt{\Gamma^2\gamma_\parallel^2 + \gamma_\perp^2}$ treats the two components of the relative acceleration differently: a component *along* the velocity (which changes the speed) is amplified by $\Gamma^3$ in the proper acceleration, a component *across* it (which turns the velocity) by only $\Gamma^2$. Circular motion has purely transverse acceleration, so its proper acceleration is $\Gamma^2|\boldsymbol\gamma|$; uniformly accelerated linear motion has purely parallel acceleration, so its proper acceleration is $\Gamma^3|\boldsymbol\gamma|$. The reusable diagnostic: before applying the norm formula, decompose the relative acceleration into parallel and transverse parts, and remember the different weightings. Getting the weighting wrong — using $\Gamma^3$ for circular motion or $\Gamma^2$ for linear — is the standard error, and it matters quantitatively (a factor of $\Gamma$, which is large at high speed). The physical reason for the difference: parallel acceleration fights the speed ceiling directly (hence the extra $\Gamma$), while transverse acceleration does not change the speed at all.

**Compute invariants two independent ways as a sign check, especially in the mostly-minus metric.** The exercise deliberately computes the proper acceleration twice — once via the norm formula (which packages the result) and once from the raw four-acceleration components (which exposes every metric sign). The agreement is a genuine check: in the mostly-minus signature, a dropped sign in $A \cdot A = (A^0)^2 - \sum (A^i)^2$ would silently corrupt the answer, and the cross-check catches it. The further check $A \cdot U = 0$ (the four-acceleration is orthogonal to the four-velocity) is a third, independent verification that costs almost nothing. The reusable practice: when a frame-independent quantity (a norm, an invariant scalar) can be computed by a packaged formula and by a direct component calculation, do both — the formula is fast but opaque, the components are slow but transparent, and their agreement certifies both the algebra and the sign conventions. This frame-invariance and method-invariance discipline is the master sanity test of relativistic computation.

**Proper acceleration governs radiation, and its $\Gamma^2$ excess over observed acceleration is why synchrotrons radiate so fiercely.** The proper acceleration $\|A\|_g$ is not just a kinematic curiosity — it is the quantity that drives the radiation of a charged particle, via the relativistic Larmor formula in which the radiated power scales as $\|A\|_g^2$. For circular motion, $\|A\|_g = \Gamma^2 R\Omega^2$, so the power scales as $\Gamma^4$: at the high Lorentz factors of a modern electron synchrotron, this is a colossal energy loss, and it is the fundamental reason that the highest-energy electron–positron colliders (and proposed future ones) are *linear* — a linac accelerates parallel to the motion and avoids the perpetual transverse acceleration that a storage ring imposes. The reusable insight is that the distinction between proper and observed acceleration, which seems like pedantry at low speed (they differ by $\Gamma^2 \approx 1$), becomes the dominant design constraint of accelerator physics at high speed. The trigger: whenever a charged particle is accelerated, especially transversely and relativistically, the radiated power is controlled by the *proper* acceleration $\|A\|_g$, amplified over the observed acceleration by powers of $\Gamma$ — the full radiation theory is in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].
